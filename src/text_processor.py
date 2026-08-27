from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(transcript: str): # Convert transcript into LangChain documents and split them into smaller chunks.
    
    document = Document(
        page_content=transcript,
        metadata={
            "source": "youtube_transcript"
        }
    )

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

    chunks = splitter.split_documents([document])

    return chunks