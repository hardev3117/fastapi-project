from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/test"

engine = create_engine(DATABASE_URL, echo=True, future=True)


# def list_users():
#         query = text("select * from users_main;")
#         with engine.connect() as conn:
#             result = conn.execute(query)
#             users = [{"id": row[0], "name": row[1]} for row in result]
#         return users

# result = list_users()

# print(result)