# BootPyAI25
 스프링부트와 파이썬 AI 협업모듈

---
# 개발환경구축

1. 파이썬 인터프리터 : 3.12버전 (http://www.python.org/)
2. IDE 설치 : 커뮤니티버전 (https://www.jetbrains.com/ko-kr/pycharm/download/?section=windows)
3. FastAPI 설치(https://velog.io/@hwaya2828/WSGI-ASGI)
   - pip install fastapi uvicorn uvicorn
    - ASGI(Asynchronus Server Gateway Interface): 파이썬에서 비동기 웹서버와 웹애플케이션 간의 인터페이스
    - 표준 ASGI는 기준 WSGI(Web Server Gateway Interface)의 비동기 버전으로, 파이썬에서 비동기 처리를 지원하는 웹 애플리케이션을 구축하기 위함

---
- ASGI 특징
   - 비동기 지원 : 비동기 코드 실행을 지원하며 높은 성능과 동시성을 제공, 웹소켓이나 서버 추시와 같은 비동기 통신이 필요한 애플리케이션에 유용
   - 범용성 : HTTP뿐만 아니라, WebSocket, gRPC와 같은 다른 프로토콜로 지원
   - 유연성 : ASGI 애플리케이션은 다앙햔 서버 및 프레임워크와 호환되며, 모듈식으로 구성

- FastAPI와 ASGI
   - ASGI 표준을 따르는 웹 ㅡ레임 워크
   - 애플리케이션은 비동기 처리를 기본으로 하며, Uvicorn과 같은 ASGI 서버를 사용하여 높은 성능을 제공

---
- FastAPI 서버 실행
 1. main.py실행
 2. Terminal : D:\phthonWorkSpace> uvicorn main:app --reload --port 8001(위치확인)
---
![image](https://github.com/user-attachments/assets/844509cd-81a7-46b4-a703-7ab202388358)

---
# 실시간 영상 스트리밍
![image](https://private-user-images.githubusercontent.com/112685332/389747091-c7575a67-b3c6-49a2-afec-1756ff476946.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1NDg0MzAsIm5iZiI6MTczODU0ODEzMCwicGF0aCI6Ii8xMTI2ODUzMzIvMzg5NzQ3MDkxLWM3NTc1YTY3LWIzYzYtNDlhMi1hZmVjLTE3NTZmZjQ3Njk0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIwM1QwMjAyMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04M2MxOGJhYzFmNWI4NWNjMTVhNjJlYmQ3N2IwNjgwOTc4NmYzYzEzMGZiZGRkODllN2ZhYzdkOGQ1NmYxMDA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.DP2KlUTM6SkzkmGJJl_ELSQmHqxfbC_2XmoTd0V4JjM)
