from textblob import TextBlob
from collections import Counter
import re
from sklearn.feature_extraction.text import CountVectorizer

def analyze_sentiment(texts):
    """
    Analyzes the sentiment of the provided list of texts.

    Parameters:
    texts (list): A list of strings to analyze.

    Returns:
    list: A list of dictionaries containing polarity and subjectivity for each text.
    """
    results = []
    
    for text in texts:
        # Create a TextBlob object
        blob = TextBlob(text)

        # Get polarity and subjectivity
        sentiment = {
            'text': text,
            'polarity': blob.sentiment.polarity,       # Ranges from -1 (negative) to 1 (positive)
            'subjectivity': blob.sentiment.subjectivity  # Ranges from 0 (objective) to 1 (subjective)
        }
        results.append(sentiment)
    
    return results

def extract_keywords(texts, specific_words=None, top_n=10, ngram_range=(1, 2)):
    """
    Extracts the most common keywords or phrases from the provided list of texts,
    or counts the occurrences of specific words if provided.

    Parameters:
    texts (list): A list of strings to analyze.
    specific_words (list): A list of specific words to count.
    top_n (int): The number of top keywords or phrases to return.
    ngram_range (tuple): The range of n-values for different n-grams to be extracted.

    Returns:
    list: A list of tuples containing the keyword/phrase and its frequency.
    """
    # Join all texts into a single string
    all_text = ' '.join(texts)
    
    # Remove punctuation and split into words
    all_text = re.sub(r'[^\w\s]', '', all_text.lower())
    
    if specific_words:
        # Count specific words
        word_counts = {word: all_text.split().count(word) for word in specific_words}
        return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    else:
        # Use CountVectorizer to extract n-grams
        vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = vectorizer.fit_transform([all_text])
        
        # Sum the counts of each n-gram
        ngram_counts = X.toarray().sum(axis=0)
        
        # Get the n-grams and their counts
        ngrams = vectorizer.get_feature_names_out()
        ngram_freq = list(zip(ngrams, ngram_counts))
        
        # Sort by frequency and get the top n
        common_ngrams = sorted(ngram_freq, key=lambda x: x[1], reverse=True)[:top_n]
        
        return common_ngrams