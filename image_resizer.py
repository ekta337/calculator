import os
from PIL import Image

# Input and Output folders
input_folder = "images"
output_folder = "output"

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize size
new_width = 800
new_height = 600

# Loop through all files
for filename in os.listdir(input_folder):
    try:
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            
            with Image.open(img_path) as img:
                resized_img = img.resize((new_width, new_height))
                
                # Convert to PNG format
                new_filename = os.path.splitext(filename)[0] + ".png"
                save_path = os.path.join(output_folder, new_filename)
                
                resized_img.save(save_path, "PNG")
                
                print(f"Resized and saved: {new_filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Task Completed ✅")
