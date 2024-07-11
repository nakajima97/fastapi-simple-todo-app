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

tags = ["auth"]

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

@router.get("/auth/me", tags=tags, summary="ログインユーザ情報取得")
async def get_me(cred = Depends(get_current_user)):
    '''
    ログインしているユーザの情報を返す
    '''
    uid = cred.get("uid")
    return {"message": f"Hello, {uid}!"}

@router.post('/auth/sign_in', tags=tags, summary="ユーザ登録")
async def sign_in():
    '''
    ユーザ登録する
    '''
    # TODO: ユーザテーブルにユーザ情報を登録する処理を書く
    # TODO: すでに登録されているユーザの場合はエラーを返す
    # TODO: モデル・マイグレーションファイルの作成からやる

    return {"message": "sign in success"}