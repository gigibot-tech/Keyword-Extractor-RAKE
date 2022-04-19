from rake_nltk import Rake
def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    phrases = r.get_ranked_phrases()
    return phrases