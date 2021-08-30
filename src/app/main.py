import uvicorn
from fastapi import FastAPI

from app.api import vk_callback

app = FastAPI(debug=True)
app.include_router(vk_callback.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
