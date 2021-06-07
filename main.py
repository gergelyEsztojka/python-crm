from fastapi import FastAPI
from crm.routers import authentication, user

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
