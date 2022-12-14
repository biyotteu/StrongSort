import os
from glob import glob
import shutil

test_path = '/workspace/Final_Submission/data/Test'
new_path = test_path + '2'
shutil.copytree(test_path, new_path)

test = glob(new_path+'/*')

for d in test:
    images = sorted(glob(d+'/img1/*.jpg'))
    shutil.copy(images[0],images[0].replace('.jpg','a.jpg'))
    shutil.copy(images[0],images[0].replace('.jpg','b.jpg'))

## strong sort 1,2프레임이 버려짐 --> 첫 프레임으로 채우기

