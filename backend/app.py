from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils import predict_condition

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "📱 PhoneGradeAI Flask API is running."

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        result = predict_condition(filepath)

        os.remove(filepath)  # cleanup

        return jsonify(result)

    except Exception as e:
        # Return error message and 500 status
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)