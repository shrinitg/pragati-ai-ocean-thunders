import json
import re
import requests

# Path to the JSON file
FILE_PATH = "/Users/shrinitgoyal/Desktop/engati/dummy/ocean-thunders-be/doctors_indian.json"

# Replace this with your actual POST endpoint
API_URL = "https://6815b45b32debfe95dbc2f3a.mockapi.io/api/arogyamitra/doctors"

# Regex to extract 6-digit Indian pincode
PINCODE_REGEX = re.compile(r"\b\d{6}\b")

def extract_pincode(address: str) -> str:
    match = PINCODE_REGEX.search(address)
    return match.group() if match else ""

def post_doctor_data():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        doctors = json.load(f)

    headers = {"Content-Type": "application/json"}
    for i, doctor in enumerate(doctors, 1):
        # Extract and update pincode from address
        address = doctor.get("address", "")
        extracted_pincode = extract_pincode(address)
        if extracted_pincode:
            doctor["pincode"] = extracted_pincode

        try:
            response = requests.post(API_URL, json=doctor, headers=headers)
            if response.status_code in (200, 201):
                print(f"[{i}] Successfully posted: {doctor['Name']}")
            else:
                print(f"[{i}] Failed to post: {doctor['Name']} | Status: {response.status_code} | Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"[{i}] Exception while posting: {doctor['Name']} | Error: {e}")

if __name__ == "__main__":
    post_doctor_data()
