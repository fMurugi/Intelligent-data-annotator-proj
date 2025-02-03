# 🌿 Vegetation Analysis Using Google Earth Engine

This project allows users to analyze vegetation cover using **Google Earth Engine (GEE)**, **Flask**, and **Leaflet.js**.

## 📌 Features
- 🗺️ **Draw a bounding box** to select an area for analysis.
- 🌍 **Fetch NDVI (vegetation) data** from Google Earth Engine.
- 🖼️ **Visualize NDVI layers** on an interactive Leaflet map.
- 🚀 **Fast API-based retrieval of vegetation data**.

---

## 🛠️ Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

🔥 Running the Application
1️⃣ Start the Flask Backend

```bash
python app.py
```
API should now be running at: http://127.0.0.1:5000/
2️⃣ Start the Frontend

```bash
python3 -m http.server 8000
```
Now open http://0.0.0.0:8000/vegetation_cover.html in your browser.

🛠️ Technologies Used

    Python (Flask) - Backend API
    Google Earth Engine (GEE) - NDVI data
    Leaflet.js - Interactive map
    HTML, JavaScript, CSS - Frontend UI


# setting up google earth engine
    ensure you have a project
    in google cloud console enable earth engine API
    run this command to authenticate locally in a venv
    ```bash
    earthengine authenticate
    ```