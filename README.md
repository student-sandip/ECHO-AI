# 🤖 ECHO AI Assistant

<p align="center">

<img src="assets/echo-logo.png" width="180">

</p>

<h1 align="center">
ECHO AI Assistant
</h1>

<p align="center">

A Personal Offline AI Assistant Powered by Python + Ollama + Llama 3.2

</p>

<p align="center">

🚀 Fast • 🧠 Smart • 💾 Memory • 🔒 Offline • ⚡ Local AI

</p>

---

# 📖 About ECHO

ECHO is a fully offline personal AI assistant built entirely in Python.

Unlike cloud-based AI assistants, ECHO runs locally on your computer using Ollama and the Llama 3.2 Large Language Model.

The goal of this project is not only to create an AI chatbot but to build a real personal assistant capable of remembering users, understanding conversations, executing commands, controlling the computer, and eventually communicating through voice.

This project is being built step by step with clean architecture and production-ready code.

---

# 🎯 Vision

The long-term vision of ECHO is to become a complete AI operating system companion.

Instead of simply answering questions, ECHO will eventually be able to:

- Remember personal information
- Learn user preferences
- Control the computer
- Open applications
- Search the web
- Talk naturally
- Listen through voice
- Understand images
- Execute tasks
- Become an everyday AI assistant

---

# 🚀 Why I Built ECHO

Most AI assistants today depend on cloud APIs.

That means:

- Internet is required
- Monthly subscription
- Privacy concerns
- API limits
- Expensive usage

ECHO solves this by running completely offline.

Everything happens locally.

No API key.

No subscription.

No internet required for chatting.

---

# ✨ Current Features (v0.4)

## AI

- Local AI using Ollama
- Llama 3.2 integration
- Streaming responses
- Natural conversations
- Professional prompt system

---

## Memory

- Long-term memory
- Persistent memory
- JSON memory storage
- Chat history
- Automatic memory extraction
- Memory recall
- Forget memory
- Clear memory

---

## Architecture

- Modular codebase
- Separate AI engine
- Separate memory manager
- Separate extractor
- Prompt library
- Easy to scale

---

## User Experience

- Startup animation
- Loading screen
- Thinking indicator
- Streaming output
- Clean terminal UI

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Core Language |
| Ollama | Local AI Runtime |
| Llama 3.2 | Language Model |
| JSON | Persistent Storage |
| Git | Version Control |
| GitHub | Project Hosting |
| VS Code | Development |
| Windows Terminal | CLI |

---

# 📂 Project Structure

```text
Echo-AI/

brain/
│
├── ai.py
├── extractor.py
├── memory_manager.py
└── prompts.py

memory/
│
├── memory.py
├── chat_history.json
└── user_memory.json

echo.py

requirements.txt

README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/student-sandip/ECHO-AI.git
```

```bash
cd ECHO-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows CMD

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama.

After installation verify:

```bash
ollama --version
```

---

## Download Llama 3.2

```bash
ollama pull llama3.2
```

---

## Run ECHO

```bash
python echo.py
```

---

# 🧠 How ECHO Works

```
User

↓

echo.py

↓

brain.ai

↓

Memory Extractor

↓

Memory Manager

↓

Local Memory

↓

Ollama

↓

Llama 3.2

↓

Streaming Response

↓

User
```

---

# 📌 Development Journey

This project is being developed step by step.

Each version introduces a completely new feature while keeping the architecture clean and scalable.

The development started from a simple terminal chatbot and is gradually evolving into a complete personal AI assistant.
---

# 🚀 Development Journey

ECHO is not a project that was built in a single day.

Every version was carefully planned, developed, tested and improved.

The objective was not only to make an AI chatbot, but to learn software engineering, clean architecture, AI integration and scalable project design.

Below is the complete development timeline.

---

# 📌 Version 0.1

## 🎯 Goal

Create the very first working version of ECHO.

At this stage, the objective was simple:

> Build an AI assistant capable of talking with the user locally.

---

## ✅ Completed

- Python project setup
- VS Code configuration
- Git initialization
- GitHub repository
- Virtual Environment
- Ollama installation
- Llama 3.2 installation
- First successful AI response
- Basic terminal interface

---

## 📂 Project Structure

```text
Echo-AI/

