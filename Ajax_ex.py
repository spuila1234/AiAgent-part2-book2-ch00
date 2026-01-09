# 임포트시 * 입력하면 해당 모델에 있는 모든 기능을 사용할 수 있다
# from fastapi import *
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# public폴더를 정적 파일 경로로 등록
app.mount("/public", StaticFiles(directory="public", html=True), name="public")


@app.get("/")
def root(message:str = "hello") :
    print("GET요청")
    return {
        "massage" : message,
        "massage length" : len(message)
    }
    
# BaseModel을 상속 받아서 Message클래스 선언
from pydantic import BaseModel

# 클라이언트에서 Ajax로 통신할때 JSON 데이터 => Post로 통신 할때는 JSON으로 데이터 전송
class Message(BaseModel) :
    text: str
    
#######################################
# post 메서드를 추가하고 postman으로 테스트 하기
# content-Type : raw로 설정 후 JSON 데이터 전송
@app.post("/")
def root(message:Message) :
    print("POST 요청")
    return {
        "massage" : message.text,
        "massage length" : len(message.text)
        # BaseModel을 상속받은 Message클래스를 상속 받음으로써 text 메서드 사용 가능
    }

# Form 파라미터 전달 받기
@app.post("/login")
def login_post(
    username:str = Form(...)
) :
    return {"username" : username}