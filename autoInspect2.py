import cv2
import numpy as np
from anomalib.deploy import OpenVINOInferencer
from pathlib import Path
from PIL import Image, ImageTk, ImageFilter
from anomalib.visualization import ImageVisualizer
import json
import cv2
import customtkinter as ctk
import os
from tkinter import filedialog
from datetime import datetime
import time
import csv
import threading


class AutoInspector2:
    def __init__(self, openvino_model_path2, file_config, is_scanning, img_format):
        super().__init__()
        self.openvino_model_path2 = openvino_model_path2
        self.file_config = file_config
        self.img_format = img_format
        #self.processed_log = self.file_config["enviados_log"]
        self.score_limit2 = float(self.file_config["scorelimit2"])
        self.is_scanning_online = is_scanning
        '''if os.path.exists(self.processed_log):
            with open(self.processed_log, "r") as f:
                self.processed_folders = set(line.strip() for line in f if line.strip())
        else:
            self.processed_folders = set()'''


    
    def analyzePic2(self, image_paths):
        #isn = image_paths.split("\\")
        #ISNn = isn[-1:]
        #isnFinal = ISNn[0]
        #print("ISN Final", isnFinal)
        try:

            image = Image.open(image_paths)
        
            if self.img_format != "JPEG":
                print("imagen tiff convirtiendo a jpeg")
                img_np = np.array(image, dtype=np.float32)
                img_np = img_np / 255.0
                img_np = np.clip(img_np, 0.0, 1.0)
                img_np = (img_np * 255).astype(np.uint8)
                image = Image.fromarray(img_np, mode = "RGB")
                image = image.filter(ImageFilter.GaussianBlur(radius=0.6))   
            #x1,y1,x2,y2
            box = (1116, 2305, 1683, 2739)
            print("snipping screw 2")
            image_snip = image.crop(box)
            im_res = image_snip.resize((256, 256))

            #hacer inferencia
            inferencer = OpenVINOInferencer(
                path=self.openvino_model_path2,
                device="CPU",
            )
            #obtener predicciones
            predictions= inferencer.predict(image=im_res)
            #print("predictions", predictions)
            scoreArr = predictions.pred_score[0]
            self.score2 = f"{(scoreArr[0]*100):.2f}"
            scorefloa = float(self.score2)
            print("prediction screw 2", self.score2)

            #Guardar solo imagen de anomalia
            vizualizer2 = ImageVisualizer(
                fields=[""],
                overlay_fields=[("image",["anomaly_map"])],
                text_config={"size":14},

            )
            output_anomalyimg = vizualizer2.visualize(predictions)
            output_anomalyimg.save("output_anomaly2.png")

            #Visualizar todas los modos de la inferencia 
            visualizer = ImageVisualizer(text_config={"size":16})
            self.output_image2 = visualizer.visualize(predictions)
            self.output_image2.save("output2.png")

            #Recorte con OpenCV [y1:y2, x1:x2]
            imroi = cv2.imread("output_anomaly2.png")
            self.roii2 = cv2.cvtColor(imroi, cv2.COLOR_BGR2RGB)

            #Analisis con openCV en el ROI 
            mean_color = cv2.mean(self.roii2)[:3]
            r_mean, g_mean, b_mean = mean_color
            #print(f"Promedio BGR: {mean_color}")

            #if b_mean < 210 and r_mean > 150 and g_mean > 230:
            if scorefloa > self.score_limit2:
                self.result2 = "NG"
            else:
                self.result2 = "OK"
        except Exception as e:
            print("Error doing inference in screw 2", e)
            return None, None, "ERROR"
        
        return   self.output_image2, self.roii2, self.score2, self.result2
    

    '''def get_subfolder(self, path):
        subfolders = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path,f))]
        if not subfolders:
            return None
        return max(subfolders, key=os.path.getmtime)

    def getPath(self, folder_path):
        correlation = self.file_config["Image_correlation1"] 
        correlation2 = self.file_config["Image_correlation2"] 

        if not os.path.isdir(folder_path):
            print("Ruta de imagenes no es valida")
            return
        
        self.processed_folders = set()
        while self.is_scanning_online:
            print("Buscando nuevas carpetas en", folder_path)
            time.sleep(2)
            day_folder = self.get_subfolder(folder_path)
            if not day_folder:
                continue
            for isn in os.listdir(day_folder):
                isn_path = os.path.join(day_folder, isn)
                print("ISN PATH", isn_path)
                if not os.path.isdir(isn_path) or isn in self.processed_folders:
                    continue
                try:
                    image_folder = os.path.join(isn_path, "Cam1")
                    creation_time = datetime.fromtimestamp(os.path.getctime(isn_path))
                except Exception as e:
                    print("Creation time cannot be readed", creation_time)
                    continue
                if creation_time > self.start_time:
                    print("Nueva carpeta detectada, esperando termine el proceso de AOI")
                    time.sleep(35)
                    try:
                        print("Este es el thread 2")
                        is_ok = isn_path+"_PASS"
                        splits = isn.split("_")
                        ISNs1= splits[0]
                        ISNs2= splits[1]
                        ISNs = f"{ISNs1}_{ISNs2}"
                        print("ISNs", ISNs)
                        img_path = os.path.join(is_ok,"Cam1",correlation)
                        img_path2 = os.path.join(is_ok,"Cam1",correlation2)
                        print("img path", img_path)
                        print("img path2", img_path2)
                        print(f"Nuevo ISN detectado {isn}")
                        self.output_image2, self.roii2, self.score2, self.result2 = self.analyzePic2(img_path)
                        self.processed_folders.add(isn)
                        print("processed with screw 2", self.processed_folders)

                    except Exception as e:
                        print(f"Error obtaining the picture for screw 2{ISNs}")
                        self.processed_folders.add(isn)
                        self.is_scanning_online = True
        
                    return  self.output_image2, self.roii2, self.score2, self.result2'''
                    


