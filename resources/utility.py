import random

class Utility:
    def random_amogus():
        return random.choice(['ඞ', 'ඞ්', 'ව', 'ධ', 'ඩ', 'ච', 'ඩ', 'ඬ', 'ඣ'])
    def check_for_words(words, content):
        if isinstance(words, str):
            words = [words]
        return any(word in content for word in words)

