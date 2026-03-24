import requests

GITHUB_API = "https://api.github.com"

def get_user_gists(username: str, page: int = 1, per_page: int = 5):
    url = f"{GITHUB_API}/users/{username}/gists?page={page}&per_page={per_page}"
    
    response = requests.get(url, timeout=5)

    if response.status_code == 404:
        raise Exception("User not found")

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    gists = response.json()

    return [
        {
            "id": gist.get("id"),
            "description": gist.get("description") or "No description",
            "url": gist.get("html_url")
        }
        for gist in gists
    ]