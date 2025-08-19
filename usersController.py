# router implementaion is pending we will implement router in future

# main.py
from fastapi import FastAPI, Depends
from services.user_service import UserService
from dependencies import get_user_service
from fastapi import APIRouter
from models import User

router = APIRouter()


@router.post("/users/add")
def user_add(user: User,service: UserService = Depends(get_user_service)):       
    return service.add_user(user)



@router.get("/users")
def get_users(service: UserService = Depends(get_user_service)):
    return service.list_users()



@router.get("/users/{user_id}")
def get_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_by_id(user_id)
    return user if user else {"error": "User not found"}



@router.put("/users/update")
def user_update(user: User,service: UserService = Depends(get_user_service)):       
    return service.update_user(user)
