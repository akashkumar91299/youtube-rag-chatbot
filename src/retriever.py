def create_retriever(vector_store, k=4):
   
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k
        }
    )

    return retriever