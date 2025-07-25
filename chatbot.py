
from langchain.memory import ConversationBufferMemory
from sentiment import get_sentiment

memory = ConversationBufferMemory()

def generate_response(user_input):
    sentiment, _ = get_sentiment(user_input)
    memory.chat_memory.add_user_message(user_input)

    # Rule-based responses based on sentiment
    if sentiment == "NEGATIVE":
        response = "I'm really sorry to hear that. Want to talk more about it?"
    elif sentiment == "POSITIVE":
        response = "That's wonderful to hear! 😊"
    else:
        response = "I see. Tell me more."

    memory.chat_memory.add_ai_message(response)
    return response, sentiment
