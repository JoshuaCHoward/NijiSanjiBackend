from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import src.app.routes.index as index

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.routes.router)
