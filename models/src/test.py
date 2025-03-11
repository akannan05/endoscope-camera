#!/usr/bin/env python3

import os 
import time 

import onnx
import onnxruntime as ort 

import numpy as np
import cv2
import torch

onnx_model_path = "best.onnx"
session = ort.InferenceSession(onnx_model_path)

imgs_dir = 'imgs'

img_files = [f for f in os.listdir(imgs_dir) if f.lower().endswith(('.jpg'))]

def preprocess(img):
    img_resized = cv2.resize(img, (640, 640))

    img_normal = img_resized/255.0
    img_transpose = np.transpose(img_normal, (2,0,1))
    img_tensor = np.expand_dims(img_transpose, axis=0).astype(np.float32)

    return img_tensor

def postprocess(outputs, img_shape):
    pred = outputs[0]

    boxes = pred[..., :4]
    scores = pred[..., 4]

    boxes = boxes * np.array([img_shape[1], img_shape[0], img_shape[1], img_shape[0]])

    boxes[:, 2] += boxes[:, 0]
    boxes[:, 3] += boxes[:, 1]
    
    return boxes, scores

for img_file in img_files:
    img_path = os.path.join(imgs_dir, img_file)

    img = cv2.imread(img_path)

    start_time = time.time()

    preprocess_start = time.time()
    img_tensor = preprocess(img)
    preprocess_end = time.time()

    infer_start = time.time()
    input_name = session.get_inputs()[0].name
    result = session.run(None, {input_name: img_tensor})
    infer_end = time.time()

    postprocess_start = time.time()
    boxes, scores = postprocess(result, img.shape)
    postprocess_end = time.time()

    for box, score in zip(boxes, scores):
        print(box.shape)
        print(box)
        x1, y1, x2, y2 = box.astype(int)
        color = (0, 0, 255)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        
    output_path = os.path.join("output", img_file)
    cv2.imwrite(output_path, img)

    preprocessing_time_ms = (preprocess_end - preprocess_start)*1000
    inference_time_ms = (infer_end - infer_start)*1000
    postprocessing_time_ms = (postprocess_end - postprocess_start)*1000
    total_time_ms = (time.time() - start_time)*1000

    print(f'Image: {img_file}')
    print(f'Inference: {inference_time_ms:.2f} ms')
    print(f'total: {total_time_ms:.2f} ms')
