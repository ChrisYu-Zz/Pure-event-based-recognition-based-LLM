import json
import os
import re
import time
from collections import defaultdict

import openai



q00 = "Category Name: '0', '1', '2', '3','4','5','6','7','8','9'."

q0 = "Event cameras are specialized sensors that detect pixel-level brightness changes asynchronously, capturing only those changes rather than full frames. The events are accumulated over a specific time window to create an image, which represents the intensity of changes during that period."

q1 = "I will provide several reconstructed images generated from event camera data. These images capture pixel-level brightness changes over time, so they may appear noisy. Your task is to accurately categorize each image based on the categories listed."

q11 = "Each image is composed of 30 small images arranged in 5*6 groups. These 30 small images all belong to the same category, so please provide a category for each 30-in-1 image."
q2 = "Each image must be classified into one of the above categories. Make sure to match the image with the most relevant category from the list."

q3 = "Treat each image independently. After you classify one image, clear your memory of it before moving to the next. Your response should only include the image name and its corresponding category."

q6 = "Please return the results in dictionary format, where each key is the original image name and the value is the identified category. Do not modify the image names or provide any additional information."

q7 = "I will provide the image name followed by the image itself. Your task is to pair the image with the correct category and return the result as a dictionary entry. No additional information is needed."
q= q00+q0+q1+q11+q2+q3+q6+q7
openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxx"
openai.api_base = "xxxxxxxxxxxxxxxxxxx"

image_count=1

file_path = 'E2HQV-MNIST-t2o-groundtruth.txt'

category_images = defaultdict(list)
category_number = {}
with open(file_path, 'r') as file:
    for line in file:
        image_data = json.loads(line.strip())
        for image_name, category in image_data.items():
            category_images[category].append(image_name)
            category_number[category] = 0

category_counts = {category: len(images) for category, images in category_images.items()}
#
#
file_type = "E2HQV-MNIST-t2o-327"

for image_folder in os.listdir("E2HQV-MNIST-t2o-327"):
    images_file="E2HQV-MNIST-t2o-327/"+image_folder
    images_list=[]
    messages = [{"role": "user", "content": [
        {"type": "text", "text": q}
    ]}]
    for image in os.listdir(images_file):
        images_list.append(image)
    for i in range(len(images_list)):
        messages[0]["content"].append(
            {"type":"text","text":images_list[i]}
        )
        messages[0]["content"].append(
            {"type": "image_url", "image_url": {
                "url": f"https://env-00jxh60u5ok0.normal.cloudstatic.cn/eventgpt/E2HQV-MNIST-t2o-327/{images_list[i]}"}}
        )

    while True:
        try:
            result = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=messages
            )
            answer = result['choices'][0]['message']['content']
            print(answer)
            print("--------------------------------------------------------------------------")
            # print(len(eval(answer)))
            with open('Result-4t-'+file_type+'.txt', 'a', encoding='utf-8') as file:
                file.write(answer + '\n')
            break
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            time.sleep(2)


cate_list = {}
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
with open('Result-4t-'+file_type+'.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    matches = pattern.findall(content)
    for key, value in matches:
        cate_list[key] = value

groundtruth_dict={}
with open("E2HQV-MNIST-t2o-groundtruth.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            entry = eval(line)
            groundtruth_dict.update(entry)

sum = 0
for key in cate_list:
    if key in groundtruth_dict:
        if cate_list[key] == groundtruth_dict[key]:
            category_number[cate_list[key]]+=1
            sum+=1
        elif groundtruth_dict[key]=="BACKGROUND_Google" and cate_list[key]=="others":
            category_number[groundtruth_dict[key]]+=1
            sum+=1
print(f"Accuracy is {sum/len(cate_list)*100:.2f}%")

for category, count in category_counts.items():
    print(f"Category: {category}, Number of Images: {count},Number of identified:{category_number[category]},Percentage is {category_number[category]/count*100:.2f}")
