import hashlib
from .db import get_user_by_email, create_user

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash

def signup(name: str, email: str, password: str) -> str:
    if get_user_by_email(email):
        return "Email already registered."
    ph = hash_password(password)
    try:
        create_user(name, email, ph)
        return "OK"
    except Exception as e:
        return f"Error creating user: {e}"

def login(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        return None
    if verify_password(password, user['password_hash']):
        return {"id": user["id"], "name": user["name"], "email": user["email"]}
    return None
