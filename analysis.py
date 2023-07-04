import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def read_word_count_files(folder_path):
    word_counts = {}
    for filename in os.listdir(folder_path):
        year = filename.split("_")[1].split(".")[0]
        with open(os.path.join(folder_path, filename), 'r') as file:
            word_counts[year] = {}
            for line in file:
                word, count = line.strip().split("\t")
                word_counts[year][word] = int(count)
    return word_counts

def generate_word_cloud(word_count, year):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_count)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"Word Cloud - {year}")
    plt.axis('off')
    plt.savefig(f"word_cloud_{year}.png")  # Save the word cloud as an image file
    plt.close()

# Folder path containing word count files
folder_path = 'Headline/output'

word_counts = read_word_count_files(folder_path)

for year, word_count in word_counts.items():
    print(f"Year: {year}")
    total_words = sum(word_count.values())
    unique_words = len(word_count)
    most_common_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10] # Sort words based on alphabetical order
    
    print(f"Total Words: {total_words}")
    print(f"Unique Words: {unique_words}")
    print("Most Common Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    print("-----------------------------")

# Generate word cloud for each year and save it as an image file
for year, word_count in word_counts.items():
    generate_word_cloud(word_count, year)
