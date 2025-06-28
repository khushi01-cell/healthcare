# Healthcare Chatbot

A modern healthcare chatbot built with FastAPI and LangChain that provides appointment booking capabilities and healthcare assistance.

## 🏥 Features

- **Appointment Booking**: Book and manage healthcare appointments
- **AI-Powered Responses**: Intelligent healthcare assistance using LangChain
- **Fallback System**: Rule-based responses when AI is unavailable
- **Multi-Provider Support**: Manage appointments for multiple healthcare providers
- **REST API**: Clean API interface for integration
- **Comprehensive Documentation**: Full docstrings and API documentation

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Installation

1. **Clone the repository** (if using git):
   ```bash
   git clone <repository-url>
   cd health_care
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (optional):
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

6. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API**:
   - API Documentation: http://127.0.0.1:8000/docs
   - Alternative Docs: http://127.0.0.1:8000/redoc

## 📖 Usage

### API Endpoint

**POST** `/chat`

Send a JSON request with your message:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "I want to book an appointment"}'
```

### Example Interactions

#### Booking an Appointment
```bash
# Request booking
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "I want to book an appointment"}'

# Response
{
  "response": "Sure! Please provide your preferred date and time (e.g., 2025-06-27 10:00).\nAvailable slots: 2025-06-27 10:00, 2025-06-27 11:00, 2025-06-27 11:30, 2025-06-27 14:00"
}
```

#### Confirming a Slot
```bash
# Book specific slot
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "2025-06-27 10:00"}'

# Response
{
  "response": "Your appointment is booked for 2025-06-27 10:00."
}
```

#### General Healthcare Queries
```bash
# Ask about clinic hours
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "What are your hours?"}'

# Response
{
  "response": "Our clinic is open Monday to Friday, 9 AM to 5 PM."
}
```

## 🏗️ Project Structure

```
health_care/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── chatbot/               # Chatbot package
│   ├── __init__.py        # Package initialization
│   ├── flow.py            # Main chatbot logic
│   └── slots.py           # Appointment slot management
└── venv/                  # Virtual environment (not in git)
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for AI-powered responses
- If not set, the chatbot will use fallback responses

### Customizing Available Slots

Edit `chatbot/slots.py` to modify available appointment slots:

```python
available_slots = {
    "doctor1": [
        "2025-06-27 10:00",
        "2025-06-27 11:00",
        # Add more slots as needed
    ],
    "doctor2": [
        # Add slots for additional providers
    ]
}
```

## 🤖 AI Integration

The chatbot uses a hybrid approach:

1. **Rule-based Logic**: For critical functions like appointment booking
2. **AI-Powered Responses**: For general healthcare queries using LangChain
3. **Fallback System**: Predefined responses when AI is unavailable

### Supported AI Models

- **OpenAI**: GPT models via LangChain (requires API key)
- **Ollama**: Local models (requires Ollama installation)
- **Fallback**: Rule-based responses when AI is unavailable

## 🧪 Testing

Test the chatbot using the interactive API documentation:

1. Start the server: `uvicorn main:app --reload`
2. Visit: http://127.0.0.1:8000/docs
3. Use the "Try it out" feature to test endpoints

## 📝 API Documentation

The API documentation is automatically generated and available at:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the API documentation
- Review the code comments and docstrings
- Open an issue on the repository

## 🔄 Version History

- **v1.0.0**: Initial release with appointment booking and AI integration 