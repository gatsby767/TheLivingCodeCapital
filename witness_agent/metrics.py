import re

def humility_score(text):
    humility_keywords = ["I may be wrong", "I don't know", "uncertain", "open to correction", "not sure"]
    score = sum(1 for phrase in humility_keywords if phrase in text.lower())
    return score / len(humility_keywords)

def bias_confession_rate(text):
    bias_phrases = ["I have a bias", "this may be biased", "subjective", "limited perspective", "flawed assumption"]
    score = sum(1 for phrase in bias_phrases if phrase in text.lower())
    return score / len(bias_phrases)
