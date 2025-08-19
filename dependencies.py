# dependencies.py
from services.user_service import UserService
from container import Container

container = Container()

def get_user_service() -> UserService:
    return container.user_service()
