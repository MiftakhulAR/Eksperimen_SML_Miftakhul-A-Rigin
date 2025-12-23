# Eksperimen_SML_Miftakhul-A-Rigin

Repository ini berisi eksperimen **Supervised Machine Learning**
untuk klasifikasi penyakit jantung (Heart Disease Classification).

Eksperimen mencakup:
- Data preprocessing
- Training model machine learning
- Experiment tracking menggunakan **MLflow**
- Logging eksperimen **ONLINE melalui DagsHub**

## 📊 Dataset

Dataset yang digunakan adalah **Heart Disease Dataset** dengan tipe
**klasifikasi biner** (memiliki penyakit jantung atau tidak).

Sumber dataset:
- Github – Heart Disease Dataset

File dataset:
- `heart_raw.csv` → data mentah
- `heart_preprocessed.csv` → hasil preprocessing

## 🧹 Preprocessing

Tahapan preprocessing meliputi:
- Handling missing values
- Encoding data kategorikal
- Normalisasi fitur numerik
- Pemisahan fitur dan label

Script preprocessing:
preprocessing/automate_Miftakhul-A-Rigin.py

Untuk menjalankan preprocessing:
python preprocessing/automate_Miftakhul-A-Rigin.py

## 🤖 Training Model & MLflow Tracking

Model machine learning dilatih menggunakan Scikit-Learn
dan dilacak menggunakan MLflow Tracking ONLINE melalui DagsHub.

Eksperimen mencatat:
- Accuracy
- Precision
- Recall
- F1-score

Artefak tambahan yang dilog:
- confusion_matrix.png
- sample_data.csv

Script training model:
modelling/modelling.py

Untuk menjalankan training:
python modelling/modelling.py

🌐 MLflow Tracking (Online)

Semua eksperimen dapat diakses secara online melalui DagsHub:

🔗 DagsHub Repository & Experiments
https://dagshub.com/MiftakhulAR/Eksperimen_SML_Miftakhul-A-Rigin
