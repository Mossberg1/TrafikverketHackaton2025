from flask import Flask, render_template, jsonify, send_from_directory
from parkings import fetch_parkings

app = Flask(__name__)

@app.route('/')
def view_map():
    return render_template('map.html')

@app.route('/api/parkings', methods=['GET'])
def get_parkings():
    return jsonify(fetch_parkings(10000))

if __name__ == '__main__':
    app.run()



