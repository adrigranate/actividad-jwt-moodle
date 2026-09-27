from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import hash_password, verify_password, create_token, get_current_user

app = FastAPI(title="Actividad JWT - FastAPI")

USERS_DB = {
    "estudiante_user": {
        "username": "estudiante_user",
        "hashed_password": hash_password("pass123"),
        "role": "estudiante"
    },
    "admin_user": {
        "username": "admin_user",
        "hashed_password": hash_password("admin123"),
        "role": "admin"
    }
}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USERS_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_token(data={"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/publico")
def ruta_publica():
    return {"mensaje": "Endpoint público: Libre acceso sin token"}

@app.get("/privado")
def ruta_privada(current_user: dict = Depends(get_current_user)):
    return {"mensaje": f"Bienvenido {current_user['username']}.", "usuario": current_user}

@app.get("/admin")
def ruta_admin(current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso prohibido: Se requiere rol de administrador"
        )
    return {"mensaje": "Bienvenido al panel de administración."}
