import cv2
import numpy as np

import os

import matplotlib.pyplot as plt

def simulate_nbi(image):
    r_channel, g_channel, b_channel = cv2.split(image)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    g_channel_enhanced = clahe.apply(g_channel)
    b_channel_enhanced = clahe.apply(b_channel)

    # Reduce the Red channel's contribution
    r_channel_reduced = cv2.addWeighted(r_channel, 0.3, np.zeros_like(r_channel), 0.0, 0)

    # Merge enhanced channels back into an image
    nbi_image = cv2.merge([r_channel_reduced, g_channel_enhanced, b_channel_enhanced])

    return nbi_image

# directories 
input_dir = "val"
output_dir = "val2"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):  # Process only .jpg files
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Read the input image
        image = cv2.imread(input_path)
        if image is None:
            print(f"Failed to load image: {filename}")
            continue

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Apply the NBI simulation
        nbi_image = simulate_nbi(image_rgb)

        # Convert back to BGR for saving
        nbi_image_bgr = cv2.cvtColor(nbi_image, cv2.COLOR_RGB2BGR)

        # Save the output image
        cv2.imwrite(output_path, nbi_image_bgr)

print("Batch processing complete!")

