# video recorder  

openCV를 이용한 동영상 저장 프로그램

### 기능 설명
- 카메라 열기(기본 카메라)
  ```python
  video = cv.VideoCapture(0) # 기본 카메라 열기
  ```
  - 실행 환경에서는 맥북과 연결된 아이폰의 후면카메라와 연결.
- 동영상 녹화/녹화 종료  
  - space bar 버튼을 누를 경우 녹화/녹화종료
    ```python
    elif key == 32: # space bar키를 누르면 녹화/녹화종료
            if isRecord:
                isRecord = False
                target.release()
            else:
                isRecord = True
                h, w, *_ = img.shape
                is_color = (img.ndim > 2) and (img.shape[2] > 1)
                target.open('myvideo.mp4',cv.VideoWriter_fourcc(*'H264'), fps, (w,h), is_color)
    ```
  - 녹화 시 Recording... 문자열을 화면 상 좌측 상단에 표시
    ```python
    if isRecord: # 영상 저장 및 Recording 표시
            target.write(img)
            cv.putText(img, 'Recording...', (10, 50), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255), 2)
    ```  
  - <img width="500" alt="스크린샷 2025-03-13 오후 12 36 58" src="https://github.com/user-attachments/assets/c3a0d938-024b-476a-aafa-3c5480591671" />

- 카메라 종료  
  esc 버튼을 누를 경우 카메라 종료

#### 추가 기능 설명
- 색상 반전/해제  
  - c 버튼을 누를 경우 색상 반전/해제
    ```python
    if isContrast: # negative image로 전환
            img = 255 - img
    ...
    ...
    elif key == 99: # c키를 누르면 negative image로 전환.
            isContrast = not isContrast
    ```
  - <img width="500" alt="스크린샷 2025-03-13 오후 12 29 44" src="https://github.com/user-attachments/assets/3921ccc2-8eae-41d7-b9ca-801d5fbc5c0a" />
  - <img width="500" alt="스크린샷 2025-03-13 오후 12 30 15" src="https://github.com/user-attachments/assets/65ba72e6-e32e-4e79-9fc4-d3be7f3ee006" />

- 코덱 설정 변경  
  - H264로 변경, mp4확장자로 동영상 파일 저장
    ```python
    target.open('myvideo.mp4',cv.VideoWriter_fourcc(*'H264'), fps, (w,h), is_color)
    ```
