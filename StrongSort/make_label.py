import json
from glob import glob
from tqdm import tqdm
import random
import os 
from shutil import copyfile
from tqdm.auto import tqdm
from multiprocessing import Process
# import multiprocessing
# from functools import partial
# from contextlib import contextmanager
classes = [
    "사람",
    "오토바이탄사람",
    "자전거탄사람",
    "킥보드탄사람",
    "오토바이",
    "자전거",
    "킥보드",
]

image_paths = glob('/mnt/d/data/01.데이터/2.Validation/원천데이터/VS_사건사고데이터이미지/사건사고데이터이미지/*/*/*.jpg')

random.shuffle(image_paths)

train_paths = image_paths[:50000] 
val_paths = image_paths[50000:52000] 
test_paths = image_paths[52000:54000]

save_image_dir = '/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/images/'
save_label_dir = '/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/labels/'
origin_label_dir = '/mnt/d/data/01.데이터/2.Validation/라벨링데이터/사건사고데이터이미지/'
save_image_dir_linux = '/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/images/'

def convert(paths,txt_path):
    f_txt = open(txt_path,'w', encoding='UTF-8')

    for path in tqdm(paths):
        filename = os.path.basename(path)
        f_txt.write(save_image_dir_linux+filename+"\n")

    f_txt.close()

convert(train_paths,'/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/train.txt')
convert(val_paths,'/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/val.txt')
convert(test_paths,'/mnt/c/Users/Navy/Desktop/maicon/Yolov5_StrongSORT_OSNet/yolov5/dataset/test.txt')

def convert(paths):

    for path in tqdm(paths):
        filename = os.path.basename(path)
        label_path = origin_label_dir+'/'+'/'.join(path.split('/')[-3:]).replace('.jpg','.json')
        # print(path)
        # print(label_path)

        try:
            with open(label_path,'r', encoding='UTF-8') as f:
                json_object = json.load(f)
        except:
            continue
        
        size = json_object["image"]["size"]
        label_data = ""
        for ano in json_object['annotation']:
                class_name = classes.index(ano["property"]["name"])
                bbox = ano["bndbox"]
                x = (bbox['xmin']+bbox['xmax'])/(2*size['width'])
                y = (bbox['ymin']+bbox['ymax'])/(2*size['height'])
                width = (bbox['xmax'] - bbox['xmin'])/size['width']
                height = (bbox['ymax'] - bbox['ymin'])/size['height']
                label_data = label_data + str(class_name) + " " + str(x) + " " + str(y) + " " + str(width) + " " + str(height) + "\n"

        f_label = open(save_label_dir+filename.replace('.jpg','.txt'),'w', encoding='UTF-8')
        f_label.write(label_data)
        f_label.close()
        
        result_path = save_image_dir+filename
        copyfile(path,result_path)

print("load")
p_list = []

for i in range(11):
    p_list.append(Process(target=convert, args=(train_paths[5000*(i-1):5000*i],)))

p1 = Process(target=convert, args=(val_paths,))
p2 = Process(target=convert, args=(test_paths,))

for i in range(11):
    p_list[i].start()
p1.start();p2.start();

for i in range(11):
    p_list[i].join()
p1.join();p2.join();
