# 🚀 Kayfa Labs — Agentic AI Diploma

A hands-on learning repository documenting my journey through the **Kayfa Academy – Agentic AI Diploma**.

This repository contains practical labs, weekly assignments, experiments, and mini-projects focused on understanding and building intelligent AI agents.

## 🎯 Learning Goals

- Understand Large Language Models (LLMs) and how they work.
- Learn the fundamentals of Agentic AI.
- Build AI agents using Python.
- Explore prompting techniques and system instructions.
- Understand reasoning, planning, memory, and decision-making.
- Learn how agents interact with external tools and APIs.
- Design and build practical AI-powered applications.

## 📚 Course Content & Progress

| Session | Topic | Status |
|---|---|---|
| Session 01 | Welcome to Agentic AI: Concepts, Use Cases & Your First Agent | 🟡 In Progress |
| Session 02 | Coming Soon | ⏳ Upcoming |
| Session 03 | Coming Soon | ⏳ Upcoming |

## 🧪 Practical Labs

### Session 01 — Your First AI Agent

**Task 1: Run & Personalize Your First Agent**

Objective:
Build and customize a conversational AI agent with a specific personality and purpose using a system prompt.

Implementation:
- Created a Python virtual environment.
- Integrated Google Gemini API.
- Configured environment variables using `.env`.
- Designed a custom system prompt for an Agentic AI Learning Coach.
- Added a welcome message.
- Implemented a message counter.
- Added clean conversation exit handling.
- Maintained conversation context between messages.

**Technologies:**
- Python
- Google Gemini API
- Google Gen AI SDK
- Python Dotenv

**Deliverables:**
- Modified Python agent implementation.
- Screenshot demonstrating the agent conversation.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini | LLM integration |
| Google Gen AI SDK | API communication |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and documentation |

## 📁 Repository Structure

```text
kayfa_Labs/
│
├── labs/
│   ├── session-01/
│   │   ├── first_agent.py
│   │   └── screenshots/
│   │
│   ├── session-02/
│   │
│   └── session-03/
│
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/basmaebraheim/kayfa_Labs.git
cd kayfa_Labs
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your `.env` file or expose your API key.

### 6. Run the first agent

```bash
python labs/session-01/first_agent.py
```

## 🔐 Security

- API keys are stored in environment variables.
- `.env` files must never be committed.
- Sensitive credentials must not appear in screenshots or source code.

## 📈 My Learning Philosophy

I believe the best way to understand AI is to build with it.

This repository is not just a collection of completed assignments; it is a record of experimentation, problem-solving, technical growth, and continuous learning.

**Learn → Build → Experiment → Improve**

---

⭐ Follow this repository to track my progress in the world of Agentic AI.

*Learning by building, one agent at a time.*