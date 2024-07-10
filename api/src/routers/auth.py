import os
import firebase_admin
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import credentials, auth
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

credentials_path = os.getenv("FIREBASE_SECRETS_PATH")
credentials = credentials.Certificate(credentials_path)
firebase_admin.initialize_app(credentials)

# 認証関数の定義
def get_current_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not cred:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    try:
        cred = auth.verify_id_token(cred.credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return cred

@router.get("/auth/me")
async def get_me(cred = Depends(get_current_user)):
    uid = cred.get("uid")
    return {"message": f"Hello, {uid}!"}