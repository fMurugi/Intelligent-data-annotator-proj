from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def dashboard():
    return send_file("/home/fiona/Desktop/tuts/school_project/homePage/map_with_menu.html")  # Serve your HTML file

if __name__ == "__main__":
    app.run(port=7000)
