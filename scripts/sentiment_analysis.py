from textblob import TextBlob

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

# for result in sentiment_results:
#     print(f"Text: {result['text']}")
#     print(f"Polarity: {result['polarity']}, Subjectivity: {result['subjectivity']}\n")