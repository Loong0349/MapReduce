import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
from alive_progress import alive_bar

# Download the required NLTK data (stopwords) if not already available
nltk.download('stopwords')

# Function to preprocess text data (lowercase, tokenization, removal of single alphabets, numbers, and stopwords, and lemmatization)
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()
    # Tokenize the text into individual words
    words = nltk.word_tokenize(text)

    # Remove single alphabets, numbers, and symbols from the words
    words = [word for word in words if re.match(r'^[a-zA-Z]{2,}$', word)]
    # Remove stopwords from the words (common words that do not carry much meaning)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Perform lemmatization on the words (reducing words to their base or root form)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word, pos='v') for word in words]  # Specify 'v' for verb lemmatization

    return words

# Path to the CSV dataset file containing publish_date and headline columns
dataset_path = 'headline.csv'

# Dictionary to store preprocessed data for each year
data_by_year = {}

# Open the CSV dataset file
with open(dataset_path, 'r') as file:
    # Create a CSV reader to read the data from the file
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    total_rows = sum(1 for _ in reader)  # Count the total number of rows (excluding the header)
    file.seek(0)  # Reset the file pointer to start from the beginning
    next(reader)  # Skip the header row again

    # Initialize an alive_bar to visualize the progress of data processing
    with alive_bar(total_rows, title="Processing data") as bar:
        # Loop through each row in the CSV file
        for row in reader:
            # Extract the year from the publish_date (assuming it is in the first column, and the first 4 characters represent the year)
            publish_date = row[0]
            year = publish_date[:4]
            # Extract the headline from the second column
            headline = row[1]
            # Preprocess the headline to obtain a list of preprocessed words
            preprocessed_words = preprocess_text(headline)

            # Check if the year exists as a key in the data_by_year dictionary, if not, create a new entry for it
            if year not in data_by_year:
                data_by_year[year] = []

            # Extend the list of preprocessed words for the corresponding year
            data_by_year[year].extend(preprocessed_words)

            # Update the progress bar
            bar()

# Output folder to store the processed headline files
output_folder = 'processed_headline'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each year and its corresponding preprocessed terms
for year, terms in data_by_year.items():
    # Create the output file path for the year
    output_file = os.path.join(output_folder, f"{year}.txt")
    # Open the output file in 'write' mode and write the preprocessed terms (words) into the file
    with open(output_file, 'w') as file:
        file.write(' '.join(terms))

