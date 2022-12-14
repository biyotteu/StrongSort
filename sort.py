from glob import glob
import os
from functools import cmp_to_key

def xy_compare(x, y):
    if int(x[1]) > int(y[1]): # y좌표가 작은 것부터 앞으로
        return 1
    elif int(x[1]) == int(y[1]): # y좌표가 같을 경우
        if int(x[0]) > int(y[0]): # x 좌표가 작은 것이 앞으로 나오게
            return 1
        elif int(x[0]) < int(y[0]): # x 좌표가 큰 것이 뒤로
            return -1
        else: # 같은 경우에는 그대로
            return 0
    else: # y좌표가 큰 것이 뒤로
        return -1

list_dir = glob('/workspace/Final_Submission/result/*.txt')
print(len(list_dir))
for path in list_dir:
    f_read = open(path,'r')
    f_write = open(path.replace('result','sorted_result').replace('_.txt','.txt'),'w')
    lines = f_read.readlines()
    # print(lines[0])
    for i in range(len(lines)):
        lines[i] = lines[i].replace(" \n","")
        lines[i] = lines[i].split(' ')
    # print(lines)
    lines = sorted(lines,key=cmp_to_key(xy_compare))
    # print(lines)
    for i in range(len(lines)):
        tmp = lines[i][0]
        for j in range(1,len(lines[i])):
            tmp = tmp + "," + lines[i][j]
        tmp = tmp + "\n"
        lines[i] = tmp
    f_write.writelines(lines) 
    # break