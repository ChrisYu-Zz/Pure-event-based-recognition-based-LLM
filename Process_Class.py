import json

file_path = './CLIP-IN_ClassNames.txt'

class_dict = {}

with open(file_path, 'r') as file:
    for line in file:
        key, value = line.strip().split(' ', 1)
        class_dict[key] = value

print(class_dict)

file_path = 'Gray-ImageNet-f2o-100-class.txt'

image_dict = {}

with open(file_path, 'r') as file:
    for line in file:
        entry = json.loads(line.strip())
        image_dict.update(entry)

print(image_dict)

image_class={}

for image in image_dict:

    image_class[image] = class_dict[image_dict[image]]
print(image_class)

output_file_path = 'Gray-ImageNet-f2o-100-groundtruth.txt'

with open(output_file_path, 'w') as outfile:
    for key, value in image_class.items():
        formatted_entry = json.dumps({key: value})
        outfile.write(formatted_entry + '\n')

print(f"image_class has been saved to {output_file_path}")