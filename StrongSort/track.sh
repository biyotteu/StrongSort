rm -rf /workspace/Final_Submission/result
mkdir /workspace/Final_Submission/result
python track.py --source /workspace/data/Test2/IR_28/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/IR_42/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/IR_43/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_5/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_15/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_19/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_21/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_24/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_32/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_39/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_44/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_45/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_46/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
python track.py --source /workspace/data/Test2/THERM_53/img1 --yolo-weights /workspace/Final_Submission/StrongSort/best_yolo5.pt --classes 0 --save-txt
rm -rf /workspace/Final_Submission/sorted_result
mkdir /workspace/Final_Submission/sorted_result  
python /workspace/Final_Submission/sort.py
