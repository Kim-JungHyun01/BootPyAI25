from fastapi import FastAPI # 파이썬 웹 개발 api(https://wikidocs.net/book/8531)
from pydantic import BaseModel # 유효성 검사용 판다틱
from starlette.middleware.base import BaseHTTPMiddleware
# 요청(request)과 응답(responce) 사이에 특정 작성 수행
# 미들웨어 : 모든 요청에 대해 실행되며, 요청을 처리하기전에 응답을 반환하기 전에 특정작업을 수행할 수 있음
# ex) 로깅, 인증, cors처리, 압축등...
import logging #로그 출력용

from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router

app = FastAPI( #생성자를 통해서 postman을 대체하는 문서화를 내장되어 있음(보안상 none)
    # 백검증툴
    title = "MBC AI 프로젝트 test",
    description = "파이썬과 자바부트를 연동한 ai 앱",
    version = "1.0.0",
    # 문서화 파리미터
    docs_url=None,  # http://localhost:8001/docs
    redoc_url=None # http://localhost:8001/redoc
) # FastAPI 객체생성


# 로그를 콘솔에 출력하는 용도
class LoggingMiddleware(BaseHTTPMiddleware):
    logging.basicConfig(level=logging.INFO) #로그출력추가
    async def dispatch(self, request, call_next):
        logging.info(f"Req : {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response
app.add_middleware(LoggingMiddleware) #모든 요청에 대해 로그를 남기는 미들웨어 클래스를 사용

# item 객체클래스
class Item(BaseModel): # BaseModel : 객체 연결 -> 상속
    name : str                  #필드1 : 상품명_문자열
    description : str = None    #필드2 : 설명_문자열(null)
    price : float               #필드3 : 가격_실수
    tax : float = None          #필드4 : 세금_실수(null)
# Item() end

# 컨트롤러 검증 : postman이용 | 내장된 백검증툴로 있음

@app.get("/") #http://ip주소:포트번호/ (루트컨텍스트)
async def read_root():#비동기변수메서드
    return {"Hello" : "word"}

#BaseModel : 데이터 모델링을 쉽게 도와주고, 유효성검사실행
@app.post("/items/") #post메서드용 응답
async def create_item(item : Item):
    # 잘못된 데이터 입력시 오류코드 : 422
    return item


@app.get("/items/{item_id}") # http://ip주소:포토/items/1
async def read_item(item_id : int, q:str=None):
    # item_id : 상품번호 -> 경로매개변수
    # q : 퀴리 매개변수 (기본값 : None)
    return {"item_id" : item_id, "q" : q}

# 실행문
# uvicorn main:app --reload --port 8001
# reload : 처음시작이면 시작을, 시작중이면 다시 불러오는 것
# start : 시작만 하는 것
# 서버종료
# ctrl + c
