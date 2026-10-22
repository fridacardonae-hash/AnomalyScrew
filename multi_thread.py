import os 
import threading
from autoInspect import AutoInspector
from autoInspect2 import AutoInspector2
from autoInspect3 import AutoInspector3


class Thread_handler:
    def __init__(self, starter):
        self.starter = starter

        self.done1 = threading.Event()
        self.done2 = threading.Event()
        self.done3 = threading.Event()

        self.output_image1 = None
        self.output_image2 = None
        self.output_image3 = None

    def Inspection1(self):
        #self.output_image1 = None
        try:
            self.autoinspector = AutoInspector(self.starter.openvino_model_path1, self.starter.file_config, self.starter.is_scanning_online)
            self.output_image1, self.roi1, self.score1, self.result1 = self.autoinspector.analyzePic1(self.img_path)
           
            print("Screw 1 ready")
        except Exception as e:
            print("Error in Inspection 1", e)
        #return self.output_image1, self.roi1, self.score1, self.result1

        finally:
            self.done1.set()
    
    def Inspection2(self):
        #self.output_image2 = None
        try:
            self.autoinspector2 = AutoInspector2(self.starter.openvino_model_path1, self.starter.file_config, self.starter.is_scanning_online)
            self.output_image2, self.roi2, self.score2, self.result2 = self.autoinspector2.analyzePic2(self.img_path)
           
            print("Screw 2 ready")
        except Exception as e:
            print("Error in Inspection 2", e)
        #return self.output_image2, self.roi2, self.score2, self.result2

        finally:
            self.done2.set()

    def Inspection3(self):
        #self.output_image3 = None
        try:
            self.autoinspector3 = AutoInspector3(self.starter.openvino_model_path1, self.starter.file_config, self.starter.is_scanning_online)
            self.output_image3, self.roi3, self.score3, self.result3 = self.autoinspector3.analyzePic3(self.img_path2)
     
            print("Screw 3 ready")

        except Exception as e:
            print("Error in Inspection 3", e)
        finally:
            self.done3.set()

    def thread_trigger(self, im_path, im_path2):

        self.img_path = im_path
        self.img_path2 = im_path2

        self.done1.clear()
        self.done2.clear()
        self.done3.clear()

        t1 = threading.Thread(target=self.Inspection1, daemon=True)
        t2 = threading.Thread(target=self.Inspection2, daemon= True)
        t3 = threading.Thread(target=self.Inspection3, daemon=True)

        t1.start()
        t2.start()
        t3.start()

        self.done1.wait()
        self.done2.wait()
        self.done3.wait()

        print("3 inspecciones terminadas")
  
        return (self.output_image1, self.output_image2, self.output_image3, self.roi1, self.roi2, self.roi3, self.score1, self.score2, self.score3, self.result1, self.result2, self.result3)
        


        