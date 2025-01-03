import cv2 # OpenCV

# Visão computacional

# Detecção de faces

imagem = cv2.imread('workplace-1245776_1920.jpg')

#cv2.imshow(imagem)
from google.colab.patches import cv2_imshow
cv2_imshow(imagem)

detector_face = cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2_imshow(imagem_cinza)

deteccoes = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.3, minSize=(30,30))

deteccoes

len(deteccoes)

for (x, y, l, a) in deteccoes:
    #print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)
cv2_imshow(imagem)

# Detecção do corpo

image = cv2.imread('/content/pessoas.jpg')
cv2_imshow(image)

detector_corpo = cv2.CascadeClassifier('/content/fullbody.xml')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detections = detector_corpo.detectMultiScale(image_gray, scaleFactor=1.1, minSize=(50,50))
print(len(detections))
print(detections)
for (x, y, l, a) in detections:
    cv2.rectangle(image, (x, y), (x + l, y + a), (0,255,0), 2)
cv2_imshow(image)

# Reconhecimento Facial

#Treinamento

from PIL import Image
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

import zipfile
path = '/content/drive/My Drive/Cursos - recursos/yalefaces.zip'
zip_object = zipfile.ZipFile(file=path, mode='r')
zip_object.extractall('./')
zip_object.close()

import os
os.listdir('/content/yalefaces/treinamento')

def dados_imagem():
    caminhos = [os.path.join('/content/yalefaces/treinamento', f) for f in os.listdir('/content/yalefaces/treinamento')]
    faces = []
    ids = []
    for caminho in caminhos:
        if caminho == '/content/yalefaces/treinamento/.ipynb_checkpoints':
            continue
        imagem = Image.open(caminho).convert('L')
        imagem_np = np.array(imagem, 'uint8')
        id = int(os.path.split(caminho)[1].split('.')[0].replace('subject', ''))
        ids.append(id)
        faces.append(imagem_np)
    return np.array(ids), faces

ids, faces = dados_imagem()

print(ids)

print(faces[0])

lbph = cv2.face.LBPHFaceRecognizer_create()
lbph.train(faces, ids)
lbph.write('classificadorLBPH.yml')

# Classificação

reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('/content/classificadorLBPH.yml')

imagem_teste = '/content/yalefaces/teste/subject10.sad.gif'

imagem = Image.open(imagem_teste).convert('L')
imagem_np = np.array(imagem, 'uint8')
print(imagem_np)

idprevisto, _ = reconhecedor.predict(imagem_np)
idprevisto

idcorreto = int(os.path.split(imagem_teste)[1].split('.')[0].replace('subject', ''))
idcorreto

cv2.putText(imagem_np, 'P: ' + str(idprevisto), (x,y + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
cv2.putText(imagem_np, 'C: ' + str(idcorreto), (x,y + 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
cv2_imshow(imagem_np)







