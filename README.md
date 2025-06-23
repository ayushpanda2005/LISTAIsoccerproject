SUBMITTED BY:
AYUSH PANDA 
BTECH CSE
SECOND YEAR STUDENT
NIT RKL

Please refer only to my soccer project rest are just practise codes .
CHECK RESULT IMAGES AT RESULTSOCCERTACTICAM.PNG AND RESULTSOCCERBROADCAST.PNG
This project focuses on detecting and identifying football players (Red & White teams) and the goalkeeper from broadcast and tactical camera videos using a custom-trained YOLOv11 model.
My model path here is soccerproject\runs\detect\train3\weights\best.pt
soccerproject/
├── train/  Training images and labels 90 in number randomly taken by 50 - 50 images and labels from both videos each 100 total
├── val/ Validation images and labels 10 in number
├── images/  Extracted frames from videos
├── main.py  Frame extraction script
├── predict.py  PNG/video prediction visualizer using cv2 module 
├── dataset_custom.yaml # Custom dataset config
├── best.pt # Final trained YOLOv11 model
├── runs/ # YOLOv11 training logs
└── README.md

I PREPARED MY ANNOTATIONS USING LABEL_STUDIO ON 100 IMAGES 50 FROM EACH AND RANDOMLY DISTRIBUTE IT FO5 TRAINING AND VALIDATION .
performance on validation dataset and batch_size=12 :

Validating runs\detect\train3\weights\best.pt... this good ?? 
Ultralytics 8.3.158  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4070 Ti SUPER, 16376MiB)
YOLOv5x summary (fused): 150 layers, 97,171,868 parameters, 0 gradients, 246.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 1/1 [00:00<00:00,  4.10it/s]
                   all         10        160      0.858      0.888      0.879      0.419
                 Red_1         10         10      0.955          1      0.995      0.437
                 Red_2         10         10      0.613        0.9      0.741      0.379
                 Red_3         10         10      0.926        0.6      0.743       0.33
                 Red_4         10         10      0.847        0.9      0.844      0.541
                 Red_5         10         10      0.948          1      0.995      0.506
                 Red_6          5          5      0.707        0.8      0.697      0.385
                 Red_7          5          5      0.707        0.8      0.682      0.378
                 Red_8          5         10      0.988          1      0.995      0.398
                 Red_9          5          5      0.731        0.8      0.805       0.24
        Red_Goalkeeper         10         10      0.883          1      0.995      0.485
               White_1         10         10      0.907      0.982      0.986      0.574
               White_2          5          5      0.909          1      0.995       0.31
               White_3         10         10       0.85        0.9      0.844        0.5
               White_4         10         10      0.661      0.392      0.477      0.168
               White_5         10         10      0.982          1      0.995      0.429
               White_6         10         10      0.934        0.8      0.817      0.402
               White_7          5          5      0.912          1      0.995      0.532
               White_8          5          5      0.812          1      0.995      0.514
               White_9          5          5          1      0.893      0.995      0.508
              White_10          5          5      0.886          1      0.995      0.359
| Metric       | Meaning                                                                          |
| ------------ | -------------------------------------------------------------------------------- |
| **Box(P)**   | Precision — % of detections that were correct. (High = fewer false positives)    |
| **R**        | Recall — % of actual objects correctly detected. (High = fewer misses)           |
| **mAP50**    | Mean Average Precision at IoU 0.5 — standard accuracy score in object detection. |
| **mAP50-95** | Average over multiple IoU thresholds (0.5 to 0.95, step 0.05). Tougher metric.   |

An impressive feat .
Runs and retains player id which can be seen from given ims as samples users can try it

