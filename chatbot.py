import os
from langchain_openai import ChatOpenAI

# OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Set up the LLM
llm = ChatOpenAI(temperature=0)

# Bias filter function
def is_biased(text):
    bias_keywords = ["gender", "religion", "caste", "race", "politics", "ethnicity", "nationality", "country"]
    return any(word in text.lower() for word in bias_keywords)

# Main chatbot loop
print("isunbiased_chatbot  (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    try:
        response = llm.predict(user_input)
        print(" Raw Response:", response)

        if is_biased(response):
            print(" Output blocked due to detected bias.")
        else:
            print("Bot:", response)

    except Exception as e:
        print("Error:", e)

