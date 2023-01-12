from starlite import CORSConfig, Starlite, put
from tinydb import TinyDB, Query

# from pydantic import BaseModel


@put("/data/add")
def add_data(data: dict) -> None:
    version = data.pop("version")
    tinydb_filepath = f"./data/{version}.json"
    db = TinyDB(tinydb_filepath)
    db.upsert(data, Query()["hashId"] == data["hashId"])


# For development, allows CORS requests.
cors_config = CORSConfig(
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = Starlite(route_handlers=[add_data], cors_config=cors_config, debug=True)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
