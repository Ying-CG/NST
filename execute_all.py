import os
import random
import subprocess

# Paths
content_dir = './data/content-images'
style_dir = './data/style-images'

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.webp')

# Get list of content and style images
content_images = [f for f in os.listdir(content_dir) if f.lower().endswith(image_extensions)]
style_images = [f for f in os.listdir(style_dir) if f.lower().endswith(image_extensions)]

# Loop through content images
for content_img in content_images:
    # Pick a random style image
    style_choices = random.sample(style_images, 1)

    for style_img in style_choices:
        command = [
            'python', 'neural_style_transfer.py',
            '--content_img_name', content_img,
            '--style_img_name', style_img
        ]
        print(f"Running NST with content: {content_img} and style: {style_img}")
        subprocess.run(command)
