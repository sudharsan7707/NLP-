(.venv) PS D:\nlp> python nlp7.py
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\sudharsan\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
Enter a tweet:  Students completed the machine learning assignment successfully.                 

Tokens:
['students', 'completed', 'the', 'machine', 'learning', 'assignment', 'successfully', '.']

Unigrams:
[('students',), ('completed',), ('the',), ('machine',), ('learning',), ('assignment',), ('successfully',), ('.',)]

Bigrams:
[('students', 'completed'), ('completed', 'the'), ('the', 'machine'), ('machine', 'learning'), ('learning', 'assignment'), ('assignment', 'successfully'), ('successfully', '.')]

Trigrams:
[('students', 'completed', 'the'), ('completed', 'the', 'machine'), ('the', 'machine', 'learning'), ('machine', 'learning', 'assignment'), ('learning', 'assignment', 'successfully'), ('assignment', 'successfully', '.')]

Word Frequencies:
students : 1
completed : 1
the : 1
machine : 1
learning : 1
assignment : 1
successfully : 1
. : 1

HMM Prediction (Sample)
AI -> NOUN
improves -> VERB
technology -> NOUN

Comparison
N-Gram Model  : Captures word sequence frequencies.
HMM Model     : Predicts grammatical tags for words.
