# 🦾 Handover – Real-Time 3D Gesture Control with Python, MediaPipe & Blender

> Like Iron Man... but on a student budget 😄  
> This project lets you control a **3D robotic arm in Blender** using only your hand movements, detected live through your webcam — no controller, no sensors.

---

## 🎥 Demo Video

▶️ [Watch the demo on YouTube](https://youtu.be/NQjh0z16frE)

---

## 🧠 Technologies Used

- **Python** – for real-time processing
- **MediaPipe** – for hand tracking (21 landmarks)
- **OpenCV** – for webcam input
- **Blender** – for animating the 3D object

---

## 📁 Project Structure

```bash
Handover/
├── main.py                # Captures and interprets hand gestures
├── HandTrackingModule.py # Hand detection using MediaPipe
├── scripting_blender.py  # Run this inside Blender to control your object
├── scale.txt              # Scaling instructions
├── rotate.txt             # Rotation instructions
├── pan.txt                # Translation instructions
└── README.md              # This file ✨
```

---

## 🚀 How to Run the Project

### 1. Install dependencies

```bash
pip install mediapipe opencv-python
```

### 2. Run the Python script

```bash
python main.py
```

### 3. In Blender:

- Delete the default camera and light
- Add an object (like a Cube or robotic arm)
- Go to the **Scripting** tab
- Paste the content of `scripting_blender.py`
- Click ▶️ **Run Script**

---

## 🔧 Customization

- Replace `"Robotic Arm"` in `scripting_blender.py` with the **exact name** of your Blender object
- The `.txt` files act as a communication bridge between Python and Blender (real-time control)
- You can tweak speed, movement limits, and sensitivity

---

## 👩‍💻 About

Created by **Fatoumata Diallo**  
This project explores:
- Applied artificial intelligence (AI)
- Gesture-based interaction
- Creative multi-tool integration (Python ↔ Blender)

---

## 🧾 License

[MIT License](LICENSE)

---

## ⭐ Like this project?

- Give it a ⭐️ on GitHub
- Share it with others
- Fork it and build your own version!
