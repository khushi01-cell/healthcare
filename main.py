"""
Healthcare Chatbot API

This module provides a FastAPI application for a healthcare chatbot that can:
- Handle appointment booking requests
- Manage available appointment slots
- Provide healthcare information and assistance
- Use AI-powered responses with fallback to rule-based responses

The chatbot integrates LangChain for AI capabilities and provides a REST API
endpoint for client applications to interact with the healthcare assistant.

Author: Healthcare Chatbot Team
Version: 1.0.0
"""

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.flow import chatbot_flow

app = FastAPI(
    title="Healthcare Chatbot API",
    description="A healthcare assistant chatbot with appointment booking capabilities",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    """
    Request model for chat messages.
    
    Attributes:
        message (str): The user's message to the chatbot
    """
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Handle chat requests from users.
    
    This endpoint processes user messages and returns appropriate responses
    from the healthcare chatbot. The chatbot can handle appointment booking,
    general healthcare queries, and provide information about clinic services.
    
    Args:
        request (ChatRequest): The chat request containing the user's message
        
    Returns:
        dict: A dictionary containing the chatbot's response
            Format: {"response": "chatbot_response_text"}
            
    Example:
        Request: {"message": "I want to book an appointment"}
        Response: {"response": "Sure! Please provide your preferred date and time..."}
    """
    response = chatbot_flow(request.message)
    return {"response": response}
