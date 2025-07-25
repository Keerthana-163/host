from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Image Hosting Server Running!"

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)

