import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

MODEL_PATH = os.path.join("model", "phone_grade_model.h5")

try:
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Failed to load model: {e}")

def predict_condition(img_path):
    try:
        print(f"🔍 Predicting for: {img_path}")
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0][0]
        confidence = float(prediction)

        if confidence >= 0.5:
            label = "Good"
            score = round(confidence * 100, 2)
        else:
            label = "Damaged"
            score = round((1 - confidence) * 100, 2)

        return {"condition": label, "confidence": score}
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        raise e
