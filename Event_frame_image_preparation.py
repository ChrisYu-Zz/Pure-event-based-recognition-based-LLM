import os
import shutil


def create_subfolders_with_images(src_folder, num_subfolders, images_per_folder):
    all_images = sorted([img for img in os.listdir(src_folder) if img.endswith(('.png', '.jpg', '.jpeg'))])

    if len(all_images) < num_subfolders * images_per_folder:
        raise ValueError("There are not enough pictures to distribute among the subfolders.")

    for i in range(num_subfolders):
        subfolder_name = os.path.join(src_folder, f'subfolder_{i + 1}')
        os.makedirs(subfolder_name, exist_ok=True)

        start_index = i * images_per_folder
        end_index = start_index + images_per_folder
        selected_images = all_images[start_index:end_index]

        for img in selected_images:
            shutil.move(os.path.join(src_folder, img), os.path.join(subfolder_name, img))


src_folder = 'Gray-ImageNet-f2o-2000'
create_subfolders_with_images(src_folder, num_subfolders=200, images_per_folder=10)
