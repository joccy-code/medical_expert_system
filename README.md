
# 🩺 Medical Diagnosis Expert System (Python)

An **AI-based medical diagnosis expert system** written in Python.
It asks patients for their details and symptoms, then suggests possible diseases and prescriptions based on a knowledge base.

---

## 🚀 Features

* ✅ Patient registration (name, age, gender)
* ✅ Symptom-based disease diagnosis
* ✅ Threshold-based diagnosis (≥25% symptom match)
* ✅ Fallback to **best match** if no disease meets threshold
* ✅ Medication prescription for diagnosed diseases
* ✅ Console-based interaction

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/joccy-code/medical_expert_system.git
cd medical_expert_system
```

### 2. Run the Program

Make sure you have **Python 3** installed.

```bash
python3 diagnosis.py
```

---

## 📖 Usage

1. Register a patient (enter name, age, gender).
2. Enter symptoms one by one (type `done` when finished).
3. The system suggests possible diseases and prescriptions.

### Example:

```
=== Medical Diagnosis Expert System ===
Enter patient name: John
Enter patient age: 25
Enter patient gender (male/female/other): male

Enter symptoms one by one. Type 'done' when finished.
Available symptoms: fever, cough, fatigue, muscle_ache, runny_nose, sore_throat, sneezing, swollen_lymph_nodes, difficulty_swallowing, nausea, vomiting, diarrhea, abdominal_pain, itchy_eyes, rash
Symptom: fever
Symptom: cough
Symptom: done

Patient: John, Age: 25, Gender: male

Diagnosed Diseases (>=25% match):
 - flu: 2/4 symptoms (50.0%) → ['fever', 'cough']

Medications for flu:
  - Paracetamol: 500 mg every 6 hours for fever/pain. Do not exceed 4g daily.
  - Antihistamine: 10 mg daily. Avoid driving if drowsy.
```

---

## 📂 Project Structure

```
medical_expert_system/
│-- diagnosis.py   # Main expert system program
│-- README.md      # Project documentation
```

---

## 🔮 Future Improvements

* Store patient records in a **database (SQLite/CSV)**
* Add more diseases & medications
* Create a **web interface (Flask/FastAPI)**
* Build a **GUI version** with Tkinter/Streamlit

---

## 👨‍💻 Author

**Jossy Mesfin Yoseph**
🚀 Passionate about AI, Expert Systems, and Python Development

