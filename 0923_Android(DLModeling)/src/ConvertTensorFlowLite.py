import tensorflow as tf


converter = tf.lite.TFLiteConverter.from_keras_model(mlp_model)
tflite_model = converter.convert()

with open('./keras_model.tflite', 'wb') as f:
    f.write(tflite_model)