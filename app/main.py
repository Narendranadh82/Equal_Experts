from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from app.service import get_user_gists

app = FastAPI()

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)


@app.get("/{username}")
def fetch_gists(username: str, page: int = 1, per_page: int = 5):
    try:
        gists = get_user_gists(username, page, per_page)
        return {"username": username, "gists": gists}

    except Exception as e:
        print(f"ERROR: {e}")  # 👈 Add this for debugging

        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=str(e))

        raise HTTPException(status_code=500, detail=str(e))  # 👈 show actual errorx