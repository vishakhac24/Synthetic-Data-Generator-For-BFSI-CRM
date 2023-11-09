from faker import Faker
import random
import pandas as pd
import nltk
from nltk.corpus import words

fake = Faker('en_IN')  # Use Indian locale for names and addresses
nltk.download('words')

# Create an empty list to store generated data
data = []

# Number of records to generate
num_records = 1000

word_list = words.words()

# Define positive and negative feedback keywords
positive_keywords = ['Great', 'Excellent', 'Satisfied', 'Helpful']
negative_keywords = ['Poor', 'Unsatisfactory', 'Disappointed', 'Confusing']

# Create a function to generate feedback
def generate_feedback():
    return f"{random.choice(positive_keywords)}: {fake.sentence()}"

# Create a function to generate social media handles
def generate_social_media_handle(first_name, last_name):
    first_name_lower = first_name.lower()
    last_name_lower = last_name.lower()
    handle = f"{first_name_lower}_{last_name_lower}_{random.randint(10, 99)}"
    return handle

# Generate basic customer information
for _ in range(num_records):
    customer_id = fake.uuid4()
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(['Male', 'Female'])
    dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
    contact_number = fake.phone_number()
    address = fake.address()
    city = fake.city()
    state = fake.state()
    postal_code = fake.postcode()
    country = 'India'
