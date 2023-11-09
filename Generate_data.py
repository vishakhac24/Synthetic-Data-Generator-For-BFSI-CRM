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
