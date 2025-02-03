
from flask import Flask, request, jsonify
from flask_cors import CORS
import ee

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  

# Initialize Google Earth Engine
ee.Initialize(project="dynamic-sun-449808-i5")
project_id = "dynamic-sun-449808-i5"
@app.route('/get_ndvi', methods=['POST'])
def get_ndvi():
    data = request.get_json()
    print("Received NDVI request:", data)  # Debugging log

    try:
        south, west, north, east = data["south"], data["west"], data["north"], data["east"]
        roi = ee.Geometry.Rectangle([west, south, east, north])

        collection = ee.ImageCollection('COPERNICUS/S2') \
            .filterBounds(roi) \
            .filterDate('2020-01-01', '2025-01-01') \
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))

        def addNDVI(image):
            ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
            return image.addBands(ndvi)

        with_ndvi = collection.map(addNDVI)
        median_ndvi = with_ndvi.select('NDVI').median().clip(roi)

        # Visualization parameters
        ndvi_vis = {'min': 0, 'max': 1, 'palette': ['blue', 'white', 'green']}

        # ✅ Generate a tile layer URL (instead of a static image)
        map_id = median_ndvi.getMapId(ndvi_vis)
        project_id = "dynamic-sun-449808-i5"  # ✅ Replace with your actual project ID
        map_url = f"https://earthengine.googleapis.com/v1/{map_id['mapid']}/tiles/{{z}}/{{x}}/{{y}}"

        print("Generated NDVI Tile URL:", map_url)  # ✅ Debugging log
        return jsonify({"map_url": map_url})
  

    except Exception as e:
        print("Error generating NDVI:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
