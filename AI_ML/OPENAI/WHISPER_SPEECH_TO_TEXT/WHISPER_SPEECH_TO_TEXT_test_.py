from pathlib import Path
import pytest
import os


def test_WHISPER_SPEECH_TO_TEXT_no_api_key(mock_flojoy_decorator):
    import WHISPER_SPEECH_TO_TEXT

    with pytest.raises(Exception, match="OPENAI_API_KEY environment variable not set"):
        res = WHISPER_SPEECH_TO_TEXT.WHISPER_SPEECH_TO_TEXT(
            file_path="",
        )


def test_WHISPER_SPEECH_TO_TEXT_no_input_file(mock_flojoy_decorator):
    import WHISPER_SPEECH_TO_TEXT

    with pytest.raises(ValueError, match="file_path parameter is missing!"):
        res = WHISPER_SPEECH_TO_TEXT.WHISPER_SPEECH_TO_TEXT(
            default="",
            file_path="",
        )


def test_WHISPER_SPEECH_TO_TEXT(mock_flojoy_decorator):
    api_key = os.getenv("OPENAI_API_KEY", None)
    if api_key:
        import WHISPER_SPEECH_TO_TEXT

        file_path = Path(__file__).parent / "test_audio.mp3"
        res = WHISPER_SPEECH_TO_TEXT.WHISPER_SPEECH_TO_TEXT(
            file_path=file_path,
        )

        # TODO - do proper assertions

        # assert res.type == "image"
        # assert isinstance(res.r, numpy.ndarray)
        # assert isinstance(res.g, numpy.ndarray)
        # assert isinstance(res.b, numpy.ndarray)
