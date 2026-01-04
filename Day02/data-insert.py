from pymongo import MongoClient
from datetime import datetime

# === MongoDB connection ===
MONGO_URI = "mongodb://root:root@localhost:27017/?authSource=admin"
client = MongoClient(MONGO_URI)
db = client["health_system"]

# === Patients data ===
patients = [
    {"patient_id": "P1001", "name": "John Doe", "age": 45, "gender": "Male"},
    {"patient_id": "P1002", "name": "Sarah Khan", "age": 32, "gender": "Female"},
    {"patient_id": "P1003", "name": "Michael Brown", "age": 60, "gender": "Male"},
    {"patient_id": "P1004", "name": "Ayesha Rahman", "age": 28, "gender": "Female"},
    {"patient_id": "P1005", "name": "David Lee", "age": 50, "gender": "Male"},
    {"patient_id": "P1006", "name": "Fatima Noor", "age": 36, "gender": "Female"},
    {"patient_id": "P1007", "name": "Robert Miller", "age": 55, "gender": "Male"},
    {"patient_id": "P1008", "name": "Nusrat Jahan", "age": 41, "gender": "Female"},
    {"patient_id": "P1009", "name": "Daniel Kim", "age": 29, "gender": "Male"},
    {"patient_id": "P1010", "name": "Samira Ahmed", "age": 47, "gender": "Female"}
]

# === Appointments data ===
appointments = [
    {"patient_id": "P1001", "date": "2025-01-02", "doctor": "Dr. Smith", "department": "Cardiology", "status": "Confirmed"},
    {"patient_id": "P1002", "date": "2025-01-05", "doctor": "Dr. Ali", "department": "Dermatology", "status": "Pending"},
    {"patient_id": "P1003", "date": "2025-01-03", "doctor": "Dr. Williams", "department": "Orthopedics", "status": "Confirmed"},
    {"patient_id": "P1004", "date": "2025-01-04", "doctor": "Dr. Noor", "department": "Gynecology", "status": "Cancelled"},
    {"patient_id": "P1005", "date": "2025-01-06", "doctor": "Dr. Chen", "department": "Neurology", "status": "Confirmed"},
    {"patient_id": "P1006", "date": "2025-01-07", "doctor": "Dr. Patel", "department": "Endocrinology", "status": "Confirmed"},
    {"patient_id": "P1007", "date": "2025-01-08", "doctor": "Dr. Ahmed", "department": "Urology", "status": "Pending"},
    {"patient_id": "P1008", "date": "2025-01-09", "doctor": "Dr. Roy", "department": "ENT", "status": "Confirmed"},
    {"patient_id": "P1009", "date": "2025-01-10", "doctor": "Dr. Park", "department": "Psychiatry", "status": "Confirmed"},
    {"patient_id": "P1010", "date": "2025-01-11", "doctor": "Dr. Rahman", "department": "General Medicine", "status": "Pending"}
]

# === Prescriptions data ===
prescriptions = [
    {"patient_id": "P1001", "medicine": "Atorvastatin", "refill_status": "Available"},
    {"patient_id": "P1002", "medicine": "Cetirizine", "refill_status": "Not Available"},
    {"patient_id": "P1003", "medicine": "Ibuprofen", "refill_status": "Available"},
    {"patient_id": "P1004", "medicine": "Iron Supplements", "refill_status": "Available"},
    {"patient_id": "P1005", "medicine": "Metformin", "refill_status": "Pending"},
    {"patient_id": "P1006", "medicine": "Levothyroxine", "refill_status": "Available"},
    {"patient_id": "P1007", "medicine": "Tamsulosin", "refill_status": "Not Available"},
    {"patient_id": "P1008", "medicine": "Amoxicillin", "refill_status": "Available"},
    {"patient_id": "P1009", "medicine": "Sertraline", "refill_status": "Pending"},
    {"patient_id": "P1010", "medicine": "Paracetamol", "refill_status": "Available"}
]

# === Insurance data ===
insurance = [
    {"patient_id": "P1001", "provider": "HealthCare Plus", "eligibility": "Active"},
    {"patient_id": "P1002", "provider": "MediAssist", "eligibility": "Expired"},
    {"patient_id": "P1003", "provider": "LifeSecure", "eligibility": "Active"},
    {"patient_id": "P1004", "provider": "CareShield", "eligibility": "Pending"},
    {"patient_id": "P1005", "provider": "WellnessOne", "eligibility": "Active"},
    {"patient_id": "P1006", "provider": "PrimeHealth", "eligibility": "Active"},
    {"patient_id": "P1007", "provider": "SecureLife", "eligibility": "Expired"},
    {"patient_id": "P1008", "provider": "HealthFirst", "eligibility": "Active"},
    {"patient_id": "P1009", "provider": "MediCare Gold", "eligibility": "Pending"},
    {"patient_id": "P1010", "provider": "TotalCare", "eligibility": "Active"}
]

# === Insert data into collections ===
db.patients.insert_many(patients)
db.appointments.insert_many(appointments)
db.prescriptions.insert_many(prescriptions)
db.insurance.insert_many(insurance)

print("Health system data inserted successfully.")

