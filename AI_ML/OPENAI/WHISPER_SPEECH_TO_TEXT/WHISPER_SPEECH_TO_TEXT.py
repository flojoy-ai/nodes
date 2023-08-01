from flojoy import flojoy, Bytes, run_in_venv, TextBlob
from typing import Optional
import os
from pathlib import Path
import time
from tempfile import NamedTemporaryFile


ACCEPTED_AUDIO_FORMATS = ["mp3", "wav"]
API_RETRY_ATTEMPTS = 5
API_RETRY_INTERVAL_IN_SECONDS = 1


@flojoy
@run_in_venv(pip_dependencies=["openai==0.27.8", "pandas==2.0.2"])
def WHISPER_SPEECH_TO_TEXT(
    default: Optional[Bytes] = None, file_path: Optional[str] = None
) -> TextBlob:
    """
    the node WHISPER_SPEECH_TO_TEXT uses OpenAI whisper transcription model to convert audio to text. The audio can be provided as a file path or as bytes from a previous node. The previous node value has priority over the file path.

    Parameters:
    -----------
    file_path: string
        Path to the audio file to be transcribed. Only mp3 format is supported.
    """
    import openai
    import pandas as pd

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OPENAI_API_KEY environment variable not set")

    openai.api_key = api_key
    model = "whisper-1"
    f = None
    if default and isinstance(getattr(default, "b"), bytes):
        f = NamedTemporaryFile(suffix=".mp3")
        f.write(default.bytes)
        f.seek(0)
        file_path = f.name

    elif file_path is None:
        raise ValueError("file_path parameter is missing!")

    file_format = file_path.split(".")[-1]
    if file_format not in ACCEPTED_AUDIO_FORMATS:
        raise ValueError(
            f"file format {file_format} is not supported. Supported formats are {ACCEPTED_AUDIO_FORMATS}"
        )

    file_path = Path(file_path)
    if not file_path.exists():
        raise ValueError(f"file {file_path} does not exist!")

    with open(file_path, "rb") as f:
        for i in range(API_RETRY_ATTEMPTS):
            try:
                transcript = openai.Audio.translate(model, f)
                print(f"No error in attempt {i} of transcription")
                break
            except openai.error.RateLimitError:
                if i > API_RETRY_ATTEMPTS:
                    raise Exception("Rate limit error. Max retries exceeded.")

                print(
                    f"Rate limit error, retrying in {API_RETRY_INTERVAL_IN_SECONDS} seconds"
                )
                time.sleep(API_RETRY_INTERVAL_IN_SECONDS)

    if f is not None:
        f.close()

    transcript_text = transcript.get("text")
    return TextBlob(text_blob=transcript_text)
