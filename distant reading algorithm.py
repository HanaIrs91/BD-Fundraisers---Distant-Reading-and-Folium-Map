# Topic: distant reading of Bandcamp fundraisers (frequencies and correlations)/ statement analysis
# Author: Hana Arshid
# Date: 04/10/2024

import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from nltk import bigrams

# Download resources from nltk
nltk.download('punkt')
nltk.download('stopwords')

# Load the Excel file from the provided path
file_path = '/Users/hanairshaid/Desktop/Data analysis and visualisation py/Textual Data - BC Gaza Fundraisers.xlsx'
df = pd.read_excel(file_path)

# Extract the text column 
texts = df['Statements '].tolist()  

# Combine all the texts into a single string
combined_text = " ".join(texts)

# Tokenise the text
words = nltk.word_tokenize(combined_text)

# Convert to lowercase and remove punctuation
words = [word.lower() for word in words if word.isalpha()]  # Remove non-alphabetical tokens like punctuation

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count word frequencies
word_counts = Counter(filtered_words)

# Get the 20 most common words
most_common_words = word_counts.most_common(20)

# Visualization: Word Frequency Bar Chart
labels, values = zip(*most_common_words)
colors = ['#E8F5E9', '#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#43A047', '#388E3C', '#2E7D32', '#1B5E20']

plt.figure(figsize=(9, 5), dpi=300)  
bars = plt.bar(labels, values, color=colors[:len(labels)], edgecolor='black', alpha=0.8)

# Add title and labels 
plt.title('Top 20 Most Common Words', fontsize=14, fontname='Times New Roman', fontweight='bold', pad=20)
plt.xlabel('Words', fontsize=6, fontname='Times New Roman', fontweight='bold')
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')

# Rotate x-ticks 
plt.xticks(rotation=90, ha='center', fontsize=4, fontname='Times New Roman')

# Add gridlines to the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure y-ticks cover the full range, including the max value
plt.yticks(range(0, max(values) + 10, 10), fontsize=4, fontname='Times New Roman')  # Ensure it shows up to 50

# Use tight_layout() 
plt.tight_layout(pad=6.0)

# Save the word frequency chart
plt.savefig('word_frequency_chart_fixed.png', format='png', dpi=300)

# Show the word frequency chart
plt.show()

# Bigrams (Word Correlations) Analysis
bigrams_list = list(bigrams(filtered_words))
bigram_counts = Counter(bigrams_list)

# Get the 20 most common bigrams
most_common_bigrams = bigram_counts.most_common(20)

# Correct the extraction of bigram labels and values
bigram_labels = [f'{w1} {w2}' for (w1, w2), _ in most_common_bigrams]
bigram_values = [count for _, count in most_common_bigrams]

# Visualization: Bigram Frequency Bar Chart
plt.figure(figsize=(9, 5), dpi=300)  
bars = plt.bar(bigram_labels, bigram_values, color=colors[:len(bigram_labels)], edgecolor='black', alpha=0.8)

# Add title and labels 
plt.title('Top 20 Most Common Bigrams', fontsize=14, fontname='Times New Roman', fontweight='bold', pad=20)
plt.xlabel('Bigrams', fontsize=6, fontname='Times New Roman', fontweight='bold')
plt.ylabel('Frequency', fontsize=6, fontname='Times New Roman', fontweight='bold')

# Rotate x-ticks 
plt.xticks(rotation=45, ha='right', fontsize=4, fontname='Times New Roman')  # Changed to ha='right' for better alignment
plt.yticks(fontsize=4, fontname='Times New Roman')

# Add gridlines to the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Use tight_layout() 
plt.tight_layout(pad=6.0)

# Save the bigram frequency chart
plt.savefig('bigram_frequency_chart_fixed.png', format='png', dpi=300)

# Show the bigram frequency chart
plt.show()
