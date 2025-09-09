# Medical Diagnosis Expert System in Python

# Knowledge base: Symptoms associated with diseases
disease_symptoms = {
    "flu": ["fever", "cough", "fatigue", "muscle_ache"],
    "cold": ["runny_nose", "sore_throat", "cough", "sneezing"],
    "strep_throat": ["sore_throat", "fever", "swollen_lymph_nodes", "difficulty_swallowing"],
    "gastroenteritis": ["nausea", "vomiting", "diarrhea", "abdominal_pain"],
    "allergies": ["sneezing", "itchy_eyes", "runny_nose", "rash"]
}

# Knowledge base: Medications for diseases
medications = {
    "flu": [
        ("Paracetamol", "500 mg every 6 hours for fever/pain. Do not exceed 4g daily."),
        ("Antihistamine", "10 mg daily. Avoid driving if drowsy.")
    ],
    "cold": [
        ("Decongestant", "10 mg every 4-6 hours. Avoid if hypertensive."),
        ("Cough Syrup", "10 ml every 4 hours. Do not use more than 7 days.")
    ],
    "strep_throat": [
        ("Amoxicillin", "500 mg every 8 hours for 10 days. Complete full course.")
    ],
    "gastroenteritis": [
        ("Oral Rehydration Salts", "1 sachet in 1L water daily. Follow package instructions.")
    ],
    "allergies": [
        ("Cetirizine", "10 mg daily. Avoid alcohol to prevent drowsiness.")
    ]
}

# Register patient
def register_patient():
    name = input("Enter patient name: ").strip()
    age = input("Enter patient age: ").strip()
    gender = input("Enter patient gender (male/female/other): ").strip().lower()
    return {"name": name, "age": age, "gender": gender}

# Collect symptoms
def collect_symptoms():
    print("\nEnter symptoms one by one. Type 'done' when finished.")
    print("Available symptoms:", ", ".join(sorted({s for sym in disease_symptoms.values() for s in sym})))
    symptoms = []
    while True:
        s = input("Symptom: ").strip().lower()
        if s == "done":
            break
        if any(s in sym_list for sym_list in disease_symptoms.values()):
            symptoms.append(s)
        else:
            print("Invalid symptom. Try again.")
    return symptoms

# Diagnose diseases
def diagnose(symptoms):
    matches = {}
    for disease, sym_list in disease_symptoms.items():
        common = set(symptoms) & set(sym_list)
        if common:
            percentage = (len(common) / len(sym_list)) * 100
            if percentage >= 25:  # threshold
                matches[disease] = (common, percentage)
    return matches

# Best match if no disease passes threshold
def best_match(symptoms):
    best = {}
    max_match = 0
    for disease, sym_list in disease_symptoms.items():
        common = set(symptoms) & set(sym_list)
        if len(common) > max_match:
            max_match = len(common)
            best = {disease: (common, (len(common)/len(sym_list))*100)}
        elif len(common) == max_match and common:
            best[disease] = (common, (len(common)/len(sym_list))*100)
    return best

# Prescribe medications
def prescribe(diseases):
    for disease in diseases:
        print(f"\nMedications for {disease}:")
        if disease in medications:
            for med, dose in medications[disease]:
                print(f"  - {med}: {dose}")
        else:
            print("  No medications available.")

# Main program
def main():
    print("=== Medical Diagnosis Expert System ===")
    patient = register_patient()
    symptoms = collect_symptoms()

    print(f"\nPatient: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}")
    if not symptoms:
        print("No symptoms provided. Unable to diagnose.")
        return

    result = diagnose(symptoms)
    if result:
        print("\nDiagnosed Diseases (>=25% match):")
        for disease, (common, perc) in result.items():
            print(f" - {disease}: {len(common)}/{len(disease_symptoms[disease])} symptoms ({perc:.1f}%) → {list(common)}")
        prescribe(result.keys())
    else:
        print("\nNo diseases met the threshold. Best matches:")
        best = best_match(symptoms)
        if best:
            for disease, (common, perc) in best.items():
                print(f" - {disease}: {len(common)}/{len(disease_symptoms[disease])} symptoms ({perc:.1f}%) → {list(common)}")
            prescribe(best.keys())
        else:
            print("No possible matches.")

if __name__ == "__main__":
    main()
