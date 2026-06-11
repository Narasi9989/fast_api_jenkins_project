from fastapi import FastAPI
from routes.employees import router
from db.database import get_connection

app = FastAPI()

@app.on_event("startup")
def startup():

    try:
        conn = get_connection()
        conn.close()
        print("Oracle connection successful")

    except Exception as e:
        print("Database connection failed")
        print(e)

app.include_router(router)