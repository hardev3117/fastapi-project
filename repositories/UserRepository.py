# repositories/impl.py
from repositories.IUserRepository import IUserRepository
from models import User
from sqlalchemy import text
from database import engine

class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def get_all(self):
        query = text("select id , name, age from users_main order by id ;")
        with engine.connect() as conn:
                result = conn.execute(query)
                self.users =[{"id": row[0], "name": row[1], "age":row[2]} for row in result]
        return self.users
    

    def get_by_id(self, user_id: int):
         query = text("SELECT id, name, age FROM users_main WHERE id = :user_id")
         with engine.connect() as conn:
                result = conn.execute(query, {"user_id": user_id})
                self.users =[{"id": row[0], "name": row[1], "age":row[2]} for row in result]
         return self.users
    
    
    def add_user(self, user: User):
        with engine.connect() as conn:
            # Check if user with this ID exists
            check_query = text("SELECT 1 FROM users_main WHERE id = :id")
            result = conn.execute(check_query, {"id": user.id}).fetchone()

            if result:
                return "User with this ID already exists"

            # Insert new user
            insert_query = text(
                "INSERT INTO users_main (name, age) VALUES (:name, :age)"
            )
            conn.execute(insert_query, {"name": user.name, "age": user.age})
            conn.commit()

        return {"message": "User added successfully", "user": user}
        
    
    def update_user(self, user: User):
        update_query = text("""
            UPDATE users_main
            SET name = :name,
                age = :age
            WHERE id = :id
            RETURNING id, name, age;
        """)

        with engine.connect() as conn:
            result = conn.execute(update_query, {"id": user.id, "name": user.name, "age": user.age})
            updated_user = result.fetchone()
            conn.commit()

        if updated_user:
            return {"message": "User updated successfully", "user": user}
        else:
            return {"error": "User not found"}