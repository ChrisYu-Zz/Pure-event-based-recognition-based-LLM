import os
import cv2
import numpy as np

def create_collage_from_subfolders(root_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f))]

    for folder in folders:
        folder_path = os.path.join(root_dir, folder)
        images = [img for img in os.listdir(folder_path) if img.endswith('.png')]

        n = 1
        for i in range(0, len(images), 4):
            selected_images = images[i:i+4]

            if len(selected_images) < 4:
                print(f"{folder} There are less than 4 pictures left in the folder, skipping...")
                break

            collage = np.zeros((720, 960, 3), dtype=np.uint8)

            for j, image_name in enumerate(selected_images):
                image_path = os.path.join(folder_path, image_name)
                img = cv2.imread(image_path)
                x = (j % 2) * 480
                y = (j // 2) * 360
                resized_img = cv2.resize(img, (480, 360))
                collage[y:y + 360, x:x + 480] = resized_img

            output_filename = f"{folder}-{n}.png"
            output_filepath = os.path.join(output_dir, output_filename)

            cv2.imwrite(output_filepath, collage)
            print(f"Collage saved as {output_filename}")
            n += 1

root_directory = r'N-ImageNet-grayscale-blackbackground-timewindow'
output_directory = r'Gray-ImageNet-f2o'
create_collage_from_subfolders(root_directory, output_directory)
