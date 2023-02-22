"""
-This module saves images and log file. 
-Images are saved in a folder-> DataCollected 
-Folder should be created manually with the name "DataCollected"
-The name of the image and the steering angle is logged in the log file. 
-Call the saveData function to start
-Call the saveLog fuction to end
If runs independent, will save ten images as a demo 
"""

import pandas as pd #data science/data analysis and machine learning tasks.
import os #creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
from datetime import datetime #dealing with date and time data
import cv2 

#variables
global imgList, steeringList
countFolder = 0
count = 0 
imgList = []
steeringList = []

#get current directory path 
myDirectory = os.path.join(os.getcwd(),'DataCollected')
#print(myDirectory)

#get the number of folders that are inside of DataCollected folders 
#newFolder=newFolder+1
#create a new folder based on the previous folder count 
while os.path.exists(os.path.join(myDirectory,f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG"+str(countFolder)
os.makedirs(newPath)


#save images in the specific folder (current folder that will be created)
def saveData(img,steering):#angle->steering 
    #absolute nickname, unic name 
    global imgList, steeringList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace('.','')
    print("timestamp= ",timestamp)
    fileName = os.path.join(newPath,f'Image_{timestamp}.jpg')
    #save the fileName and img
    cv2.imwrite(fileName,img)
    imgList.append(fileName)#store the filename in an array , the name of the img. 
    steeringList.append(steering)#store the path + the steering angle value 

#save log file when the session ends 
#transfer all the data into the csv file 
def saveLog(): 
    global imgList, steeringList
    rawData = {'Image':imgList,
               'Steering':steeringList}
    #form the list to a csv file 
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory,f'log_{str(countFolder)}.csv'),index=False,header=False)
    print('log saved')
    print('Total images: ',len(imgList))

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    #just for testing 
    for x in range (10):
        _, img = cap.read()
        saveData(img,0.5)#image and angle 
        cv2.waitKey(1)
        cv2.imshow("Image",img)
    saveLog()#ends the session 

