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

    # Generate customer email addresses
    def generate_email(first_name, last_name):
        email_provider = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'rediffmail.com.', 'icloud.com'])
        email = f"{first_name.lower()}.{last_name.lower()}@{email_provider}"
        return email
    
    # Generate transactional data
    transaction_id = fake.uuid4()
    transaction_date = fake.date_time_this_year()
    product = random.choice(['Savings Account', 'Credit Card', 'Personal Loan', 'Fixed Deposit'])
    purchase_amount = round(random.uniform(5000, 100000), 2)
    payment_method = random.choice(['Debit Card', 'Internet Banking', 'Cheque', 'UPI'])
    order_status = random.choice(['Pending', 'Completed', 'Cancelled'])

    # Generate financial data
    account_balance = round(random.uniform(1000, 50000), 2)
    credit_score = random.randint(300, 850)
    loan_amount = round(random.uniform(10000, 500000), 2)
    interest_rate = round(random.uniform(5, 15), 2)
    
    # Generate interaction history
    interaction_date = fake.date_time_this_month()
    interaction_type = random.choice(['Email', 'Call', 'Chat'])

    if interaction_type == 'Email':
        interaction_subject = f"Account Statement Request"
        notes = f"Customer inquiring about their recent transactions and account balance."
    elif interaction_type == 'Call':
        interaction_subject = f"Home Loan Inquiry"
        notes = f"Customer interested in getting information about home loan options."
    else:
        interaction_subject = f"Online Banking Help"
        notes = f"Customer needing assistance with online banking login issues."
        
    # Generate behavioral data
    website_visits = random.randint(1, 50)
    time_spent = random.randint(10, 180)
    
    # Generate social media interactions
    social_media_platform = random.choice(['Facebook', 'Twitter', 'Instagram'])
    post_comment_date = fake.date_time_this_month()
    sentiment = random.choice(['Positive', 'Negative', 'Neutral'])
    engagement_metrics = random.randint(0, 100)
    
    # Generate survey and feedback data
    survey_id = fake.uuid4()
    survey_responses = generate_feedback()
    feedback_date = fake.date_time_this_month()
    ratings = random.randint(1, 5)
    feedback_comments = generate_feedback()
    
    # Generate purchase frequency and patterns
    frequency_of_purchase = random.choice(['High', 'Medium', 'Low'])
    recurring_purchases = random.choice(['Yes', 'No'])
    seasonal_patterns = random.choice(['Spring', 'Summer', 'Fall', 'Winter'])
    
    # Generate customer segmentation data
    customer_segment = random.choice(['Segment A', 'Segment B', 'Segment C'])
    segment_preferences = generate_feedback()
    segment_behavior = generate_feedback()
    
    # Generate churn data
    churn_status = random.choice(['Churned', 'Active'])
    churn_date = fake.date_this_year() if churn_status == 'Churned' else None
    
    # Generate social media handle
    social_media_handle = generate_social_media_handle(first_name, last_name)
    
    # Append data to the list
    data.append([customer_id, first_name, last_name, gender, dob, contact_number, email, address, city, state, postal_code, country,
                 transaction_id, transaction_date, product, purchase_amount, payment_method, order_status,
                 account_balance, credit_score, loan_amount, interest_rate,
                 interaction_date, interaction_type, interaction_subject, notes,
                 website_visits, time_spent,
                 social_media_platform, post_comment_date, sentiment, engagement_metrics,
                 survey_id, survey_responses, feedback_date, ratings, feedback_comments,
                 frequency_of_purchase, recurring_purchases, seasonal_patterns,
                 customer_segment, segment_preferences, segment_behavior,
                 churn_status, churn_date,
                 social_media_handle])
    