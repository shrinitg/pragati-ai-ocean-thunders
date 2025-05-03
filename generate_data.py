import json
import random
from faker import Faker

# Use Indian locale
fake = Faker('en_IN')

# Load your existing JSON data
with open('doctors.json', 'r') as file:
    doctors = json.load(file)

# List of common Indian first and last names for realism
first_names = [
    'Amit', 'Priya', 'Raj', 'Sunita', 'Anil', 'Kavita', 'Rohit', 'Neha', 'Vikram', 'Pooja',
    'Arjun', 'Meena', 'Manish', 'Sneha', 'Karan', 'Divya', 'Rahul', 'Anita', 'Suresh', 'Ritu',
    'Sanjay', 'Swati', 'Ajay', 'Nisha', 'Deepak', 'Isha', 'Naveen', 'Rekha', 'Abhishek', 'Preeti',
    'Alok', 'Tanvi', 'Harish', 'Geeta', 'Rakesh', 'Simran', 'Tushar', 'Payal', 'Dev', 'Asha',
    'Gaurav', 'Bhavna', 'Mahesh', 'Lata', 'Yogesh', 'Juhi', 'Vikas', 'Radha', 'Naresh', 'Madhu'
]
last_names = [
    'Sharma', 'Patel', 'Reddy', 'Iyer', 'Gupta', 'Rao', 'Desai', 'Mehta', 'Jain', 'Nair',
    'Verma', 'Khanna', 'Prasad', 'Choudhury', 'Soni', 'Yadav', 'Bhat', 'Singh', 'Das', 'Kulkarni',
    'Agarwal', 'Dubey', 'Tiwari', 'Joshi', 'Pillai', 'Naidu', 'Bansal', 'Malhotra', 'Shah', 'Chandra',
    'Sahu', 'Menon', 'Bhattacharya', 'Bhardwaj', 'Kaur', 'Gupta', 'Thakur', 'Rawat', 'Kapoor', 'Bhargava',
    'Banerjee', 'Ghosh', 'Sreekumar', 'Chawla', 'Mehra', 'Solanki', 'Mathur', 'Khurana', 'Jadhav', 'Shetty'
]

# Update each doctor entry
for doc in doctors:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"

    doc["Name"] = full_name
    doc["Email"] = f"{first_name.lower()}.{last_name.lower()}@example.in"
    doc["address"] = fake.address().replace("\n", ", ")
    doc["pincode"] = str(fake.postcode())

# Save updated JSON
with open('doctors_indian.json', 'w') as file:
    json.dump(doctors, file, indent=2)

print("Updated data saved to doctors_indian.json")
