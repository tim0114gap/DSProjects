from django.db import models
import numpy as np
import keras,sys
import tensorflow as tf
from keras.models import load_model
from PIL import Image
import io,base64
from keras.models import load_model, model_from_json
from datetime import datetime

graph = tf.get_default_graph()

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(null = True, upload_to='cnn_coin')

    IMAGE_SIZE = 224
    MODEL_PATH = "./ml_models/DSProject_mizumashi2_model.json"
    MODEL_PATH_WEIGHTS = "./ml_models/DSProject_mizumashi2_model_weights.h5"
    imagename = ['rupee_2', 'rupee_10', 'rupee_1', 'rupee_5']
    numlst = [2, 10, 1, 5]
    image_len =len(imagename)

    def predict(self):
        model=None
        global graph#毎回同じモデルのセッションに投入して推論可能にする。
        with graph.as_default():
            model = model_from_json(open(self.MODEL_PATH).read())
            model.load_weights(self.MODEL_PATH_WEIGHTS)

            img_data = self.image.read()
            img_bin = io.BytesIO(img_data)

            img = Image.open(img_bin)
            img = img.resize((self.IMAGE_SIZE, self.IMAGE_SIZE))
            img = img.convert('RGB')
            data = np.asarray(img)

            # scaling
            data = data / 255

            # to 4dim
            data = data[None, ...]

            features = model.predict(data)

            feature = [round(features[0][0], 3), round(features[0][1], 3), round(features[0][2], 3), round(features[0][3], 3)]
            maxNum = 0
            num = 0
            for i in range(len(feature)):
                if maxNum < feature[i]:
                    maxNum = feature[i]
                    num = i
            maxNum = round(maxNum*100,2)

            time = datetime.now()
            
            # rate = round(self.numlst[num] * 16.37, 2)
            # result = str(self.numlst[num])+" rupee = "+ str(rate)+" won"
            rupee = self.numlst[num]
            won = round(self.numlst[num] * 16.37, 2)

            return self.imagename[num], maxNum, time, rupee, won

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()

            return "data:"+img.file.content_type+":base64"+base64_img