from flojoy import flojoy, DataFrame as FlojoyDataFrame, run_in_venv
import openai
import pandas as pd
import os
import json
from copy import deepcopy


ACCEPTED_SCHEMA_FORMATS = [".json"]

BASE_SCHEMA = {
    "name": "information_extraction",
    "description": "Extracts the information as JSON.",
    "parameters": {"type": "object", "properties": {}, "required": []},
}


@flojoy
@run_in_venv(
    pip_dependencies=[
        "openai==0.27.8",
        "pandas==2.0.2"
    ]
)
def JSON_EXTRACTOR(
    properties: str,
    prompt: str,
) -> FlojoyDataFrame:
    """
    The JSON_EXTRACTOR node extract specific properties information from a text using JSON schema.

    Parameters
    ----------
    properties: string
        Comma separated list of properties to extract. Example: "name,age,location"
    prompt: string
        Text to extract information from. Example: "I'm John, I am 30 years old and I live in New York."
    """

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key

    if not properties:
        raise Exception("No properties found to extract.")

    properties = properties.split(",")
    schema = deepcopy(BASE_SCHEMA)
    for property in properties:
        schema["parameters"]["properties"][property] = {
            "title": property,
            "type": "string",
        }
        schema["parameters"]["required"].append(property)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        functions=[schema],
        function_call={"name": schema.get("name", "json_extractor")},
    )

    if not response.choices:
        raise Exception("No extraction choices found in response.")

    data = json.loads(response.choices[0].message.function_call.arguments)
    df = pd.DataFrame(data=[data])
    return FlojoyDataFrame(df=df)
