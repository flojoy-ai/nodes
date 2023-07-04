from flojoy import flojoy, DataContainer
from typing import List
import openai
import pandas as pd
import os
from pathlib import Path
import json


ACCEPTED_SCHEMA_FORMATS = [".json"]


@flojoy
def JSON_EXTRACTOR(dc: List[DataContainer], params):
    """
    Extract information from a text using a JSON schema.
    Parameters:
    - schema_file_path: string
        Path to the schema file.
    - prompt: string
        Text to extract information from.
    """

    schema_file_path = params.get("schema_file_path")
    prompt = params.get("prompt")
    if schema_file_path is None:
        raise ValueError("schema_file_path is required.")
    
    schema_file_path = Path(schema_file_path)
    if not schema_file_path.exists():
        raise ValueError("schema_file_path does not exist.")
    
    schema_file_format = schema_file_path.suffix
    if schema_file_format not in ACCEPTED_SCHEMA_FORMATS:
        raise ValueError(f"schema_file_format {schema_file_format} is not supported. Supported formats are {ACCEPTED_SCHEMA_FORMATS}")
    
    with open(schema_file_path, 'r') as f:
        schema = json.load(f)
    
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