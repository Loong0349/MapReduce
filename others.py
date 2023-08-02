import os
from alive_progress import alive_bar

# Function to count the occurrences of each word in a given input file
def word_count(input_file):
    # Create a dictionary to store word counts
    word_counts = {}
    # Count the total number of lines in the input file
    total_lines = sum(1 for line in open(input_file))

    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Initialize an alive_bar to visualize the progress of the word counting process
        with alive_bar(total_lines, title=input_file) as bar:
            # Loop through each line in the input file, along with its line number (starting from 1)
            for line_num, line in enumerate(file, 1):
                # Split the line into individual words, removing leading/trailing whitespaces
                words = line.strip().split()
                # Loop through each word in the line and update the word_counts dictionary
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

                # Update the progress bar
                bar()

    # Sort the word_counts dictionary by word in alphabetical order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    # Return the sorted list of word counts
    return sorted_word_counts

# Function to save word counts for a specific year to an output file
def save_results_by_year(sorted_word_counts, year):
    # Generate the output file name based on the year
    output_file = f'results_{year}.txt'
    # Open the output file in 'append' mode to avoid overwriting existing data
    with open(output_file, 'a') as file:
        # Write each word and its count to the output file
        for word, count in sorted_word_counts:
            file.write(f'{word}: {count}\n')

if __name__ == '__main__':
    # Define the input folder where the processed headline files are located
    input_folder = 'processed_headline/'

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file has a '.txt' extension
        if filename.endswith('.txt'):
            # Extract the year from the filename (assuming the filename contains the year before '.txt')
            year = filename[:-4]
            # Create the full path to the input file
            input_file = os.path.join(input_folder, filename)
            # Check if the file is indeed a regular file (not a directory, etc.)
            if os.path.isfile(input_file):
                # Count the words in the input file and get the sorted word counts
                sorted_word_counts = word_count(input_file)
                # Save the word counts to an output file corresponding to the year
                save_results_by_year(sorted_word_counts, year)