echo.py
```

---

## Learned

During this version I learned:

- How Ollama works
- How local LLMs work
- Running AI completely offline
- Python virtual environments
- Git basics
- GitHub workflow

---

## Problems Faced

- Python package installation
- Virtual environment confusion
- Ollama PATH issue
- GitHub authentication
- Git author mismatch

Every issue was fixed before moving to the next version.

---

# 📌 Version 0.2

## 🎯 Goal

Improve the chatting experience.

Instead of waiting several seconds and printing the entire response at once, ECHO should stream the response just like ChatGPT.

---

## ✅ Completed

- Streaming response
- Generator based output
- Better terminal experience
- Reduced waiting feeling

---

## Before

```
Thinking...

(wait...)

Entire answer appears.
```

---

## After

```
Thinking...

Hello...

I am ECHO...

Nice to meet you...
```

The response now appears word by word (streaming), making conversations feel much more natural.

---

## Learned

- Python generators
- yield keyword
- Streaming APIs
- Better user experience

---

# 📌 Version 0.3

## 🎯 Goal

Give ECHO memory.

Instead of forgetting everything after closing the program, ECHO should remember important user information.

---

## Features Added

### Chat History

ECHO now remembers previous conversations.

---

### Persistent Memory

User information is stored permanently.

Example:

```
My name is Sandip.
```

Later...

```
Who am I?
```

ECHO remembers.

---

### JSON Storage

Created:

```
chat_history.json
```

Stores conversations.

Created:

```
user_memory.json
```

Stores long-term user information.

---

### Memory Functions

Created:

- remember()
- recall()
- forget()
- clear_memory()

---

## Learned

- JSON storage
- File handling
- Persistent memory
- Context handling

---

# 📌 Version 0.4

## 🎯 Goal

Transform ECHO from a small script into a professional AI project.

Instead of keeping everything inside one file, the project was redesigned using modular architecture.

---

## Major Refactoring

Old Structure

```text
echo.py
```

Everything existed inside one file.

---

New Structure

```text
brain/

memory/

echo.py
```

Each module now has its own responsibility.

---

## New Modules

### ai.py

Responsible for

- AI conversation
- Ollama communication
- Streaming responses

---

### extractor.py

Responsible for

- Extracting useful information
- Identifying personal facts
- Preparing memory objects

---

### memory_manager.py

Responsible for

- Saving memory
- Loading memory
- Forgetting memory
- Memory searching
- Memory summary

---

### prompts.py

Contains

- System prompt
- Memory extraction prompt
- AI behavior rules

---

### memory.py

Handles

- JSON files
- Chat history
- Long-term memory
- Utility functions

---

## New Features

- Automatic memory extraction
- Modular architecture
- Better maintainability
- Cleaner code
- Professional folder structure
- Easier future upgrades

---

## Memory Capabilities

Current memory can remember things like:

```
My name is Sandip.
```

```
My favorite language is Java.
```

```
My favorite color is Blue.
```

Later ECHO can recall them instantly.

---

## Streaming Improvements

Responses are streamed in real time.

This makes conversations feel much closer to modern AI assistants.

---

## User Experience Improvements

Added:

- Loading screen
- Thinking indicator
- Startup banner
- Professional terminal interface

---

## Code Quality

Compared to v0.1

- Smaller functions
- Better readability
- Better separation of concerns
- Easier debugging
- Easier maintenance
- Easier future development

---

# 📈 Progress Summary

| Version | Main Achievement |
|----------|------------------|
| v0.1 | First Working AI |
| v0.2 | Streaming Responses |
| v0.3 | Persistent Memory |
| v0.4 | Modular Architecture + Memory Engine |

---

# 🎯 Result After v0.4

At this point ECHO has evolved from a simple terminal chatbot into a structured AI assistant capable of:

- Running completely offline
- Remembering users
- Maintaining chat history
- Streaming responses
- Using modular architecture
- Preparing for future voice interaction
- Preparing for computer automation