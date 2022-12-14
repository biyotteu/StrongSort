d = ['./overlay.txt','./overlap_list.txt','./train.txt','./val.txt']

for i in d:
    f = open(i,'r')
    lines = f.readlines()
    f.close()
    l = []
    for j in range(len(lines)):
        if lines[j] != '\n':
            l.append(lines[j].replace('Yolov5_StrongSORT_OSNet','StrongSort'))
    f = open(i,'w')
    f.writelines(l)
    f.close()
