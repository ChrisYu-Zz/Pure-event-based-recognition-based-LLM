import json
import os
import re
import time
from collections import defaultdict

import openai

q00="Category Name:'tench', 'goldfish', 'great white shark', 'tiger shark', 'hammerhead shark', 'electric ray', 'stingray', 'rooster', 'hen', 'ostrich', 'brambling', 'goldfinch', 'house finch', 'junco', 'indigo bunting', 'American robin', 'bulbul', 'jay', 'magpie', 'chickadee', 'American dipper', 'kite (bird of prey)', 'bald eagle', 'vulture', 'great grey owl', 'fire salamander', 'smooth newt', 'newt', 'spotted salamander', 'axolotl', 'American bullfrog', 'tree frog', 'tailed frog', 'loggerhead sea turtle', 'leatherback sea turtle', 'mud turtle', 'terrapin', 'box turtle', 'banded gecko', 'green iguana', 'Carolina anole', 'desert grassland whiptail lizard', 'agama', 'frilled-necked lizard', 'alligator lizard', 'Gila monster', 'European green lizard', 'chameleon', 'Komodo dragon', 'Nile crocodile', 'American alligator', 'triceratops', 'worm snake', 'ring-necked snake', 'eastern hog-nosed snake', 'smooth green snake', 'kingsnake', 'garter snake', 'water snake', 'vine snake', 'night snake', 'boa constrictor', 'African rock python', 'Indian cobra', 'green mamba', 'sea snake', 'Saharan horned viper', 'eastern diamondback rattlesnake', 'sidewinder rattlesnake', 'trilobite', 'harvestman', 'scorpion', 'yellow garden spider', 'barn spider', 'European garden spider', 'southern black widow', 'tarantula', 'wolf spider', 'tick', 'centipede', 'black grouse', 'ptarmigan', 'ruffed grouse', 'prairie grouse', 'peafowl', 'quail', 'partridge', 'african grey parrot', 'macaw', 'sulphur-crested cockatoo', 'lorikeet', 'coucal', 'bee eater', 'hornbill', 'hummingbird', 'jacamar', 'toucan', 'duck', 'red-breasted merganser', 'goose', 'black swan', 'tusker', 'echidna', 'platypus', 'wallaby', 'koala', 'wombat', 'jellyfish', 'sea anemone', 'brain coral', 'flatworm', 'nematode', 'conch', 'snail', 'slug', 'sea slug', 'chiton', 'chambered nautilus', 'Dungeness crab', 'rock crab', 'fiddler crab', 'red king crab', 'American lobster', 'spiny lobster', 'crayfish', 'hermit crab', 'isopod', 'white stork', 'black stork', 'spoonbill', 'flamingo', 'little blue heron', 'great egret', 'bittern bird', 'crane bird', 'limpkin', 'common gallinule', 'American coot', 'bustard', 'ruddy turnstone', 'dunlin', 'common redshank', 'dowitcher', 'oystercatcher', 'pelican', 'king penguin', 'albatross', 'grey whale', 'killer whale', 'dugong', 'sea lion', 'Chihuahua', 'Japanese Chin', 'Maltese', 'Pekingese', 'Shih Tzu', 'King Charles Spaniel', 'Papillon', 'toy terrier', 'Rhodesian Ridgeback', 'Afghan Hound', 'Basset Hound', 'Beagle', 'Bloodhound', 'Bluetick Coonhound', 'Black and Tan Coonhound', 'Treeing Walker Coonhound', 'English foxhound', 'Redbone Coonhound', 'borzoi', 'Irish Wolfhound', 'Italian Greyhound', 'Whippet', 'Ibizan Hound', 'Norwegian Elkhound', 'Otterhound', 'Saluki', 'Scottish Deerhound', 'Weimaraner', 'Staffordshire Bull Terrier', 'American Staffordshire Terrier', 'Bedlington Terrier', 'Border Terrier', 'Kerry Blue Terrier', 'Irish Terrier', 'Norfolk Terrier', 'Norwich Terrier', 'Yorkshire Terrier', 'Wire Fox Terrier', 'Lakeland Terrier', 'Sealyham Terrier', 'Airedale Terrier', 'Cairn Terrier', 'Australian Terrier', 'Dandie Dinmont Terrier', 'Boston Terrier', 'Miniature Schnauzer', 'Giant Schnauzer', 'Standard Schnauzer', 'Scottish Terrier', 'Tibetan Terrier', 'Australian Silky Terrier', 'Soft-coated Wheaten Terrier', 'West Highland White Terrier', 'Lhasa Apso', 'Flat-Coated Retriever', 'Curly-coated Retriever', 'Golden Retriever', 'Labrador Retriever', 'Chesapeake Bay Retriever', 'German Shorthaired Pointer', 'Vizsla', 'English Setter', 'Irish Setter', 'Gordon Setter', 'Brittany dog', 'Clumber Spaniel', 'English Springer Spaniel', 'Welsh Springer Spaniel', 'Cocker Spaniel', 'Sussex Spaniel', 'Irish Water Spaniel', 'Kuvasz', 'Schipperke', 'Groenendael dog', 'Malinois', 'Briard', 'Australian Kelpie', 'Komondor', 'Old English Sheepdog', 'Shetland Sheepdog', 'collie', 'Border Collie', 'Bouvier des Flandres dog', 'Rottweiler', 'German Shepherd Dog', 'Dobermann', 'Miniature Pinscher', 'Greater Swiss Mountain Dog', 'Bernese Mountain Dog', 'Appenzeller Sennenhund', 'Entlebucher Sennenhund', 'Boxer', 'Bullmastiff', 'Tibetan Mastiff', 'French Bulldog', 'Great Dane', 'St. Bernard', 'husky', 'Alaskan Malamute', 'Siberian Husky', 'Dalmatian', 'Affenpinscher', 'Basenji', 'pug', 'Leonberger', 'Newfoundland dog', 'Great Pyrenees dog', 'Samoyed', 'Pomeranian', 'Chow Chow', 'Keeshond', 'brussels griffon', 'Pembroke Welsh Corgi', 'Cardigan Welsh Corgi', 'Toy Poodle', 'Miniature Poodle', 'Standard Poodle', 'Mexican hairless dog (xoloitzcuintli)', 'grey wolf', 'Alaskan tundra wolf', 'red wolf or maned wolf', 'coyote', 'dingo', 'dhole', 'African wild dog', 'hyena', 'red fox', 'kit fox', 'Arctic fox', 'grey fox', 'tabby cat', 'tiger cat', 'Persian cat', 'Siamese cat', 'Egyptian Mau', 'cougar', 'lynx', 'leopard', 'snow leopard', 'jaguar', 'lion', 'tiger', 'cheetah', 'brown bear', 'American black bear', 'polar bear', 'sloth bear', 'mongoose', 'meerkat', 'tiger beetle', 'ladybug', 'ground beetle', 'longhorn beetle', 'leaf beetle', 'dung beetle', 'rhinoceros beetle', 'weevil', 'fly', 'bee', 'ant', 'grasshopper', 'cricket insect', 'stick insect', 'cockroach', 'praying mantis', 'cicada', 'leafhopper', 'lacewing', 'dragonfly', 'damselfly', 'red admiral butterfly', 'ringlet butterfly', 'monarch butterfly', 'small white butterfly', 'sulphur butterfly', 'gossamer-winged butterfly', 'starfish', 'sea urchin', 'sea cucumber', 'cottontail rabbit', 'hare', 'Angora rabbit', 'hamster', 'porcupine', 'fox squirrel', 'marmot', 'beaver', 'guinea pig', 'common sorrel horse', 'zebra', 'pig', 'wild boar', 'warthog', 'hippopotamus', 'ox', 'water buffalo', 'bison', 'ram (adult male sheep)', 'bighorn sheep', 'Alpine ibex', 'hartebeest', 'impala (antelope)', 'gazelle', 'arabian camel', 'llama', 'weasel', 'mink', 'European polecat', 'black-footed ferret', 'otter', 'skunk', 'badger', 'armadillo', 'three-toed sloth', 'orangutan', 'gorilla', 'chimpanzee', 'gibbon', 'siamang', 'guenon', 'patas monkey', 'baboon', 'macaque', 'langur', 'black-and-white colobus', 'proboscis monkey', 'marmoset', 'white-headed capuchin', 'howler monkey', 'titi monkey', 'Geoffroy's spider monkey', 'common squirrel monkey', 'ring-tailed lemur', 'indri', 'Asian elephant', 'African bush elephant', 'red panda', 'giant panda', 'snoek fish', 'eel', 'silver salmon', 'rock beauty fish', 'clownfish', 'sturgeon', 'gar fish', 'lionfish', 'pufferfish', 'abacus', 'abaya', 'academic gown', 'accordion', 'acoustic guitar', 'aircraft carrier', 'airliner', 'airship', 'altar', 'ambulance', 'amphibious vehicle', 'analog clock', 'apiary', 'apron', 'trash can', 'assault rifle', 'backpack', 'bakery', 'balance beam', 'balloon', 'ballpoint pen', 'Band-Aid', 'banjo', 'baluster / handrail', 'barbell', 'barber chair', 'barbershop', 'barn', 'barometer', 'barrel', 'wheelbarrow', 'baseball', 'basketball', 'bassinet', 'bassoon', 'swimming cap', 'bath towel', 'bathtub', 'station wagon', 'lighthouse', 'beaker', 'military hat (bearskin or shako)', 'beer bottle', 'beer glass', 'bell tower', 'baby bib', 'tandem bicycle', 'bikini', 'ring binder', 'binoculars', 'birdhouse', 'boathouse', 'bobsleigh', 'bolo tie', 'poke bonnet', 'bookcase', 'bookstore', 'bottle cap', 'hunting bow', 'bow tie', 'brass memorial plaque', 'bra', 'breakwater', 'breastplate', 'broom', 'bucket', 'buckle', 'bulletproof vest', 'high-speed train', 'butcher shop', 'taxicab', 'cauldron', 'candle', 'cannon', 'canoe', 'can opener', 'cardigan', 'car mirror', 'carousel', 'tool kit', 'cardboard box / carton', 'car wheel', 'automated teller machine', 'cassette', 'cassette player', 'castle', 'catamaran', 'CD player', 'cello', 'mobile phone', 'chain', 'chain-link fence', 'chain mail', 'chainsaw', 'storage chest', 'chiffonier', 'bell or wind chime', 'china cabinet', 'Christmas stocking', 'church', 'movie theater', 'cleaver', 'cliff dwelling', 'cloak', 'clogs', 'cocktail shaker', 'coffee mug', 'coffeemaker', 'spiral or coil', 'combination lock', 'computer keyboard', 'candy store', 'container ship', 'convertible', 'corkscrew', 'cornet', 'cowboy boot', 'cowboy hat', 'cradle', 'construction crane', 'crash helmet', 'crate', 'infant bed', 'Crock Pot', 'croquet ball', 'crutch', 'cuirass', 'dam', 'desk', 'desktop computer', 'rotary dial telephone', 'diaper', 'digital clock', 'digital watch', 'dining table', 'dishcloth', 'dishwasher', 'disc brake', 'dock', 'dog sled', 'dome', 'doormat', 'drilling rig', 'drum', 'drumstick', 'dumbbell', 'Dutch oven', 'electric fan', 'electric guitar', 'electric locomotive', 'entertainment center', 'envelope', 'espresso machine', 'face powder', 'feather boa', 'filing cabinet', 'fireboat', 'fire truck', 'fire screen', 'flagpole', 'flute', 'folding chair', 'football helmet', 'forklift', 'fountain', 'fountain pen', 'four-poster bed', 'freight car', 'French horn', 'frying pan', 'fur coat', 'garbage truck', 'gas mask or respirator', 'gas pump', 'goblet', 'go-kart', 'golf ball', 'golf cart', 'gondola', 'gong', 'gown', 'grand piano', 'greenhouse', 'radiator grille', 'grocery store', 'guillotine', 'hair clip', 'hair spray', 'half-track', 'hammer', 'hamper', 'hair dryer', 'hand-held computer', 'handkerchief', 'hard disk drive', 'harmonica', 'harp', 'combine harvester', 'hatchet', 'holster', 'home theater', 'honeycomb', 'hook', 'hoop skirt', 'gymnastic horizontal bar', 'horse-drawn vehicle', 'hourglass', 'iPod', 'clothes iron', 'carved pumpkin', 'jeans', 'jeep', 'T-shirt', 'jigsaw puzzle', 'rickshaw', 'joystick', 'kimono', 'knee pad', 'knot', 'lab coat', 'ladle', 'lampshade', 'laptop computer', 'lawn mower', 'lens cap', 'letter opener', 'library', 'lifeboat', 'lighter', 'limousine', 'ocean liner', 'lipstick', 'slip-on shoe', 'lotion', 'music speaker', 'loupe magnifying glass', 'sawmill', 'magnetic compass', 'messenger bag', 'mailbox', 'tights', 'one-piece bathing suit', 'manhole cover', 'maraca', 'marimba', 'mask', 'matchstick', 'maypole', 'maze', 'measuring cup', 'medicine cabinet', 'megalith', 'microphone', 'microwave oven', 'military uniform', 'milk can', 'minibus', 'miniskirt', 'minivan', 'missile', 'mitten', 'mixing bowl', 'mobile home', 'ford model t', 'modem', 'monastery', 'monitor', 'moped', 'mortar and pestle', 'graduation cap', 'mosque', 'mosquito net', 'vespa', 'mountain bike', 'tent', 'computer mouse', 'mousetrap', 'moving van', 'muzzle', 'metal nail', 'neck brace', 'necklace', 'baby pacifier', 'notebook computer', 'obelisk', 'oboe', 'ocarina', 'odometer', 'oil filter', 'pipe organ', 'oscilloscope', 'overskirt', 'bullock cart', 'oxygen mask', 'product packet / packaging', 'paddle', 'paddle wheel', 'padlock', 'paintbrush', 'pajamas', 'palace', 'pan flute', 'paper towel', 'parachute', 'parallel bars', 'park bench', 'parking meter', 'railroad car', 'patio', 'payphone', 'pedestal', 'pencil case', 'pencil sharpener', 'perfume', 'Petri dish', 'photocopier', 'plectrum', 'Pickelhaube', 'picket fence', 'pickup truck', 'pier', 'piggy bank', 'pill bottle', 'pillow', 'ping-pong ball', 'pinwheel', 'pirate ship', 'drink pitcher', 'block plane', 'planetarium', 'plastic bag', 'plate rack', 'farm plow', 'plunger', 'Polaroid camera', 'pole', 'police van', 'poncho', 'pool table', 'soda bottle', 'plant pot', 'potter's wheel', 'power drill', 'prayer rug', 'printer', 'prison', 'projectile', 'projector', 'hockey puck', 'punching bag', 'purse', 'quill', 'quilt', 'race car', 'racket', 'radiator', 'radio', 'radio telescope', 'rain barrel', 'recreational vehicle', 'fishing casting reel', 'reflex camera', 'refrigerator', 'remote control', 'restaurant', 'revolver', 'rifle', 'rocking chair', 'rotisserie', 'eraser', 'rugby ball', 'ruler measuring stick', 'sneaker', 'safe', 'safety pin', 'salt shaker', 'sandal', 'sarong', 'saxophone', 'scabbard', 'weighing scale', 'school bus', 'schooner', 'scoreboard', 'CRT monitor', 'screw', 'screwdriver', 'seat belt', 'sewing machine', 'shield', 'shoe store', 'shoji screen / room divider', 'shopping basket', 'shopping cart', 'shovel', 'shower cap', 'shower curtain', 'ski', 'balaclava ski mask', 'sleeping bag', 'slide rule', 'sliding door', 'slot machine', 'snorkel', 'snowmobile', 'snowplow', 'soap dispenser', 'soccer ball', 'sock', 'solar thermal collector', 'sombrero', 'soup bowl', 'keyboard space bar', 'space heater', 'space shuttle', 'spatula', 'motorboat', 'spider web', 'spindle', 'sports car', 'spotlight', 'stage', 'steam locomotive', 'through arch bridge', 'steel drum', 'stethoscope', 'scarf', 'stone wall', 'stopwatch', 'stove', 'strainer', 'tram', 'stretcher', 'couch', 'stupa', 'submarine', 'suit', 'sundial', 'sunglass', 'sunglasses', 'sunscreen', 'suspension bridge', 'mop', 'sweatshirt', 'swim trunks / shorts', 'swing', 'electrical switch', 'syringe', 'table lamp', 'tank', 'tape player', 'teapot', 'teddy bear', 'television', 'tennis ball', 'thatched roof', 'front curtain', 'thimble', 'threshing machine', 'throne', 'tile roof', 'toaster', 'tobacco shop', 'toilet seat', 'torch', 'totem pole', 'tow truck', 'toy store', 'tractor', 'semi-trailer truck', 'tray', 'trench coat', 'tricycle', 'trimaran', 'tripod', 'triumphal arch', 'trolleybus', 'trombone', 'hot tub', 'turnstile', 'typewriter keyboard', 'umbrella', 'unicycle', 'upright piano', 'vacuum cleaner', 'vase', 'vaulted or arched ceiling', 'velvet fabric', 'vending machine', 'vestment', 'viaduct', 'violin', 'volleyball', 'waffle iron', 'wall clock', 'wallet', 'wardrobe', 'military aircraft', 'sink', 'washing machine', 'water bottle', 'water jug', 'water tower', 'whiskey jug', 'whistle', 'hair wig', 'window screen', 'window shade', 'Windsor tie', 'wine bottle', 'airplane wing', 'wok', 'wooden spoon', 'wool', 'split-rail fence', 'shipwreck', 'sailboat', 'yurt', 'website', 'comic book', 'crossword', 'traffic or street sign', 'traffic light', 'dust jacket', 'menu', 'plate', 'guacamole', 'consomme', 'hot pot', 'trifle', 'ice cream', 'popsicle', 'baguette', 'bagel', 'pretzel', 'cheeseburger', 'hot dog', 'mashed potatoes', 'cabbage', 'broccoli', 'cauliflower', 'zucchini', 'spaghetti squash', 'acorn squash', 'butternut squash', 'cucumber', 'artichoke', 'bell pepper', 'cardoon', 'mushroom', 'Granny Smith apple', 'strawberry', 'orange', 'lemon', 'fig', 'pineapple', 'banana', 'jackfruit', 'cherimoya (custard apple)', 'pomegranate', 'hay', 'carbonara', 'chocolate syrup', 'dough', 'meatloaf', 'pizza', 'pot pie', 'burrito', 'red wine', 'espresso', 'tea cup', 'eggnog', 'mountain', 'bubble', 'cliff', 'coral reef', 'geyser', 'lakeshore', 'promontory', 'sandbar', 'beach', 'valley', 'volcano', 'baseball player', 'bridegroom', 'scuba diver', 'rapeseed', 'daisy', 'yellow lady's slipper', 'corn', 'acorn', 'rose hip', 'horse chestnut seed', 'coral fungus', 'agaric', 'gyromitra', 'stinkhorn mushroom', 'earth star fungus', 'hen of the woods mushroom', 'bolete', 'corn cob', 'toilet paper'."

