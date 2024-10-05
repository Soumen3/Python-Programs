import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Set up NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Preprocess user input
def preprocess_input(input_text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(input_text.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return filtered_tokens

# Define responses to specific queries
def get_response(query):
    if 'hello' in query:
        return 'Hi there!'
    elif 'time' in query:
        import datetime
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        return f"The current time is {current_time}."
    else:
        return "I'm sorry, I don't understand your query."

# Main loop
while True:
    user_input = input('User: ')
    preprocessed_input = preprocess_input(user_input)
    response = get_response(preprocessed_input)
    print('AI: ' + response)
