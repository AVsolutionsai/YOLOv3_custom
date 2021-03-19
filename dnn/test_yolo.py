# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:36:11 2021

@author: Isaac
"""

import cv2 

import numpy as np
import time

net = cv2.dnn.readNet("yolov3-tiny_custom_4000.weights","yolov3-tiny_custom.cfg") # Poner los pesos obtenidos del entrenamiento y el .cfg utilizado

classes = []
with open("obj.names","r") as f: #utilizar el obj.names utilizado en yolo 
    classes = [line.strip() for line in f.readlines()]
    
print(classes)

layer_names = net.getLayerNames()
outputlayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

colors= np.random.uniform(0,255,size=(len(classes),3))

#cargar video
cap=cv2.VideoCapture("../data/video/video_name.mp4") #aquí debe de poner el nombre del video
font = cv2.FONT_HERSHEY_PLAIN
starting_time= time.time()
frame_id = 0

while True:
    _,frame= cap.read() # 
    frame_id+=1
    
    height,width,channels = frame.shape
    
    #detección de los objetos
    blob = cv2.dnn.blobFromImage(frame,0.00392,(320,320),(0,0,0),True,crop=False) #reduce 416 a 320    

        
    net.setInput(blob)
    outs = net.forward(outputlayers)



    #Mostrar la información en pantalla del confidence score que obtiene el modelo de cada objeto detectado
    class_ids=[]
    confidences=[]
    boxes=[]
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3: # Aquí puede modificar la detección
                
                #Objeto detectado
                center_x= int(detection[0]*width)
                center_y= int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                #Coordenadas del rectangulo
                x=int(center_x - w/2)
                y=int(center_y - h/2)

                boxes.append([x,y,w,h]) #poner todos los rectangulos
                confidences.append(float(confidence)) #indice de coincidencia relacionado con cada objeto detectado
                class_ids.append(class_id) #nombre del objeto que fue detectado

    indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)


    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence= confidences[i]
            color = colors[class_ids[i]]
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            cv2.putText(frame,label+" "+str(round(confidence,2)),(x,y+30),font,1,(255,255,255),2)
            

    elapsed_time = time.time() - starting_time
    fps=frame_id/elapsed_time
    cv2.putText(frame,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
    
    cv2.imshow("Image",frame)
    key = cv2.waitKey(1) 
    
    if key == 27: #presionar esc para salir del proceso
        break;
    
cap.release()    
cv2.destroyAllWindows()