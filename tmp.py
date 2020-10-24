import os

path = "data/obj_train_data"

for file in os.listdir(path):
    if file.endswith('.txt'):
        print("data/obj_train_data/" + file.replace("txt", "bmp"))

