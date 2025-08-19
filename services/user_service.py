# services/user_service.py
from repositories.IUserRepository import IUserRepository
from models import User

class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def list_users(self):
        return self.user_repo.get_all()

    def get_by_id(self, user_id: int):
        return self.user_repo.get_by_id(user_id)
    
    def add_user(self, user:User):        
        return self.user_repo.add_user(user)
    
    def update_user(self, user:User):        
        return self.user_repo.update_user(user)
