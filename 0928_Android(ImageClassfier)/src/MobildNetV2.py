import tensorflow as tf

# 사전 훈련된 모델 가져오기
mobilenet_imagenet_model = tf.keras.applications.MobileNetV2(weights="imagenet")

# TFLite 모델로 변환
converter = tf.lite.TFLiteConverter.from_keras_model(
    mobilenet_imagenet_model)

tflite_model = converter.convert()

# 파일로 저장
with open('./mobilenet_imagemet_model.tflite', 'wb') as f:
    f.write(tflite_model)