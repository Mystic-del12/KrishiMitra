🌾 KrishiMitra AI
Multilingual Agricultural Decision-Support Agent
📖 Table of Contents

Overview

Problem Statement

Solution

Core Features

System Architecture

Tech Stack

Installation & Setup

Usage

Example Queries

Project Structure

Future Improvements

License

🔎 Overview

KrishiMitra AI is a goal-driven agricultural decision-support agent designed to help farmers make structured and data-informed crop-selling decisions.

The system dynamically detects crop intent from user queries, selectively invokes relevant tools (weather, market price, and government schemes), and generates actionable recommendations with reasoning and confidence levels — in the same language as the user.

🚩 Problem Statement

Small and marginal farmers often rely on fragmented and unstructured information sources:

Weather forecasts

Market (mandi) prices

Government schemes

The lack of unified, structured intelligence makes timely and optimal crop-selling decisions difficult, increasing financial risk and uncertainty.

💡 Solution

KrishiMitra AI integrates structured data tools with large language model reasoning to produce clear, explainable recommendations.

The system:

Detects crop and intent from the user query

Dynamically selects relevant tools

Injects structured data into the reasoning engine

Generates a structured recommendation

Stores interaction history in MongoDB

This transforms fragmented data into actionable agricultural intelligence.

🧠 Core Features

🔍 Crop Detection from Query

🛠 Dynamic Tool Routing

🌍 Multilingual Response Generation

📊 Structured Decision Output

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

⚙ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/KrishiMitra.git
cd KrishiMitra
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Configure Environment Variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here

Make sure MongoDB is running locally:

mongod
4️⃣ Run the Application
python main.py
▶ Usage

The agent accepts natural language agricultural queries via terminal input.

It generates structured responses including:

Recommendation

Reasoning

Confidence Level

All responses are automatically generated in the same language as the user’s query.

🧪 Example Queries

Should I sell wheat this week?

What is the current rice price?

क्या मुझे इस हफ्ते गेहूं बेचना चाहिए?

મારે આ અઠવાડિયે ઘઉં વેચવું જોઈએ?

📂 Project Structure
KrishiMitra/
│
├── main.py          # Core agent logic
├── tools.py         # Tool definitions (weather, price, schemes)
├── memory.py        # MongoDB persistence layer
├── requirements.txt
├── README.md
└── .gitignore

🚀 Future Improvements

Real-time agricultural API integration
Regional customization
Historical trend modeling
Web or mobile deployment
Advanced decision scoring models

📄 License

Developed for hackathon demonstration purposes.
