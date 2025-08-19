# repositories/interfaces.py
from abc import ABC, abstractmethod
from typing import List, Optional
from models import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass