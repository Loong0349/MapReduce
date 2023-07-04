import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
from alive_progress import alive_bar

# Set up NLTK resources
nltk.download('stopwords')

# Define the preprocessing functions
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    # Remove single alphabets, numbers, and symbols
    words = [word for word in words if re.match(r'^[a-zA-Z]{2,}$', word)]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Perform lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word, pos='v') for word in words]  # Specify 'v' for verb lemmatization
    
    return words

# Read the CSV file and preprocess the data
dataset_path = 'headline.csv'
data_by_year = {}

with open(dataset_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    total_rows = sum(1 for _ in reader)  # Get the total number of rows in the CSV
    file.seek(0)  # Reset the file pointer to start from the beginning
    next(reader)  # Skip the header row again
    
    with alive_bar(total_rows, title="Processing data") as bar:
        for row in reader:
            publish_date = row[0]
            year = publish_date[:4]
            headline = row[1]
            preprocessed_words = preprocess_text(headline)

            if year not in data_by_year:
                data_by_year[year] = []

            data_by_year[year].extend(preprocessed_words)
            bar()  # Update the progress bar

# Save the year and terms for each year in separate text files
output_folder = 'processed_headline'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for year, terms in data_by_year.items():
    output_file = os.path.join(output_folder, f"{year}.txt")
    with open(output_file, 'w') as file:
        file.write(' '.join(terms))
