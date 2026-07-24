# 🍄 Mushroom Edibility Prediction using Machine Learning

A Machine Learning web application built with **Python**, **Flask**, and **Scikit-learn** that predicts whether a mushroom is **Edible** or **Poisonous** based on its physical characteristics.

---

## 📷 Application Preview

![image](https://github.com/tushar18-2006/mushroom-predictor-ml/blob/b9cb30cbe6fa3b41d93eafbef80faffcf72bc739/Mushroom.png)

---

## 📌 Project Overview

This project uses a **Decision Tree Classifier** trained on the Mushroom Dataset to classify mushrooms as:

- 🍄 **Edible**
- ☠️ **Poisonous**

Users simply select the mushroom's characteristics from dropdown menus, and the model predicts whether it is safe to eat.

---

## ✨ Features

- Beautiful and responsive user interface
- Instant prediction using Machine Learning
- Flask backend
- Decision Tree Classifier
- Label Encoding for categorical features
- Easy to deploy

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Scikit-learn
- NumPy
- Pandas
- Joblib
- HTML5
- CSS3

---

## 📂 Project Structure

```
Mushroom-Edibility-Prediction/
├── decision_tree_mushroom.pkl
├── mushroom_encoder.pkl
├── app.py
├── mushrooms.csv
├── requirements.txt
├── Mushroom.png
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/tushar18-2006/mushroom-edibility-prediction.git
```

### Move into the project directory

```bash
cd mushroom-edibility-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Model

- Algorithm: Decision Tree Classifier
- Data Preprocessing: Label Encoding
- Input Features: 22 Mushroom Characteristics
- Output:
  - Edible 🍄
  - Poisonous ☠️

---

## 📊 Input Features

- Cap Shape
- Cap Surface
- Cap Color
- Bruises
- Odor
- Gill Attachment
- Gill Spacing
- Gill Size
- Gill Color
- Stalk Shape
- Stalk Root
- Stalk Surface Above Ring
- Stalk Surface Below Ring
- Stalk Color Above Ring
- Stalk Color Below Ring
- Veil Type
- Veil Color
- Ring Number
- Ring Type
- Spore Print Color
- Population
- Habitat

---

## 🚀 Future Improvements

- Add probability/confidence score
- Display mushroom images
- Support Random Forest and XGBoost models
- Deploy on Render or Railway
- Improve UI with animations
- Mobile-friendly interface

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---


## 👨‍💻 Author

**Tushar Harihar**

BCA Student | Python Developer | Machine Learning Enthusiast

If you found this project helpful, don't forget to ⭐ the repository!
