import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.models import model_from_json
from numpy import loadtxt

class myCall(tf.keras.callbacks.Callback) :
    def on_epoch_end(self, epoch, logs={}) :
        if(logs.get('accuracy')>0.995) :
            self.model.stop_training=True
callbacks=myCall()

data_x=loadtxt("Data.txt", delimiter=',')
data_y=loadtxt("Labels1.txt", delimiter='\n')

model= tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(15, input_dim=10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(12, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(9, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(data_x, data_y, epochs=3000, callbacks=[callbacks])

model.summary()

model_json=model.to_json()
with open("model.json", "w") as json_file :
    json_file.write(model_json)
model.save_weights("model.h5")
