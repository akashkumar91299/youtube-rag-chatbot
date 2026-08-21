from src.youtube_loader import fetch_transcript
from src.text_processor import create_chunks
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.prompt import get_rag_prompt
from src.llm import get_llm


class YouTubeRAG:

    def __init__(self):
        self.embeddings = get_embeddings()
        self.llm = get_llm()

        self.vector_store = None
        self.retriever = None

    def load_video(self, youtube_url: str):

        transcript = fetch_transcript(youtube_url)

        chunks = create_chunks(transcript)

        self.vector_store = create_vector_store( chunks, self.embeddings )

        self.retriever = create_retriever( self.vector_store, k=4)

        return { "transcript": transcript, "chunks": chunks,
        }

    def ask(self, question: str):
       
        if self.retriever is None:
            raise ValueError(
                "Please load a YouTube video first."
            )

        # Retrieve relevant chunks
        retrieved_docs = self.retriever.invoke( question)

        # Combine retrieved documents
        context = "\n\n".join(
            doc.page_content
            for doc in retrieved_docs
        )

        # Create prompt
        prompt = get_rag_prompt()

        formatted_prompt = prompt.format(
            context=context,
            question=question
        )

        # Generate answer
        response = self.llm.invoke(
            formatted_prompt
        )

        return {
            "answer": response.content,
            "sources": retrieved_docs,
        }