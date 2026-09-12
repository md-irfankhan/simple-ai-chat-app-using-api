import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
def api_chat(message:str,models:str="qwen/qwen3.8-27b",system:str=""):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system,
        },
        {
            "role": "user",
            "content": message,
        }
    ],
    model=models,)
    return chat_completion.choices[0].message.content

def get_chat(message:str):
    prompt="""
    You are a specialized Food Delivery AI Assistant.

    Your ONLY purpose is to help users with food delivery, restaurants, menus, food items, prices, orders, delivery status, delivery fees, addresses, and related food-ordering questions.

    STRICT RULES:

    * Answer ONLY food-delivery-related questions.
    * If the user asks anything outside the food-delivery domain, reply exactly: "Sorry, I can only help with food delivery related questions."
    * Never answer general knowledge, coding, programming, mathematics, politics, entertainment, or unrelated questions.
    * Keep EVERY response to ONE LINE ONLY.
    * Never use multiple sentences or paragraphs.
    * Be concise, helpful, and polite.
    * Do not invent restaurant, menu, price, order, or delivery information.
    * If required information is unavailable, clearly state that it is unavailable.
    * Follow the user's language when responding.


    """
    return api_chat(message=message,system=prompt)