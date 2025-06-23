AYUSH PANDA  
B.Tech in Computer Science and Engineering  
2nd Year Student  
National Institute of Technology, Rourkela


Please refer only to my soccer project rest are just practise codes .
CHECK RESULT IMAGES AT RESULTSOCCERTACTICAM.PNG AND RESULTSOCCERBROADCAST.PNG
This project focuses on detecting and identifying football players (Red & White teams) and the goalkeeper from broadcast and tactical camera videos using a custom-trained YOLOv11 model.
My model path here is soccerproject\runs\detect\train3\weights\best.pt
soccerproject/
├── train/                # 90 training images (50 from each video)
├── val/                  # 10 validation images
├── images/               # Extracted frames from both videos
├── main.py               # Script for extracting frames from .mp4 files
├── predict.py            # Prediction visualizer (PNG/video) using OpenCV
├── dataset_custom.yaml   # YOLOv11 dataset configuration
├── best.pt               # Final YOLOv11 model weights
├── runs/                 # Training logs and outputs (YOLO default)
└── README.md             # This documentation


I PREPARED MY ANNOTATIONS USING LABEL_STUDIO ON 100 IMAGES 50 FROM EACH AND RANDOMLY DISTRIBUTE IT FO5 TRAINING AND VALIDATION .
performance on validation dataset and batch_size=12 :

Validating runs\detect\train3\weights\best.pt... this good ?? 
Ultralytics 8.3.158  Python-3.12.6 torch-2.7.1+cu128 CUDA:0 (NVIDIA GeForce RTX 4070 Ti SUPER, 16376MiB)
| Class           | Images | Instances | Precision (P) | Recall (R) | mAP\@0.5 | mAP\@0.5:0.95 |
| --------------- | ------ | --------- | ------------- | ---------- | -------- | ------------- |
| **All**         | 10     | 160       | 0.858         | 0.888      | 0.879    | 0.419         |
| Red\_1          | 10     | 10        | 0.955         | 1.000      | 0.995    | 0.437         |
| Red\_2          | 10     | 10        | 0.613         | 0.900      | 0.741    | 0.379         |
| Red\_3          | 10     | 10        | 0.926         | 0.600      | 0.743    | 0.330         |
| Red\_4          | 10     | 10        | 0.847         | 0.900      | 0.844    | 0.541         |
| Red\_5          | 10     | 10        | 0.948         | 1.000      | 0.995    | 0.506         |
| Red\_6          | 5      | 5         | 0.707         | 0.800      | 0.697    | 0.385         |
| Red\_7          | 5      | 5         | 0.707         | 0.800      | 0.682    | 0.378         |
| Red\_8          | 5      | 10        | 0.988         | 1.000      | 0.995    | 0.398         |
| Red\_9          | 5      | 5         | 0.731         | 0.800      | 0.805    | 0.240         |
| Red\_Goalkeeper | 10     | 10        | 0.883         | 1.000      | 0.995    | 0.485         |
| White\_1        | 10     | 10        | 0.907         | 0.982      | 0.986    | 0.574         |
| White\_2        | 5      | 5         | 0.909         | 1.000      | 0.995    | 0.310         |
| White\_3        | 10     | 10        | 0.850         | 0.900      | 0.844    | 0.500         |
| White\_4        | 10     | 10        | 0.661         | 0.392      | 0.477    | 0.168         |
| White\_5        | 10     | 10        | 0.982         | 1.000      | 0.995    | 0.429         |
| White\_6        | 10     | 10        | 0.934         | 0.800      | 0.817    | 0.402         |
| White\_7        | 5      | 5         | 0.912         | 1.000      | 0.995    | 0.532         |
| White\_8        | 5      | 5         | 0.812         | 1.000      | 0.995    | 0.514         |
| White\_9        | 5      | 5         | 1.000         | 0.893      | 0.995    | 0.508         |
| White\_10       | 5      | 5         | 0.886         | 1.000      | 0.995    | 0.359         |

| Metric       | Meaning                                                                          |
| ------------ | -------------------------------------------------------------------------------- |
| **Box(P)**   | Precision — % of detections that were correct. (High = fewer false positives)    |
| **R**        | Recall — % of actual objects correctly detected. (High = fewer misses)           |
| **mAP50**    | Mean Average Precision at IoU 0.5 — standard accuracy score in object detection. |
| **mAP50-95** | Average over multiple IoU thresholds (0.5 to 0.95, step 0.05). Tougher metric.   |

An impressive feat .
Runs and retains player id which can be seen from given ims as samples users can try it

