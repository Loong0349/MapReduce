import os
from alive_progress import alive_bar

def word_count(input_file):
    word_counts = {}
    total_lines = sum(1 for line in open(input_file))

    with open(input_file, 'r') as file:
        with alive_bar(total_lines, title=input_file) as bar:
            for line_num, line in enumerate(file, 1):
                words = line.strip().split()
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

                bar()

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])  # Sort words based on alphabetical order

    return sorted_word_counts

def save_results_by_year(sorted_word_counts, year):
    output_file = f'results_{year}.txt'
    with open(output_file, 'a') as file:
        for word, count in sorted_word_counts:
            file.write(f'{word}: {count}\n')

if __name__ == '__main__':
    input_folder = 'processed_headline/'  # Input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            year = filename[:-4]  # Extract the year from the filename
            input_file = os.path.join(input_folder, filename)
            if os.path.isfile(input_file):
                sorted_word_counts = word_count(input_file)
                save_results_by_year(sorted_word_counts, year)
