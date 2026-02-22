🌾 KrishiMitra AI
Multilingual Agricultural Decision Support Agent
📌 Overview

KrishiMitra AI is a goal-driven agricultural decision-support agent that helps farmers make structured, data-informed crop selling decisions.

The system dynamically detects crop intent, selectively invokes relevant tools (weather, market price, schemes), and generates actionable recommendations with reasoning and confidence levels — in the same language as the user.

🚩 Problem

Farmers often rely on fragmented information sources:

Weather forecasts

Mandi/market prices

Government schemes

This lack of unified intelligence makes timely and optimal crop-selling decisions difficult.

💡 Solution

KrishiMitra AI integrates structured data and LLM-based reasoning into a modular decision engine that:

Detects crop from user query

Dynamically routes relevant tools

Generates structured decision outputs

Automatically adapts to user language

Stores interaction history in MongoDB

🧠 Features

🔍 Crop Detection from Query

🛠 Dynamic Tool Routing

🌍 Multilingual Response Generation

📊 Structured Recommendation Format

🗄 MongoDB-Based Memory Persistence

⚙ Modular Python Architecture

🏗 System Architecture
User Query
      ↓
Intent & Crop Detection
      ↓
Tool Router
(Weather / Market / Schemes)
      ↓
Gemini Reasoning Engine
      ↓
Structured Recommendation
      ↓
MongoDB Memory Storage
🛠 Tech Stack

Python 3

Google Gemini API (models/gemini-2.5-flash)

MongoDB

PyMongo

python-dotenv

🚀 Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/KrishiMitra.git
cd KrishiMitra
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Configure Environment

Create a .env file:

GEMINI_API_KEY=your_api_key_here
4️⃣ Run Application
python main.py
🧪 Example Queries

Should I sell wheat this week?

What is the current rice price?

क्या मुझे इस हफ्ते गेहूं बेचना चाहिए?

મારે આ અઠવાડિયે ઘઉં વેચવું જોઈએ?

📈 Future Scope

Real-time agricultural APIs

Region-specific analytics

Trend forecasting

Mobile/web deployment

Reinforcement learning optimization

📄 License

This project was developed for hackathon demonstration purposes.
