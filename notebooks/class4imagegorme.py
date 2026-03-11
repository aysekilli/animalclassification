import os

label_folder = "./data/train/labels"
image_folder = "./data/train/images"

for label_file in os.listdir(label_folder):

    path = os.path.join(label_folder, label_file)

    with open(path) as f:
        lines = f.readlines()

    for line in lines:

        class_id = line.split()[0]

        if class_id == "4":

            image_name = label_file.replace(".txt",".jpg")
            print(image_name)