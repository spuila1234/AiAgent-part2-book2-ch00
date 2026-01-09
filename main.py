from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, Response
from datetime import datetime

app = FastAPI()

app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.get("/")
def root(message: str = "hello"):
    return {
        "message": message,
        "message_length": len(message),
        "status": "200 OK"
    }

cnt = 0

@app.get("/count")
def count():
    global cnt
    cnt += 1
    now = datetime.now()
    return {
        "count": cnt,
        "dateStr": now.strftime("%Y-%m-%d %H:%M")
    }

@app.get("/check/{client_cnt}")
def check_cnt(client_cnt: int):
    if cnt > client_cnt:
        now = datetime.now()
        return {
            "count": cnt,
            "dateStr": now.strftime("%Y-%m-%d %H:%M")
        }
    # 변경 없으면 204로 응답(권장)
    return Response(status_code=204)