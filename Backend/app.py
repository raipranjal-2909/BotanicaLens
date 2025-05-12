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

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    filepath = 'temp.jpg'
    file.save(filepath)

    try:
        # Preprocess image
        image = load_img(filepath, target_size=(224, 224))
        image_array = img_to_array(image)
        image_array = expand_dims(image_array, axis=0)

        # Prediction
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0])) * 100

        result = {
            'class': class_names[predicted_class],
            'confidence': round(confidence, 2)
        }

    except Exception as e:
        result = {'error': str(e)}
    finally:
        os.remove(filepath)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)