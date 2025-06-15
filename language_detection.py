from nltk.corpus import wordnet
import re
from nltk.stem import WordNetLemmatizer

stop_words = ['i',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 "you're",
 "you've",
 "you'll",
 "you'd",
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 "she's",
 'her',
 'hers',
 'herself',
 'it',
 "it's",
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 "that'll",
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'no',
 'nor',
 'not',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 's',
 't',
 'can',
 'will',
 'just',
 'don',
 "don't",
 'should',
 "should've",
 'now',
 'd',
 'll',
 'm',
 'o',
 're',
 've',
 'y',
 'ain',
 'aren',
 "aren't",
 'couldn',
 "couldn't",
 'didn',
 "didn't",
 'doesn',
 "doesn't",
 'hadn',
 "hadn't",
 'hasn',
 "hasn't",
 'haven',
 "haven't",
 'isn',
 "isn't",
 'ma',
 'mightn',
 "mightn't",
 'mustn',
 "mustn't",
 'needn',
 "needn't",
 'shan',
 "shan't",
 'shouldn',
 "shouldn't",
 'wasn',
 "wasn't",
 'weren',
 "weren't",
 'won',
 "won't",
 'wouldn',
 "wouldn't",
 "its",
  "whats",
  "im",
  "youre",
  "hes",
  "shes",
  "were",
  "theyre",
  "cant",
  "dont",
  "wont",
  "isnt",
  "arent",
  "wasnt",
  "werent",
  "couldnt",
  "shouldnt",
  "wouldnt",
  "ive",
  "youve",
  "weve",
  "theyve",
  "id",
  "youd",
  "lets",
  "thats",
  "theres",
  "heres",
  "ill",
  "hell",
  "shell",
  "mustnt",
  "mightnt",
  "shant",
  "neednt",
  "oclock",
  "cause",
  "gimme",
  "wanna",
  "gonna",
  "kinda",
  "sorta",
  "lemme",
  "aint",
  "dunno",
  "gotta",
  "yall"]
# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

#from english_words import get_english_words_set
#web2lowerset = get_english_words_set(['web2'], lower=True)

# Define the Unicode range for Hindi letters
HINDI_UNICODE_RANGE = (0x0900, 0x097F)

# Function to check if a given character is a Hindi letter
def is_hindi_letter(c):
    return ord(c) >= HINDI_UNICODE_RANGE[0] and ord(c) <= HINDI_UNICODE_RANGE[1]


# In[8]:



def en_hi_detection(text):
    text = re.sub(r'[^\w\s]', ' ', text)

    words = text.lower().strip().split()
    count_en = 0
    # Lemmatize words for all POS
    for word in words:
        for pos in [wordnet.NOUN, wordnet.VERB, wordnet.ADJ, wordnet.ADV]:
#         print(f"{word} ({pos}): {lemmatizer.lemmatize(word, pos)}")
            lem_word = lemmatizer.lemmatize(word, pos)
            if lem_word in wordnet.words():
                print("wordnet :",lem_word)
                count_en+=1
                break
            elif lem_word in stop_words:
                print("stop_words :",lem_word)
                count_en+=1
                break
    #print("total english words found :", count_en)
    #print("length of sentence :", len(words))
    #print(count_en/len(words)*100, "% english words found")
    
    
    count = 0
    # Check each word for Hindi letters and print the results
    for word in words:
        hindi_letters = []
        for c in word:
            if is_hindi_letter(c):
                hindi_letters.append(c)
        if hindi_letters:
            #print(f"Word '{word}' contains Hindi letters: {' '.join(hindi_letters)}")
            count+=1
        else:
            pass
            #print(f"Word '{word}' does not contain any Hindi letters.")
        
    #print(count/len(words)*100, "% Hindi words found")
    if count_en/len(words)*100>70:
        return "eng"
    elif count/len(words)*100>75:
        return "hi"
    else :
        return "unknown"

