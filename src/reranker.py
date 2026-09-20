from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(
        self,
        model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):
        self.model = CrossEncoder(model_name)
    def rerank(self,query,documents,top_k=4):
        if not documents:
            return []
        
        pairs  = [(query,document.page_content) for document in documents]
        
        scores = self.model.predict(pairs)
        
        documents_scored = list(zip(documents,scores))
        
        documents_scored.sort(key=lambda x: x[1],reverse=True)
        
        return [
            document
            for document,score in documents_scored[:top_k]
            ] 
        
        