q0 = "Event cameras are specialized sensors that detect pixel-level brightness changes asynchronously, capturing only those changes rather than full frames. The events are accumulated over a specific time window to create an image, which represents the intensity of changes during that period."

q1 = "I will provide you with several grayscale event frames generated from event camera data, which capture pixel-level brightness changes over a specific time window. Please note that the frame might be a little noisy. Your task is to determine which category each frame belongs to and return the corresponding category for each frame."

q11 = "Each image consists of four small images arranged in a 2*2 grouping. These four small images all belong to the same category, so give me one category for each four-in-one image."

q2 = "Each image must be classified into one of the above categories. Make sure to match the image with the most relevant category from the list."

q3 = "Treat each image independently. After you classify one image, clear your memory of it before moving to the next. Your response should only include the image name and its corresponding category."

q6 = "Please return the results in dictionary format, where each key is the original image name and the value is the identified category. Do not modify the image names or provide any additional information."

q7 = "I will provide the image name followed by the image itself. Your task is to pair the image with the correct category and return the result as a dictionary entry. No additional information is needed."
q= q00+q0+q1+q11+q2+q3+q6+q7
# prompt_list = [q0, q1, q2, q3, q4, q5, q6,q7,q8,q9,q10]
openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxx"
openai.api_base = "xxxxxxxxxxxxxxxxxxx"
image_count=1


file_path = 'Gray-ImageNet-f2o-groundtruth.txt'

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
file_type = "Gray-ImageNet-f2o-2000"

for image_folder in os.listdir("Gray-ImageNet-f2o-2000"):
    images_file="Gray-ImageNet-f2o-2000/"+image_folder
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
                "url": f"https://mp-ce6aedf9-67f1-428d-8f5a-23b74c183be4.cdn.bspapp.com/Gray-ImageNet-f2o-2000/{images_list[i]}"}}
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
        if not key.endswith(".png"):
            key += ".png"
        cate_list[key] = value

groundtruth_dict={}
with open("Gray-ImageNet-f2o-groundtruth.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            entry = eval(line)
            groundtruth_dict.update(entry)
# print(groundtruth_dict)
# print(cate_list)
sum = 0
for key in cate_list:
    if key in groundtruth_dict:
        if cate_list[key] == groundtruth_dict[key]:
            category_number[cate_list[key]]+=1
            sum+=1
print(f"Accuracy is {sum/len(cate_list)*100:.2f}%")

for category, count in category_counts.items():
    print(f"Category: {category}, Number of Images: {count},Number of identified:{category_number[category]},Percentage is {category_number[category]/count*100:.2f}")
