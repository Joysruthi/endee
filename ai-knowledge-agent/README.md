# 🧠 Agentic Knowledge Assistant using Endee Vector Database

## 📌 Project Overview

This project implements an **Agentic AI Knowledge Assistant** built on top of the **Endee Vector Database**.
The system uses the dataset already provided inside the Endee repository to perform:

* Semantic Search
* Retrieval Augmented Generation (RAG)
* Agentic AI workflow

The assistant understands user queries, retrieves relevant information from the Endee dataset using vector search, and generates intelligent responses.

This project demonstrates practical usage of **Vector Databases + AI/ML applications**.

---

## 🎯 Objective

The goal of this project is to:

* Use Endee as the vector database
* Build an AI/ML application using the given dataset only
* Implement semantic retrieval and intelligent answering
* Demonstrate RAG and Agent-based reasoning

---

## 🚀 Features

✅ Semantic Search using embeddings
✅ Retrieval Augmented Generation (RAG)
✅ Agentic AI decision workflow
✅ Context-aware question answering
✅ Uses Endee optimized dataset
✅ Command-line AI assistant

---

## 🏗️ System Architecture

```
User Query
     ↓
Embedding Model
     ↓
Endee Vector Database
     ↓
Semantic Retrieval
     ↓
Context Builder
     ↓
LLM Response Generator
     ↓
Final Answer
```

---

## ⚙️ Tech Stack

* Python
* Endee Vector Database
* Sentence Transformers
* RAG Pipeline
* LLM API (OpenAI / Gemini / Local Model)

---

## 🧠 How Endee is Used

Endee acts as the **core vector database** in this project.

### Process

1. The provided Endee dataset is indexed as vectors.
2. User queries are converted into embeddings.
3. Endee performs similarity search.
4. Relevant dataset chunks are retrieved.
5. Retrieved context is passed to the language model.
6. AI generates accurate answers using RAG.

This demonstrates real-world vector search and knowledge retrieval.

---

## 📂 Project Structure

```
endee/
│
└── ai-knowledge-agent/
    ├── app.py
    ├── rag_agent.py
    ├── requirements.txt
    └── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Your Forked Repository

```
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee
```

---

### 2️⃣ Install Dependencies

```
pip install -r ai-knowledge-agent/requirements.txt
```

---

### 3️⃣ Run the Application

```
python ai-knowledge-agent/app.py
```

---

## 💬 Example Usage

```
Ask something: Explain machine learning concepts
```

Output:

```
AI Assistant:
Machine learning is a field of artificial intelligence that...
```

---

## 🤖 Agentic Workflow

The AI assistant behaves like an intelligent agent:

* Understands user intent
* Decides when to search the dataset
* Retrieves relevant knowledge
* Generates contextual answers

---

## 📸 Demo

(Add screenshot or sample output here)

---

## ✅ Mandatory Internship Requirements Covered

✔ Used Endee repository
✔ Forked official repository
✔ Used provided dataset only
✔ Implemented RAG workflow
✔ Demonstrated semantic search
✔ Added project inside Endee repo
✔ Included clear README documentation

---

## 👩‍💻 Author

Name: *Your Name*
Program: *Your Department / College*
Project: Endee Internship Submission

---

## 📜 License

This project is developed for educational purposes as part of the Endee Internship submission.
