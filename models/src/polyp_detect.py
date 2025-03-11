#!/usr/bin/env python3

import argparse
import cv2
import torch
import os
import numpy as np
import math  # Import math for rounding confidence values

from ultralytics import YOLO

# Load YOLO model
model = YOLO("best.pt")

# Test inference on a dummy image
dummy_frame = cv2.imread('dummy.png')
if dummy_frame is not None:
    model(dummy_frame)

def infer(file):
    img = cv2.imread(file)
    if img is None:
        print(f"Error: Unable to read image {file}")
        return
    
    img_name = os.path.splitext(file)[0]
    
    # Run YOLO inference
    results = model(img, verbose=False)
    
    # Process the results
    for result in results:
        boxes = result.boxes
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Convert tensor to list
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Extract confidence score
            conf = round(float(box.conf[0]) * 100) / 100
            print(f"Confidence: {conf}")

    # Save output image
    output_path = f"{img_name}_res.jpg"
    cv2.imwrite(output_path, img)
    print(f"Processed image saved as {output_path}")

# Ensure directory exists
image_dir = 'imgs/'
if not os.path.exists(image_dir):
    print(f"Error: Directory '{image_dir}' does not exist.")
else:
    # Loop through images in directory
    for file in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file)
        if os.path.isfile(file_path):
            infer(file_path)

