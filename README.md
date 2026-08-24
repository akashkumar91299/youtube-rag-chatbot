# YouTube RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about the content of a YouTube video.

The application takes a YouTube Video ID, fetches the video transcript, processes and splits the transcript into chunks, generates embeddings, stores the embeddings in a vector store, retrieves relevant context based on the user's query, and uses an LLM to generate an answer.

## Features

* YouTube transcript extraction
* Transcript text processing and chunking
* Text embedding generation
* Vector store for storing embeddings
* Similarity-based document retrieval
* Context-aware prompt generation
* LLM-based question answering
* Streamlit-based user interface
* Modular RAG pipeline

## RAG Pipeline

```text
YouTube Video ID
        ↓
Fetch Transcript
        ↓
Text Processing
        ↓
Text Splitting
        ↓
Generate Embeddings
        ↓
Store in Vector Store
        ↓
User Query
        ↓
Retrieve Relevant Chunks
        ↓
Build Prompt with Context
        ↓
LLM
        ↓
Generate Answer
```

## Project Structure

```text
youtube-rag-chatbot/
│
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── prompt.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── text_processor.py
│   ├── vector_store.py
│   └── youtube_loader.py
│
├── utils/
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── README.md
├── app.py
└── requirement.txt
```

## File Description

| File                | Description                              |
| ------------------- | ---------------------------------------- |
| `app.py`            | Streamlit application and user interface |
| `youtube_loader.py` | Fetches the YouTube video transcript     |
| `text_processor.py` | Processes and splits transcript text     |
| `embeddings.py`     | Handles embedding generation             |
| `vector_store.py`   | Creates and manages the vector store     |
| `retriever.py`      | Retrieves relevant transcript chunks     |
| `prompt.py`         | Defines the prompt used for the LLM      |
| `llm.py`            | Configures the language model            |
| `rag_pipeline.py`   | Connects the complete RAG workflow       |

## Technologies Used

* Python
* Streamlit
* LangChain
* Hugging Face
* YouTube Transcript API
* FAISS
* Sentence Transformers
* Large Language Model (LLM)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment on Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

## Environment Variables

Create a `.env` file in the root directory.

Use `.env.example` as a reference.

Add your required API key:

```env
HUGGINGFACEHUB_API_TOKEN=your_api_token
```

Do not upload `.env` or API keys to GitHub.

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a YouTube Video ID and ask questions about the video's content.

## Example Questions

You can ask questions such as:

```text
What is the main topic of this video?
```

```text
Explain the main concepts discussed in the video.
```

```text
What are the key points mentioned by the speaker?
```

The system retrieves relevant transcript content and provides it to the LLM as context for generating the answer.

## Current Version

### v1.0 — Basic RAG

This version implements a complete basic RAG pipeline:

* YouTube transcript retrieval
* Text processing
* Text chunking
* Embedding generation
* Vector storage
* Similarity-based retrieval
* Prompt construction
* LLM-based response generation

The current version focuses on building a functional end-to-end RAG system.

## Future Improvements

Advanced RAG techniques will be added in future versions, including:

* Improved chunking strategies
* Metadata-based retrieval
* Query transformation
* Query rewriting
* Reranking
* Hybrid search
* Context compression
* Retrieval evaluation
* Response evaluation
* Conversation memory

## Development Roadmap

```text
Basic RAG
    ↓
Improved Chunking
    ↓
Metadata & Better Retrieval
    ↓
Reranking
    ↓
Query Transformation
    ↓
Hybrid Search
    ↓
RAG Evaluation
    ↓
Advanced RAG
```

## Project Goal

The goal of this project is to build a practical YouTube-based RAG chatbot and progressively improve its retrieval and response quality by implementing advanced RAG techniques.

---

**Current Status:** Basic RAG implementation completed and working successfully.
