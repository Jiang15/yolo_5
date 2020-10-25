import os

path = "data/obj_train_data"

# for file in os.listdir(path):
#     if file.endswith('.txt'):
#         f = open(os.path.join(path, file), "r")
#         lines = f.readlines()
#         print(len(lines))
#         for i in range(len(lines)):
#             l = lines[i].split()
#             s = l[0]
#             if (len(l) > 0):
#                 if( s == "4"):
#
#                     lines[i] = lines[i].replace("4","1",1)
#                 if( s =="6"):
#                     lines[i] = lines[i].replace("6","2",1)
#                 if( s =="7"):
#
#                     lines[i] = lines[i].replace("7","3",1)
#         print(lines)
#         f.close()
#         f1 = open(os.path.join(path, file), "w+")
#         for l in lines:
#             if l!="":
#                 f1.write(l)
#         f1.close()

for file in os.listdir(path):
    if file.endswith('.txt'):
        f = open(os.path.join(path, file), "r")
        lines = f.readlines()
        if len(lines)!=0:
            print(os.path.join(path, file.replace("txt", "bmp")))