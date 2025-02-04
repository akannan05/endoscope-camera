import argparse
import cv2
import torch
import os

from ultralytics import YOLO

def load_model(model_path):
    model = YOLO(model_path)
    return model

def detect_objects(model, img_path):
    img = cv2.imread(img_path)
    results = model(img)
    return results

def save_output(results, output_path, img):
    for detection in results:
        boxes = detection.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite(output_path, img)


def main():
    parser = argparse.ArgumentParser(description="Polyp Detect CLI")
    parser.add_argument("image_path", type=str, help="path to input image")
    args = parser.parse_args()

    model_path = "best.pt"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"check the model path, path not found: {model_path}")
    model = load_model(model_path)

    img = cv2.imread(args.image_path)
    if img is None:
        raise FileNotFoundError(f"check the image path, path not found: {image_path}")
    results = detect_objects(model, args.image_path)

    output_image_name = "output_image_result.jpg"
    output_image_path = os.path.join(os.getcwd(), output_image_name)
    save_output(results, output_image_path, img)

    print(f"Successfully ran model, output saved at: {output_image_path}")

if __name__ == "__main__":
    main()
