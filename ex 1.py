import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

import sys

if not sys.stdin.isatty():
	
	text = sys.stdin.read().strip()
else:
	print("Enter text (finish with an empty line):")
	lines = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		if line.strip() == "":
			break
		lines.append(line)
	text = "\n".join(lines)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
sentences = []
for ln in lines:
	sents = sent_tokenize(ln)
	sentences.extend(sents)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("\nOriginal Text:")
print(text)

print("\nSentences:")
for i, sent in enumerate(sentences, start=1):
	tokens = word_tokenize(sent)
	stemmed_words = [stemmer.stem(word) for word in tokens]
	lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

	print(f"\nSentence {i}:")
	print(sent)
	print("Tokens:", tokens)
	print("Stemmed Tokens:", stemmed_words)
	print("Lemmatized Tokens:", lemmatized_words)
	print("Stemmed Sentence:", " ".join(stemmed_words))
	print("Lemmatized Sentence:", " ".join(lemmatized_words))

print("\nNotes:")
print("Sentence tokenization splits text into sentences; stemming/lemmatization is applied per token.")
