# YOLO Video Processing Project

## 📌 Overview
This project demonstrates object detection and semantic segmentation using YOLO models. The workflow includes:
- Converting video into frames
- Applying object detection and segmentation
- Reconstructing processed frames into videos
- Comparing raw, detected, and segmented outputs

---

## ⚙️ Technologies Used
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- FFmpeg

---

## 📂 Project Structure
video_project/
│
├── make_video.py
├── add_music.py
├── metrics.py
├── REPORT.pdf
├── README.md


---

## 🎥 Outputs
- Object Detection Video
- Segmentation Video
- Final Stacked Comparison Video

---

## 📊 Performance Metrics
- Precision-Recall Curve
- Recall-Confidence Curve
- mAP@0.5 ≈ 0.60

---

## 📄 Report
Detailed explanation of YOLO dataset configuration and meta files is included in `REPORT.pdf`.

---

## 🚀 How to Run
```bash
python make_video.py
python add_music.py

## References

- Ultralytics YOLO Documentation: https://docs.ultralytics.com  
- YOLO Dataset Format Guide: https://docs.ultralytics.com/datasets  