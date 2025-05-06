# 🌿 BotanicaLens — Plant Leaf Recognition & Medicinal Benefits Predictor

**BotanicaLens** is a machine learning-powered application that identifies plant species from leaf images and predicts their potential **medicinal benefits**. By combining **image recognition** techniques with a knowledge base of plant properties, the project aims to assist users, researchers, and botanists in understanding the health benefits of various plants through simple image inputs.

---

## ✨ Features

- 🌱 Identify plant species from leaf images
- 💊 Predict and display the medicinal benefits associated with the plant
- 🤖 Trained using machine learning models (CNN/Image Classifier)
- 🗂️ Dataset handling and preprocessing pipelines
- 📈 Evaluation metrics and model performance analysis

---

## 🛠️ Tech Stack

| Component        | Technology |
|------------------|------------|
| Programming      | Python 3.x |
| ML Libraries     | TensorFlow / Keras / scikit-learn |
| Image Processing | OpenCV, PIL |
| Data Handling    | NumPy, Pandas |
| Visualization    | Matplotlib, Seaborn |
| Model Type       | Convolutional Neural Network (CNN) |

---

## 📁 Project Structure
```
BotanicaLens/
  ├── dataset/ # Dataset of plant leaf images
  ├── model/ # Trained ML models and weights
  ├── notebooks/ # Jupyter notebooks for experimentation
  ├── src/
  │ ├── preprocessing.py # Data preprocessing scripts
  │ ├── model.py # Model architecture and training
  │ └── predict.py # Inference script
  ├── requirements.txt # Required libraries
  └── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (optional)

### Installation

```
# Clone the repository
git clone https://github.com/raipranjal-2909/BotanicaLens.git
cd BotanicaLens

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the prediction script with your leaf image
python src/predict.py --image path_to_leaf_image.jpg
```

---

## 🧠 Model Details
Architecture: Convolutional Neural Network (CNN)

Dataset: Custom plant leaf image dataset with labeled medicinal benefits

Training: Data augmentation + Image preprocessing

Evaluation: Accuracy, precision, recall, confusion matrix

---

## 📈 Results
Model Accuracy: 95% 

Test Dataset Size: 3000 images

Classes Detected: List of plant species

---

## 💡 Future Work
🌐 Build a frontend or mobile app for easier user access

🔍 Expand dataset with more plant species

🔗 Integrate external plant knowledge databases for enriched information

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork, raise issues, or submit pull requests to improve datasets, models, or features.

---

## 📬 Contact
Created by Pranjal Rai
For queries, collaborations, or suggestions, feel free to reach out!

---

## 📄 License
This project is open-source and available under the MIT License.
