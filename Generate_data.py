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