import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
from tensorflow import expand_dims

# Class Names
class_names = ['Aloevera','Amla','Amruthaballi','Arali','Astma_weed','Badipala','Balloon_Vine','Bamboo','Beans','Betel','Bhrami','Bringaraja','Caricature','Castor','Catharanthus','Chakte','Chilly','Citron lime (herelikai)','Coffee','Common rue(naagdalli)','Coriender','Curry','Doddpathre','Drumstick','Ekka','Eucalyptus','Ganigale','Ganike','Gasagase','Ginger','Globe Amarnath','Guava','Henna','Hibiscus','Honge','Insulin','Jackfruit','Jasmine','Kambajala','Kasambruga','Kohlrabi','Lantana','Lemon','Lemongrass','Malabar_Nut','Malabar_Spinach','Mango','Marigold','Mint','Neem','Nelavembu','Nerale','Nooni','Onion','Padri','Palak(Spinach)','Papaya','Parijatha','Pea','Pepper','Pomoegranate','Pumpkin','Raddish','Rose','Sampige','Sapota','Seethaashoka','Seethapala','Spinach1','Tamarind','Taro','Tecoma','Thumbe','Tomato','Tulsi','Turmeric','ashoka','camphor','kamakasturi','kepala']

# Load the model
model = load_model(r'd:\BotanicaLens\model.h5')  # make sure 'model' is correct directory or path

# Load and preprocess the image
image_path = r"C:\Users\Dell\Desktop\Medicinal-Plants-Detection-Using-Deep-Learning-main\Medicinal-Plants-Detection-Using-Deep-Learning-main\Data\Aloevera.png"  # <---- PUT YOUR IMAGE PATH HERE
image = load_img(image_path, target_size=(299, 299))  # adjust to (224, 224) if MobileNetV2
image_array = img_to_array(image)
image_array = expand_dims(image_array, axis=0)

# Model prediction
predictions = model.predict(image_array)

# Softmax output → no need sigmoid
predicted_class = np.argmax(predictions[0])
confidence = 100 * np.max(predictions[0])

# Result
print("This image most likely belongs to '{}' with a {:.2f}% confidence."
      .format(class_names[predicted_class], confidence))
