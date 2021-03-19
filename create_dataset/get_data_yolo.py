# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 01:06:02 2021

@author: Isaac
"""


import cv2 
import numpy as np
from skimage import morphology
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 
import os

class ProcesarVideo():
    
    image=[]
    image_1=[]
    
    def __init__(self, filename):
        self.filename = filename
        
    def start_video(self):
        vidcap = cv2.VideoCapture(self.filename)
        success,image = vidcap.read()
        newImage = image.copy()
        model = load_model('model-280-0.989506-0.981818-0.064893.h5')
        kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)) 
        bg2 = cv2.createBackgroundSubtractorMOG2(history = 5000000, 
                                                 varThreshold =72, 
                                                 detectShadows = False) 
        frame_width = int(vidcap.get(3))
        frame_height = int(vidcap.get(4))
        name = self.filename.split('.')
        frame_length=int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps=vidcap.get(cv2.CAP_PROP_FPS)
        print(fps)
        count=0
        countEspermas = CountSpermas()
        
        
        while (count!=frame_length):
            sperms_coords = []
            sperms_coords_filter = []
            success, image = vidcap.read()
            if image is not None:
                newImage = image.copy()
            else:
                image=image
            count += 1
            
            gray_image = cv2.cvtColor(newImage,  cv2.COLOR_RGB2GRAY)
            mask = bg2.apply(gray_image)
            arr = mask > 0
            cleaned = morphology.remove_small_objects(arr, min_size=15)
            mask_cleaned = morphology.remove_small_holes(cleaned, min_size=15)
            indices = mask_cleaned.astype(np.uint8)  
            indices*=255
            output = cv2.morphologyEx(indices, cv2.MORPH_OPEN, kernel)
            
            
            countEspermas.find_contornos(output, newImage, count, 
                                         newImage, sperms_coords,
                                         sperms_coords_filter, model)
            
            th = 30
            if count>th:
                
                for each_sperm_coords in sperms_coords:
                    
                    image_detection = OperacionesSpermas.image_detection(image, 
                                                                     each_sperm_coords)
                
                    OperacionesSpermas.sperm_evaluation(image_detection, model, 
                                                        each_sperm_coords, 
                                                        sperms_coords_filter)
    
            
            if not os.path.exists('Database'):
                os.makedirs('Database')
            
            path = 'Database'
            
            
            if len(sperms_coords_filter)>1 and count> th:   
                cv2.imwrite(os.path.join(path , name[0]+'_Frame_' + 
                                         str(count)+'.jpg'), image)
                
                txt_name = name[0]+'_Frame_' + str(count)+'.txt'
                file_txt = open("Database/" + txt_name, "w")
                for coords in sperms_coords_filter:
                    class_line_txt='0 '
                    file_txt.write(class_line_txt)

                    
                    x_c = coords[0]/frame_width
                    y_c = coords[1]/frame_height
                    
                    x_n = (((coords[0]+10) - (coords[0]-10))/2)/frame_width
                    y_n = (((coords[1]+10) - (coords[1]-10))/2)/frame_height
                    info_coords = "%f %f %f %f" % (round(x_c, 6), round(y_c,6),
                                                   round(x_n, 6), round(y_n,6))
                    file_txt.write(info_coords)
                    next_txtline="\n"
                    file_txt.write(next_txtline)
                    
                    # DRAW BOUNDING
                    #cv2.rectangle(newImage, (coords[0]-10, coords[1]-10),
                    #              (coords[0]+10, coords[1]+10), (255,0,0), 2)
                    #cv2.imwrite(os.path.join(path , name[0]+'_Frame_' +
                    #                     str(count)+ '_seed' +'.jpg'), newImage)
                
                file_txt.close()    
    

            # VISUALIZE DETECTION
            #cv2.imshow("Imagen", newImage)
            
            
                   
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        vidcap.release()
        cv2.destroyAllWindows()

class CountSpermas():
    
    
    def __init__(self):
        self.vector = []
        self.pos_frames =[]
        self.v_actual=[]
        self.v_anterior=[]
        
    
           
    def find_contornos(self, th3ot, image2, count, image_o, sperms_coords,
                       sperms_coords_filter, model):
        
        contours, hierarchy = cv2.findContours(th3ot,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        contours_1=[]
        for i in contours:
            area = cv2.contourArea(i)
            if area>2 and area<200:
                contours_1.append(i)     
        self.v_anterior = self.v_actual
        self.v_actual.clear()
        for c in contours_1:

            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
            x=cx
            y=cy
            
            if x> 10 and x < 630 and y> 10 and y < 470: 
                
                x_sperm = x
                y_sperm = y
                sperms_coords.append([x_sperm,y_sperm])
            
            else:
                
                continue
    
   
            
class OperacionesSpermas():
    

    @classmethod
    def image_detection(cls,image_original, SpermCoords):
        n=SpermCoords
        sperm_morpho=image_original[n[1]-10:n[1]+10,n[0]-10:n[0]+10]
        if sperm_morpho.shape[1] > 0 and sperm_morpho.shape[0] > 0:
            sperm_resize = cv2.resize(sperm_morpho, (32,32), interpolation = cv2.INTER_AREA)
                    
        else:
            sperm_resize = np. zeros(shape=[32, 32, 3], dtype=np. uint8)
        return sperm_resize
    

       
    

    @classmethod
    def sperm_evaluation(cls, detect_image, model, coords_sperm, 
                         lista_evaluacion_sperm):
  
        x=image.img_to_array(detect_image)
        x=x/255
        x=np.expand_dims(x,axis=0)

        imagea=np.vstack([x])
        classes = model.predict(imagea)
        if classes[0]>0.5:
            lista_evaluacion_sperm.append(coords_sperm)
        
        