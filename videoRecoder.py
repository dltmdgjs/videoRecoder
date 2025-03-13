import cv2 as cv

video = cv.VideoCapture(0) # 기본 카메라 열기

if video.isOpened():
    target = cv.VideoWriter()

    fps = int(video.get(cv.CAP_PROP_FPS))

    isRecord = False
    isContrast = False

    while True:
        valid, img = video.read()
        if not valid:
            break

        if isContrast: # negative image로 전환
            img = 255 - img

        if isRecord: # 영상 저장 및 Recording 표시
            target.write(img)
            cv.putText(img, 'Recording...', (10, 50), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255), 2)
            
        cv.imshow('Video Player', img)
        
        key = cv.waitKey(1)
        if key == 27: # esc키를 누르면 종료
            break
        elif key == 32: # space bar키를 누르면 녹화/녹화종료
            if isRecord:
                isRecord = False
                target.release()
            else:
                isRecord = True
                h, w, *_ = img.shape
                is_color = (img.ndim > 2) and (img.shape[2] > 1)
                target.open('myvideo.mp4',cv.VideoWriter_fourcc(*'H264'), fps, (w,h), is_color)
        elif key == 99: # c키를 누르면 negative image로 전환.
            isContrast = not isContrast
            
    cv.destroyAllWindows()