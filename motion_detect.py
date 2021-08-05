import cv2
class Motion():
    def __init__(self):
        pass
    def detect_motion(self,cap):
        _,frame1=cap.read()
        _,frame2=cap.read()
        diff=cv2.absdiff(frame1,frame2)
        imggray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        _,img_thres=cv2.threshold(imggray,50,255,cv2.THRESH_BINARY)
        imgdil=cv2.dilate(img_thres,None,iterations=2)
        contours,hierarchy=cv2.findContours(imgdil,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area=cv2.contourArea(cnt)
            if abs(area)>5000:
                perimeter=cv2.arcLength(cnt,True)
                approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("img",frame2)
def main():
    motion=Motion()
    vid=cv2.VideoCapture(0)
    while True:
        motion.detect_motion(vid)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
if __name__=="__main__":
    main()