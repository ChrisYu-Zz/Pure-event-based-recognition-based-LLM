import os
import random
import re
import shutil
import uuid


folders = {
    'E2HQV': {
        'src': 'E2HQV-ImageNet-f2o',
        'dst': 'E2HQV-ImageNet-f2o-100',
        'mapping_file': 'E2HQV-ImageNet-f2o-100-class.txt'
    },
    'E2VID': {
        'src': 'E2VID-ImageNet-f2o',
        'dst': 'E2VID-ImageNet-f2o-100',
        'mapping_file': 'E2VID-ImageNet-f2o-100-class.txt'
    },
    'Gray': {
        'src': 'Gray-ImageNet-f2o',
        'dst': 'Gray-ImageNet-f2o-100',
        'mapping_file': 'Gray-ImageNet-f2o-100-class.txt'
    }
}


images_E2HQV = [img for img in os.listdir(folders['E2HQV']['src']) if img.endswith('.png')]

name_mapping = {}


for img in selected_images:
    match = re.match(r'^([a-zA-Z0-9]+)-\d+', img)
    original_prefix = match.group(1)
    # original_prefix = img.split('-')[0]
    random_name = f"{uuid.uuid4().hex}.png"
    name_mapping[img] = random_name


for key, folder in folders.items():

    if not os.path.exists(folder['dst']):
        os.makedirs(folder['dst'])


    for img in selected_images:
        random_name = name_mapping[img]
        shutil.copy(os.path.join(folder['src'], img), os.path.join(folder['dst'], random_name))


    with open(folder['mapping_file'], 'w') as f:
        for original_name, new_name in name_mapping.items():
            f.write(f'{{"{new_name}":"{original_name.split("-")[0]}"}}\n')

    print(f"Name mapping for {key} has been saved to {folder['mapping_file']}")


print("Processing complete.")
