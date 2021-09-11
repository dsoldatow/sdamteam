from fastapi import FastAPI

from app.api import vk_callback

app = FastAPI(debug=True)
app.include_router(vk_callback.router)
