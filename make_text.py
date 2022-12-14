from glob import glob
import random
save = '/workspace/Final_Submission/Yolov5_StrongSORT_OSNet/yolov5/dataset/'
images = glob('/workspace/Final_Submission/Yolov5_StrongSORT_OSNet/yolov5/dataset/images/*')

# random.seed(1024)
# random.shuffle(images)
# images = sorted(images)

# f = open('/workspace/Yolov5_StrongSORT_OSNet/yolov5/dataset/val.txt')
# val = f.readlines()
# f.close()
# ir = []
# th = []

# use = []
# for i in range(len(images)):
#     images[i] = images[i] + "\n"
#     if images[i] in val:
#         continue
#     use.append(images[i])
    # print(img)
    # if 'IR' in img:
    #     ir.append(img)
    # else:
    #     th.append(img)


# random.shuffle(ir)
# random.shuffle(th)

print(use[:10:2])
print(use[1:10:2])
# print(len(use[0::2]),len(use[1::2]))
# f_train_odd = open(save+'train_odd.txt','w')
# f_train_odd.writelines(use[0::2])
# f_train_odd.close()
# f_train_even = open(save+'train_odd.txt','w')
# f_train_even.writelines(use[1::2])
# f_train_even.close()

# f_ir_train = open(save+'train.txt','w')
# f_ir_train.writelines(images[:-1000])
# f_ir_val = open(save+'val.txt','w')
# f_ir_val.writelines(images[-1000:])

# f_ir_train = open(save+'ir_train.txt','w')
# f_ir_train.writelines(ir[:-200])
# f_ir_val = open(save+'ir_val.txt','w')
# f_ir_val.writelines(ir[-200:])
# f_ir_test = open(save+'ir_test.text')
# f_ir_train.close()
# f_ir_val.close()
# f_th_train = open(save+'th_train.txt','w')
# f_th_train.writelines(th[:-200])
# f_th_val = open(save+'th_val.txt','w')
# f_th_val.writelines(th[-200:])
# f_th_train.close()
# f_th_val.close()
# f_th_test = open(save+'th_test.text')

