from glob import glob
import os
import shutil
import cv2
from tqdm import tqdm
from multiprocessing import Process
train_p = '/workspace/Final_Submission/data/Train/'
train_paths = glob(train_p+'*')
save_image_path = '/workspace/Final_Submission/Yolov5_StrongSORT_OSNet/yolov5/dataset/images/'
save_label_path = '/workspace/Final_Submission/Yolov5_StrongSORT_OSNet/yolov5/dataset/labels/'

def convert(paths):
    for dir_path in tqdm(paths):
        f = open(dir_path+'/gt/gt.txt','r')
        lines = f.readlines()
        f.close()
        images = glob(dir_path+'/img1/*.jpg')
        images = sorted(images)
        labels = [[] for i in range(len(images))]
        for label in lines:
            label = label.replace("\n","")
            tmp = label.split(',')
            image_idx = int(tmp[0]) - 1
            labels[image_idx].append(label)

        for i in range(len(images)):
            tmp = images[i].split('/')
            filename = tmp[-3]+'_'+tmp[-1]
            (height,width,_) = cv2.imread(images[i]).shape
            shutil.copy(images[i], save_image_path+filename)
            f_write = open(save_label_path+filename.replace('.jpg','.txt'),'w')
            for label in labels[i]:
                tmp = label.split(',')
                left = int(tmp[2])
                top = int(tmp[3])
                w = int(tmp[4])
                h = int(tmp[5])
                cx = (left + w/2)/width
                cy = (top + h/2)/height
                w = w/width
                h = h/height
                f_write.write('0 '+str(cx)+' '+str(cy)+' '+str(w)+' '+str(h)+'\n')
            f_write.close()

print("load",len(train_paths))
p_list = []

term = len(train_paths)//10
for i in range(11):
    p_list.append(Process(target=convert, args=(train_paths[term*i:min(term*(i+1),len(train_paths))],)))


for i in range(11):
    p_list[i].start()

for i in range(11):
    p_list[i].join()
print('complete')