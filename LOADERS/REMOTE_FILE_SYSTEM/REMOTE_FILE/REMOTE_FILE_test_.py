import pytest

from flojoy import Image


def test_REMOTE_FILE_img(mock_flojoy_decorator):
    file_url = "https://datasets-server.huggingface.co/assets/BalajiAIdev/autotrain-data-animal-image-classification/--/default/train/0/image/image.jpg"  # noqa: E501
    import REMOTE_FILE

    output = REMOTE_FILE.REMOTE_FILE(file_url=file_url, file_type="Image")

    assert isinstance(output, Image)


@pytest.mark.parametrize(
    "file_url",
    [
        "not_valid",
        "/not/a/valid/url",
        "ftp://not_existing.url",
        "htp://misstyped.url",
    ],
)
def test_REMOTE_FILE_not_valid(file_url):
    import REMOTE_FILE

    with pytest.raises(ValueError):
        REMOTE_FILE.REMOTE_FILE(file_url=file_url, file_type="Image")
