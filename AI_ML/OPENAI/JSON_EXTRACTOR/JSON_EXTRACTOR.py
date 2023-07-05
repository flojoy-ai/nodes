from flojoy import flojoy, DataContainer
from typing import List
import openai
import pandas as pd
import os
from pathlib import Path
import json
from copy import deepcopy


ACCEPTED_SCHEMA_FORMATS = [".json"]

BASE_SCHEMA = {
    "name": "information_extraction",
    "description": "Extracts the information as JSON.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

@flojoy
def JSON_EXTRACTOR(dc: List[DataContainer], params):
    """
    The JSON_EXTRACTOR node extract specific properties information from a text using JSON schema.
    Parameters:
    - properties: string
        Comma separated list of properties to extract. Example: "name,age,location"
    - prompt: string
        Text to extract information from.
    """

    properties = params.get("properties")
    prompt = params.get("prompt")

    if not properties:
        raise Exception('No properties found to extract.')
    
    properties = properties.split(',')
    schema = deepcopy(BASE_SCHEMA)
    for property in properties:
        schema['parameters']['properties'][property] = {
            'title': property,
            'type': 'string',
        }
        schema['parameters']['required'].append(property)

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        functions=[schema],
        function_call={"name": schema.get('name', 'json_extractor')},
    )

    if not response.choices:
        raise Exception('No extraction choices found in response.')

    data = json.loads(response.choices[0].message.function_call.arguments)
    df = pd.DataFrame(data=[data])
    return DataContainer(
        type='dataframe',
        m=df
    )