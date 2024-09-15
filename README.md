# event-recognition-based-LLM

### 1. Dataset processing

#### 1) Combined images

Select four frames in sequence from each representation and merge them into a single frame. Change the dataset path as needed.

```python
python four2one.py
```

For the N-MNIST dataset, thirty frames of each category are selected sequentially for synthesis.

```python
python thirty2one.py
```

#### 2) Generating Groundtruth

For the N-Caltech and N-MNlST datasets, the parent folder name represents the category of each frame. We use the following script to directly rename the frames from the three representations to ensure randomness. Simultaneously, the names of the frames and their corresponding categories are recorded in a dictionary format and saved in a `.txt` file for accurate verification in subsequent steps.

```python
python Generate_Groundtruth.py
```

For the ImageNet dataset, since the parent folder name of each type of frame is its classification number, the following two files are needed to generate the corresponding relationship between the numbers and then generate Groundtruth.

```python
python Generate_Groundtruth.py
python Process_Class.py
```

#### 3) Frame preparation

While testing GPT performance, in order to avoid being affected by the GPT memory library and reduce costs, we will input prompt words and ten synthetic images of frames into GPT each time, so we use the following files to group the event frames and reconstructed frames.

```python
python Event_frame_image_preparation.py
```

#### 4) Frame upload

Since ChatGPT's API can only read URL frames when reading files, local frames need to be converted. Here we choose to upload the frame to the storage space of a personal server to obtain its URL.

### 2. Test

Test GPT-4o and GPT-4turbo by performing various tests on frames from different representations across multiple datasets. Generate distinct test results based on there presentation and model being tested, and save the results in separate `.txt` files.

```python
cd ./Caltech/E2HQV
python E2HQV-GPT-4o.py
```

