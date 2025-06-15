from string import punctuation
import re

def text_cleaning(text):
    # Remove URLs starting with http, https and www, as well as quotes
    result = re.sub(r'http\S+|www\S+|\"', '', text)
    
    # Split the text into a list of words
    words = result.split()
    
    # Remove mentions and hashtags
    words = [word for word in words if not word.startswith(('@', '#'))]
    
    # Remove leading/trailing punctuation, and individual punctuation marks
    words = [word.strip(punctuation) for word in words if word not in punctuation]
    filtered_list = [item for item in words if item != '']
    # Remove words starting with digits
    words = [word for word in filtered_list if not word[0].isdigit()]
    
    # Convert all words to lowercase
    words = [w.lower() for w in words]
    
    return " ".join(words)
