import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Sample FAQ data
faq_data = {
    "What is Python?": "Python is a high-level, interpreted programming language.",
    "What are the main features of Python?": "Python is simple, easy to learn, and versatile.",
    "What is a variable in programming?": "A variable is a storage location associated with a value.",
    "How to define a function in Python?": "You can define a function using the 'def' keyword in Python.",
    "What is a loop in programming?": "A loop is a control structure that repeats a block of code until a certain condition is met."
}

# Initialize NLTK components
nltk.download('punkt')
nltk.download('stopwords')
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercase conversion
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum()]  # Stemming
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    return tokens

# Function to generate response
def generate_response(user_query):
    tokens = preprocess(user_query)
    for question, answer in faq_data.items():
        if all(token in preprocess(question) for token in tokens):
            return answer
    return "Sorry, I don't understand your question."

# Test the chatbot
user_query = input("Ask me a question: ")
response = generate_response(user_query)
print(response)
