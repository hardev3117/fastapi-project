# container.py
from dependency_injector import containers, providers
from repositories.UserRepository import UserRepository
from services.user_service import UserService

class Container(containers.DeclarativeContainer):
    user_repository = providers.Singleton(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repository)

