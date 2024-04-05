import pytest
from httpx import AsyncClient


@pytest.mark.asyncio(scope="session")
async def test_validate_images(aclient: AsyncClient):
    wrong_response = await aclient.post(
        "/validate", json={"images_list": ["test"], "detail": "low"}
    )

    assert wrong_response.status_code == 400
    assert wrong_response.json() == {
        "code": 400,
        "message": "wrong request, no valid link",
    }

    correct_response = await aclient.post(
        "/validate",
        json={
            "images_list": [
                "https://storage.googleapis.com/holywater/Assets%20Folder/DONE/PS_S1111/image_json_t1/jTwBSXFZjryviLywdr2fOMc1xKt.jpg"
            ]
        },
    )

    assert correct_response.status_code == 200
    assert bool(correct_response.json()["images_list"]) == True
