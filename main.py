from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database: store users as key-value pairs
users_db = {
    1: {"user_id": 1, "name": "John", "age": 25, "email": "john@example.com"},
    2: {"user_id": 2, "name": "Alice", "age": 30, "email": "alice@example.com"},
    3: {"user_id": 3, "name": "Bob", "age": 28, "email": "bob@example.com"}
}
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/page")
async def read_index(request: Request):
    """Serve the index.html template"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get user from key-value dictionary"""
    if user_id in users_db:
        return users_db[user_id]
    else:
        return {"error": f"User {user_id} not found"}

@app.get("/get-user")
async def get_user_by_param(user_id: int):
    """Get user using query parameter: ?user_id=1"""
    if user_id in users_db:
        return users_db[user_id]
    else:
        return {"error": f"User {user_id} not found"}

@app.get("/all-users")
async def get_all_users():
    """Get all users from key-value dictionary"""
    return {"users": users_db}

# Define a data model for POST requests
class Item(BaseModel):
    name: str
    email: str
    message: str

@app.post("/submit")
async def submit_form(item: Item):
    """Handle form submission via POST"""
    return {
        "status": "success",
        "message": f"Thank you {item.name}, we received your message!",
        "data": {
            "name": item.name,
            "email": item.email,
            "message": item.message
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
