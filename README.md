# event-recognition-based-LLM

### 1. Dataset processing

#### 1. Combined event frame images

____Process the Caltech, ImageNet, and select four frames of each type of event frame image in sequence and merge them into a four-in-one frame image. Change the dataset path as needed.

   `python four2one.py`

For the MNIST dataset, thirty event frame images of each category are selected sequentially for synthesis.

   `python thirty2one.py`

#### 2. Generating Groundtruth

For the Caltech and MNIST datasets, the parent folder name of the event frame image is its classification. We use the following file to directly rename the event frame images of the three modes (E2HQV, E2VID, and grayscale event frames) in the dataset to ensure randomness. At the same time, the name of each event frame image and its corresponding classification are written into a .txt file in the form of a dictionary.

   `python Generate_Groundtruth.py`

For the ImageNet dataset, since the parent folder name of each type of image is its classification number, the following two files are needed to generate the corresponding relationship between the numbers and then generate Groundtruth.

   `python Generate_Groundtruth.py`
   `python Process_Class.py`

#### 3. Event frame image preparation

While testing GPT performance, in order to avoid being affected by the GPT memory library and reduce costs, we will input prompt words and ten synthetic images of event frames into GPT each time, so we use the following files to group the event frame images.

   `python Event_frame_image_preparation.py`

### 2. Test

Test GPT-4o and GPT-4-turbo, perform different tests on event frame images of different modalities of different datasets, generate different test results according to different data modalities and models tested, and save them in different .txt files.

For example, I want to test the recognition effect of GPT-4o in identifying event frame images in the E2HQV modality of the Caltech dataset, which can be tested through the following files.

   `cd ./Caltech/E2HQV`

   `python E2HQV-GPT-4o.py`


