# 실시간 웹캡 연결
# 1. 선행준비
#   1) ip 카메라준비
#   2) ip 카메라 관련 네트워크 설정
#   3) vms 프로그램설치_ip, 암호, rtsp 프로토콜 활성화

# 2. 파이썬과 프론트를 연동하는 mqtt api를 활용
#   1) 설치
#   MQTT : 실시간 출력 프로토콜(https://underflow101.tistory.com/22)
#   MQTT 브로커용 프로그램 모스키토 api를 활용
#   버전 : mosquitto-2.0.18 사용(https://mosquitto.org/download/)
#   모스키도 환경설정변경_위치 : #Listener (C:\Program Files\mosquitto\mosquitto.conf)
#   #MQTT 기본 리스너 설정
#   listener 1883
#   protocol mqtt
#
#   #WebSocket 리스너 설정
#   listener 9001
#   protocol websockets
#
#   #익명의 접속 허용
#   allow_anonymous true

# 3. 환경설정 적용실행(환경설정파일, 방화벽, 서비스)
#   1) 방화벽 설정 추가(터미널실행) -> 실행(wf.msc) -> 1883, 9001열기
#   2) mosquitto 실행(cmd실행) : C:\Program Files\mosquitto>mosquitto -c mosquitto.conf -v
#                            : cd\ -> cd "Program Files" -> cd "mosquitto"
#   2-1) 2)가 안될경우 : services.msc에 가서 서비스 재실행


import base64
import io
from PIL import Image
import numpy as np
import json
from ultralytics import YOLO
# ↓ paho.mqtt: 브로커 추가(→mosquitto 실행 필수)
import paho.mqtt.client as mqtt
import cv2
import time

model = YOLO('yolov8n.pt')
client = mqtt.Client()  # mosquitto -c mosquitto.conf -v
topic = '/camera/objects'  # 경로
client.connect('localhost', 1883, 60)  # maxdata 조절용


# 연결용 함수
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")


# 객체 감지용 색상 함수
def get_colors(num_colors):
    np.random.seed(0)
    colors = [tuple(np.random.randint(0, 255, 3).tolist()) for _ in range(num_colors)]
    return colors


# 모델에서 받은 클래스 이름
class_names = model.names
num_classes = len(class_names)  # 클래스 번호
colors = get_colors(num_classes)  # 사각박스 컬러색

client.on_connect = on_connect  # 클라이언트 연결정보(https://deep-learning-study.tistory.com/107)
cap = cv2.VideoCapture('rtsp://admin:mbc312AI!!@192.168.0.5:554/mbcai312')  # rtsp 정보(vms 참고)


# https://deep-learning-study.tistory.com/107
# 참고용_ java 프론트에서 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
# bRec = False
# PrevTime = 0

############################# 전처리 #############################
# 모델 객체를 탐지용 함수
def detect_objects(image: np.array):
    results = model(image, verbose=False)
    class_names = model.names

    for result in results:
        boxes = result.boxes.xyxy
        confidences = result.boxes.conf
        class_ids = result.boxes.cls
        for box, confidence, class_id in zip(boxes, confidences, class_ids):
            x1, y1, x2, y2 = map(int, box)
            label = class_names[int(class_id)]
            cv2.rectangle(image, (x1, y1), (x2, y2), colors[int(class_id)], 2)
            cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[int(class_id)], 2)

    return image


# 객체탐지 반복용 루프
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    result_image = detect_objects(frame)

    # base64인코딩
    _, buffer = cv2.imencode('.jpg', result_image)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    payload = json.dumps({'image': jpg_as_text})
    client.publish(topic, payload)
    # cv2.imshow('Frame', result_image)

    # 영상 출력 중 q가 입력되면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # videoCapture 객체해제
cv2.destroyAllWindows()  # 창 닫기
client.disconnect()  # 연결 해제