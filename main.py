# Libraries
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math

# Scanning Function
def Scanning():
# Read VideoCapture
    if cap is not None:
        ret, frame = cap.read()
        frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if ret == True:

            results = model(frame, stream=True, verbose=False)

            for res in results:
            # Box
                boxes = res.boxes
                for box in boxes:
                    # Bounding Box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    # Error
                    if x1 < 0: x1 = 0
                    if y1 < 0: y1 = 0
                    if x2 < 0: x2 = 0
                    if y2 < 0: y2 = 0

                    # Clase
                    cls = int(box.cls[0])
                    # Confidence
                    conf = math.ceil(box.conf[0])
                    if conf > 0.5:
                        if cls == 0:
                        # Draw Rectamgle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                        # Text
                            text = f'{clsName[cls]} {int(conf) * 100} %'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rect
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

                        if cls == 1:
                        # Draw Rectamgle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 0, 0), 2)
                        # Text
                            text = f'{clsName[cls]} {int(conf) * 100} %'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rect
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

                        if cls == 2:
                        # Draw Rectamgle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                        # Text
                            text = f'{clsName[cls]} {int(conf) * 100} %'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rect
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            # Resize
            frame_show = imutils. resize(frame_show, width=640)

            # Convertir Video
            im = Image.fromarray(frame_show)
            img = ImageTk.PhotoImage (image=im)

            # Mostrar
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, Scanning)

        else:
            cap.release()
# main
def ventana_principal():
    global model, clsName, img_metal, img_glass, img_plastic, img_carton, img_medical, lblVideo
    global img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medicaltxt, cap
    # Ventana principal
    pantalla = Tk()
    pantalla.title("RECICLAJE INTELIGENTE")
    pantalla.geometry("1280x720")

    # Background
    imagenF = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagenF)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Model
    model = YOLO('Modelos/best.pt')

    # Clases
    clsName = ['Metal', 'Glass', 'Plastic', 'Carton', 'Medical']

    # Img
    #img_metal = cv2.imread("setUp/metal.png")
    #img_glass = cv2.imread("setUp/vidrio.png")
    #img_plastic = cv2.imread("setUp/plastico. png")
    #img_carton = cv2.imread("setUp/carton.png")
    #img_medical = cv2.imread("setUp/medical.png")
    #img_metaltxt = cv2.imread("setUp/metaltxt.png")
    #img_glasstxt = cv2.imread("setUp/vidriotxt.png")
    #img_plastictxt = cv2.imread("setUp/plasticotxt.png")
    #img_cartontxt = cv2.imread("setUp/cartontxt.png")
    #img_medicaltxt = cv2.imread("setUp/medicaltxt.png")

    # Label Video
    lblVideo = Label(pantalla)
    lblVideo.place(x=130, y=130)
    # Cam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 834)
    cap.set(4, 564)
    # Scanning
    Scanning()

    # Loop
    pantalla.mainloop()


if __name__ == '__main__':
    ventana_principal()
