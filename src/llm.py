import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

load_dotenv()

def get_llm():
  
    HF_TOKEN = os.getenv("HF_TOKEN")

    if not HF_TOKEN:
        raise ValueError(
            "api  is missing. "
            "Please add it to your .env file."
        )

    llm = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-120b",
        task="text-generation",
        huggingfacehub_api_token=HF_TOKEN,
        max_new_tokens=512,
        temperature=0.2,
        do_sample=True
    )

    model = ChatHuggingFace(
        llm=llm
    )

    return model