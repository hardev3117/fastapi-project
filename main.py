from fastapi import FastAPI
# import uvicorn
import usersController  # assuming your router is in app/routers/users.py

app = FastAPI()

app.include_router(usersController.router, prefix="/api/v1", tags=["Users"])


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)