import cv2
import numpy as np
import Utlis

curveList = []
avgVal = 10

def getLaneCurve(img, display=2):#send a img a return the curve

    imgCopy = img.copy()
    imgResult = img.copy()


    #STEP 1-> thresholding

    imgThres = Utlis.thresholding(img)

    #STEP 2-> warping
    hT,wT,c = img.shape
    points = Utlis.valTrackbars()
    imgWarp = Utlis.warpImg(imgThres,points,wT,hT)
    imgWarpPoints = Utlis.drawPoints(imgCopy,points)
    
    #STEP 3-> AVERAGE
    middlePoint,imgHist = Utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
    curveAveragePoint,imgHist = Utlis.getHistogram(imgWarp,display=True,minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint


    #STEP 4 -> AVERAGING 
    #a smooth transtition 
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))


    #STEP 5 -> DISPLAY 
    if display != 0:
       imgInvWarp = Utlis.warpImg(imgWarp, points, wT, hT,inv = True)
       imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
       imgInvWarp[0:hT//3,0:wT] = 0,0,0
       imgLaneColor = np.zeros_like(img)
       imgLaneColor[:] = 0, 255, 0
       imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
       imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
       midY = 450
       cv2.putText(imgResult,str(curve),(wT//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
       cv2.line(imgResult,(wT//2,midY),(wT//2+(curve*3),midY),(255,0,255),5)
       cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY-25), (wT // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
       for x in range(-30, 30):
           w = wT // 20
           cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
                    (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)
       #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
       #cv2.putText(imgResult, 'FPS '+str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,50,50), 3);
    if display == 2:
        imgStacked = Utlis.stackImages(0.7,([img,imgWarpPoints,imgWarp],
                                            [imgHist,imgLaneColor,imgResult]))
        cv2.imshow('ImageStack',imgStacked)
    elif display == 1:
        cv2.imshow('Result',imgResult)


    #middlePoint,imgHist = Utlis.getHistogram(imgWarp,display=True,minPer=0.5, region=2)

    #cv2.imshow("Thres",imgThres)
    #cv2.imshow("Warp",imgWarp)
    #cv2.imshow("Warp points",imgWarpPoints)
    #cv2.imshow("hitograma",imgHist)

     ##NOMRALIZATION 
    curve = curve/100 
    if curve > 1: 
        curve == 1
    if curve < -1: 
        curve == -1

    return curve;





if __name__ == '__main__': #if this is the main script
    cap = cv2.VideoCapture('vid1.mp4')#read the video / get the image
    initialTrackBarVals = [102,80,20,214]#these values could be changed
    Utlis.initializeTrackbars(initialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0
        success, img = cap.read() #get the fames from the video
        img = cv2.resize(img,(480,240))#resize the output window of the video
        curve = getLaneCurve(img,display=1)#0=real 
        print(curve)
        #cv2.imshow("VideoDemo",img)
        cv2.waitKey(1)