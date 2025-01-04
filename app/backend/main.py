from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.router import router as router_api
#from app.pages.router import router as router_page
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all sources
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods
    allow_headers=["*"],  # allow all headers
)


#app.include_router(router_auth)
app.include_router(router_api)
#app.include_router(router_page)

app.mount("/", StaticFiles(directory="frontend", html=True))
