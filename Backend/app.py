from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow import expand_dims
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend (React) to access API

# Load model once when server starts
model = load_model('model.h5')

# Class names (80 classes)
class_names = ['Aloevera','Amla','Amruthaballi','Arali','Astma_weed','Badipala','Balloon_Vine','Bamboo','Beans','Betel',
               'Bhrami','Bringaraja','Caricature','Castor','Catharanthus','Chakte','Chilly','Citron lime (herelikai)','Coffee',
               'Common rue(naagdalli)','Coriender','Curry','Doddpathre','Drumstick','Ekka','Eucalyptus','Ganigale','Ganike',
               'Gasagase','Ginger','Globe Amarnath','Guava','Henna','Hibiscus','Honge','Insulin','Jackfruit','Jasmine',
               'Kambajala','Kasambruga','Kohlrabi','Lantana','Lemon','Lemongrass','Malabar_Nut','Malabar_Spinach','Mango',
               'Marigold','Mint','Neem','Nelavembu','Nerale','Nooni','Onion','Padri','Palak(Spinach)','Papaya','Parijatha',
               'Pea','Pepper','Pomoegranate','Pumpkin','Raddish','Rose','Sampige','Sapota','Seethaashoka','Seethapala',
               'Spinach1','Tamarind','Taro','Tecoma','Thumbe','Tomato','Tulsi','Turmeric','ashoka','camphor','kamakasturi','kepala']

plant_benefits = {
    "Neem": "Treats skin disorders, boosts immunity, has anti-bacterial and anti-inflammatory properties.",
    "Tulsi": "Relieves cold, cough, and sore throat; helps in digestion and reducing stress.",
    "Amla": "Rich in Vitamin C, boosts immunity, good for digestion and skin.",
    "Aloevera": "Soothes skin, aids digestion, and helps in healing wounds.",
    "Turmeric": "Anti-inflammatory, antiseptic, improves liver health.",
}


@app.route('/predict', methods=['POST'])
def predict():
    filepath = 'temp.jpg'

    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    try:
        # Save uploaded file
        file.save(filepath)

        # Load and preprocess image
        image = load_img(filepath, target_size=(299, 299))
        image_array = img_to_array(image)
        image_array = expand_dims(image_array, axis=0)

        # Predict using model
        predictions = model.predict(image_array)

        if predictions.shape[0] == 0:
            raise ValueError("Prediction failed, no output returned.")

        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(np.max(predictions[0])) * 100

        plant_name = class_names[predicted_class]
        result = {
            'class': plant_name,
            'confidence': round(confidence, 2),
            'benefit': plant_benefits.get(plant_name, "Benefit information not available.")
        }

    except Exception as e:
        result = {'error': f'Prediction error: {str(e)}'}

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)