import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

text = """
Artificial Intelligence is changing the world.
It helps doctors, students and businesses.
Many companies use AI to save time.
AI can automate repetitive tasks.
Technology is growing very fast.
"""

sentences = sent_tokenize(text)

# Print first 2 sentences as summary
print("SUMMARY:\n")
print(sentences[0])
print(sentences[1])
