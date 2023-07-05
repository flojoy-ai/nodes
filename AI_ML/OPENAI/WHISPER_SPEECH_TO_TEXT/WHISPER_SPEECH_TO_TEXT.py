from flojoy import flojoy, DataContainer
from typing import List
import openai
import pandas as pd
import os
from pathlib import Path


ACCEPTED_AUDIO_FORMATS = ["mp3"]


@flojoy
def WHISPER_SPEECH_TO_TEXT(dc: List[DataContainer], params):
    """
    The WHISPER_SPEECH_TO_TEXT node uses OpenAI whisper transcription model to 
    convert audio to text.

    Parameters
    ----------
    file_path: string
        Path to the audio file to be transcribed. Only mp3 format is supported.
    """

    file_path = params.get("file_path")
    if file_path is None:
        raise ValueError("file_path parameter is missing!")
    
    file_format = file_path.split(".")[-1]
    if file_format not in ACCEPTED_AUDIO_FORMATS:
        raise ValueError(f"file format {file_format} is not supported. Supported formats are {ACCEPTED_AUDIO_FORMATS}")
    
    file_path = Path(file_path)
    if not file_path.exists():
        raise ValueError(f"file {file_path} does not exist!")

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    model = 'whisper-1'
    with open(file_path, 'rb') as f:
        transcript = openai.Audio.translate(model, f)

    transcript_text = transcript.get('text')
    transcription_df = pd.DataFrame(data={
        'text': [transcript_text]
    })

    return DataContainer(
        type='dataframe',
        m=transcription_df
    )