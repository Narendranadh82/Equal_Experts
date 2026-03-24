from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_octocat_gists():
    """
    Test basic API functionality
    """
    response = client.get("/octocat")

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "octocat"
    assert isinstance(data["gists"], list)


def test_pagination():
    """
    Test pagination functionality
    """
    response = client.get("/octocat?page=1&per_page=2")

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "octocat"
    assert isinstance(data["gists"], list)
    assert len(data["gists"]) <= 2


def test_invalid_user():
    """
    Test handling of non-existing GitHub user
    """
    response = client.get("/thisuserdoesnotexist123456")

    # Depending on your implementation, this could be 404 or 500
    assert response.status_code in [404, 500]


def test_response_structure():
    """
    Validate structure of each gist object
    """
    response = client.get("/octocat")

    assert response.status_code == 200

    data = response.json()

    if data["gists"]:  # Only check if list is not empty
        gist = data["gists"][0]

        assert "id" in gist
        assert "description" in gist
        assert "url" in gist