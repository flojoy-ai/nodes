from flojoy import flojoy, DataContainer, DataFrame as FlojoyDataFrame, Bytes
from typing import List, Optional
import openai
import pandas as pd
import os
from pathlib import Path
from tempfile import NamedTemporaryFile


ACCEPTED_AUDIO_FORMATS = ["mp3", "wav"]


@flojoy
def WHISPER_SPEECH_TO_TEXT(
    default: Optional[Bytes] = None, 
    file_path: Optional[str] = None
) -> FlojoyDataFrame:
    """
    This node uses OpenAI whisper transcription model to convert audio to text.
    The audio can be provided as a file path or as bytes from a previous node.
    The previous node value has priority over the file path.

    Parameters:
    -----------
    - file_path: string
        Path to the audio file to be transcribed. Only mp3 format is supported.
    """
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    model = 'whisper-1'
    f = None
    if default and isinstance(getattr(default, 'bytes'), bytes):
        f = NamedTemporaryFile(suffix=".mp3")
        f.write(default.bytes)
        f.seek(0)
        file_path = f.name

    elif file_path is None:
        raise ValueError("file_path parameter is missing!")
    
    file_format = file_path.split(".")[-1]
    if file_format not in ACCEPTED_AUDIO_FORMATS:
        raise ValueError(f"file format {file_format} is not supported. Supported formats are {ACCEPTED_AUDIO_FORMATS}")
    
    file_path = Path(file_path)
    if not file_path.exists():
        raise ValueError(f"file {file_path} does not exist!")

    with open(file_path, 'rb') as f:
        transcript = openai.Audio.translate(model, f)

    if f is not None:
        f.close()

    transcript_text = transcript.get('text')
    transcription_df = pd.DataFrame(data={
        'text': [transcript_text]
    })

    return FlojoyDataFrame(df=transcription_df)