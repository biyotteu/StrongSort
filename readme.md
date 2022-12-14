# 국방 AI 경진대회 코드 사용법
NavyNet: 김윤수, 성수영, 김덕현, 김민섭

# 모델 설명
뛰어난 object detection 성능을 자랑하는 yolov5를 탐지 모델로 사용하였고, StrongSORT Tracker를 사용하여 다중 객체 트래킹을 진행했다. IR이미지와 THERMAL이미지의 도메인적 특성을 고려해 분리하여 학습하고 추론하여 후처리하여 성능을 냈다.

# 코드 설명
  - make_new_test.py          strong sort 알고리즘 시 빠지는 프레임 보충
  - make_path                 제공된 data에서 Yolo형식 라벨 생성
  - make_text.py              train,val,test 나눔
  - sort.py                   객체 아이디 기준으로 mot 라벨 정렬
  
  - StrongSort/               테스트 결과 폴더
    - yolov5/                 yolov5 폴더
    
## 주요 설치 library
- pytorch==1.13.0
- torchvision==0.14.0
- cudatoolkit=11.7
- opencv-python==4.6.0.66
- scikit-learn==1.0.2

# 실행 환경 설정

  - 환경 설치
    ```
    pip install -r ./StrongSort/requirements.txt
    pip install -r ./StrongSort/yolov5/requirements.txt
    ```

# 학습 실행 방법
`./BaselineModel/train.py` 내의 경로명을 실제 학습 환경에 맞게 수정
```
cd /workspace/Final_Submission/StrongSort/yolov5
ex) python train.py --data <data.yaml> --epochs 300 --weights '' --cfg yolov5x.yaml  --batch-size 24 --workers 2


python train.py --data over.yaml --epochs 13 --weights '/workspace/Final_Submission/weights_yolos/best_yolo5.pt' --cfg yolov5x.yaml  --batch-size 24 --workers 2  -> 결과 weight == 13over.pt 
python train.py --data over.yaml --epochs 11 --weights '/workspace/Final_Submission/weights_yolos/11epoch_13over.pt' --cfg yolov5x.yaml  --batch-size 24 --workers 2 -> 결과 weight == 11epoch_13over.pt
```

사용한 학습 가중치 파일 출처 https://github.com/biyotteu/StrongSort/blob/main/yolo.zip
- **최종 제출 파일 :./post_sota_ensemble/**
# Track 실행 방법

track.sh 파일 내부에 데이터 경로, 가중치 수정가능
ex)python track.py --source <data_path> --yolo-weights <with_path> --classes 0 --save-txt
```
cd /workspace/Final_Submission/StrongSort
sh track.sh
```

# 후처리 실행 방법
  - ./post_processing.ipynb 실행
  - 각 셀 (마스크 합성) 아래 경로 확인 후 실행
      ```
      label_dir_path = '/workspace/sorted_result/*.txt'
      processed_label_dir_path = '/workspace/post/post_0/'
      ```
  - ./post/post_0 ~ post_6에 각각의 후처리 단계 저장
  - ./post/post_6 최종 결과물이 저장됨.