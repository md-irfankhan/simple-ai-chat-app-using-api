from fastapi import FastAPI,Body
from services.chats import get_chat
app=FastAPI()
@app.get('/')
def home():
    return "Hello"
@app.post('/chat')
def chat(message:str=Body(None)):
    if len(message)<0:
        return "You must input some text"
    return f"""
    you: {message}
    assistant:{get_chat(message=message)}
    """