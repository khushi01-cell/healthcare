"""
Healthcare Chatbot Flow Module

This module contains the core logic for the healthcare chatbot, combining
AI-powered responses with rule-based fallback mechanisms. It handles user
interactions, appointment booking, and provides intelligent healthcare
assistance through LangChain integration.

The module implements a hybrid approach:
- Rule-based logic for critical functions (appointment booking)
- AI-powered responses for general healthcare queries
- Graceful fallback to predefined responses when AI is unavailable

Features:
- Appointment booking and slot management
- AI integration with OpenAI (with quota handling)
- Intelligent fallback responses
- Multi-provider appointment system support

Author: Healthcare Chatbot Team
Version: 1.0.0
"""

from .slots import get_available_slots, book_slot
from langchain.prompts import ChatPromptTemplate
import os

# Optional: Load environment variables from a .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is not installed, skip

# Try to use OpenAI, fallback to simple responses if not available
try:
    from langchain_openai import ChatOpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY:
        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.2)
        prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful healthcare assistant. If the user asks about booking or appointments, reply with instructions to book. Otherwise, answer their question politely.
            User: {user_message}
            Assistant:
            """
        )
        chain = prompt | llm
        USE_AI = True
        print("OpenAI configured successfully.")
    else:
        USE_AI = False
        print("No OpenAI API key found. Using fallback responses.")
except Exception as e:
    print(f"OpenAI setup failed: {e}")
    print("Using fallback responses instead.")
    USE_AI = False

def get_fallback_response(user_message: str) -> str:
    """
    Generate fallback responses when AI is not available.
    
    This function provides intelligent rule-based responses for common
    healthcare queries when the AI model is unavailable due to quota
    limits, API issues, or configuration problems.
    
    The function uses keyword matching to identify user intent and
    provides appropriate, helpful responses for healthcare-related
    inquiries.
    
    Args:
        user_message (str): The user's input message
        
    Returns:
        str: An appropriate response based on the detected intent
        
    Example:
        >>> get_fallback_response("Hello")
        "Hello! I'm your healthcare assistant. How can I help you today?"
        
        >>> get_fallback_response("What are your hours?")
        "Our clinic is open Monday to Friday, 9 AM to 5 PM."
    """
    user_message_lower = user_message.lower()
    
    # Common healthcare responses
    if any(word in user_message_lower for word in ["hello", "hi", "hey"]):
        return "Hello! I'm your healthcare assistant. How can I help you today?"
    
    elif any(word in user_message_lower for word in ["hours", "open", "time"]):
        return "Our clinic is open Monday to Friday, 9 AM to 5 PM."
    
    else:
        return "Thank you for your message. I'm here to help with appointment booking and general healthcare information. How can I assist you?"

def chatbot_flow(user_message: str) -> str:
    """
    Main chatbot function that processes user messages and returns appropriate responses.
    
    This function implements the core logic for the healthcare chatbot, handling
    different types of user interactions:
    
    1. Appointment Booking: Detects booking intent and shows available slots
    2. Slot Booking: Processes specific slot requests and books appointments
    3. General Queries: Uses AI or fallback responses for healthcare questions
    
    The function uses a hybrid approach combining rule-based logic for critical
    functions (appointment booking) with AI-powered responses for general queries.
    
    Args:
        user_message (str): The user's input message to process
        
    Returns:
        str: The chatbot's response to the user
        
    Example:
        >>> chatbot_flow("I want to book an appointment")
        "Sure! Please provide your preferred date and time (e.g., 2025-06-27 10:00).\nAvailable slots: 2025-06-27 10:00, 2025-06-27 11:00, ..."
        
        >>> chatbot_flow("2025-06-27 10:00")
        "Your appointment is booked for 2025-06-27 10:00."
        
        >>> chatbot_flow("Hello")
        "Hello! I'm your healthcare assistant. How can I help you today?"
    """
    user_message_lower = user_message.lower()
    slots = get_available_slots()

    # Booking logic - Handle appointment booking requests
    if "book" in user_message_lower or "appointment" in user_message_lower:
        if not slots:
            return "Sorry, there are no available slots at the moment."
        return (
            "Sure! Please provide your preferred date and time (e.g., 2025-06-27 10:00).\n"
            f"Available slots: {', '.join(slots)}"
        )
    
    # Slot booking logic - Process specific slot requests
    for slot in slots:
        if slot in user_message_lower:
            if book_slot(slot):
                return f"Your appointment is booked for {slot}."
            else:
                return "Sorry, that slot is no longer available."
    
    # General query handling - Use AI if available, otherwise fallback
    if USE_AI:
        try:
            response = chain.invoke({"user_message": user_message})
            return response.content.strip() if hasattr(response, 'content') else str(response).strip()
        except Exception as e:
            print(f"AI response failed: {e}")
            return get_fallback_response(user_message)
    else:
        return get_fallback_response(user_message)