"""
Interactive Q&A module.
This file contains the code to handle user interaction and queries.
"""

from rag_pipeline import initialize_rag_pipeline, run_rag_query

def start_interactive_session():
    """
    Start an interactive Q&A session with the RAG pipeline.
    """
    pipeline = initialize_rag_pipeline()
    
    print("Welcome to the Interactive Q&A system. Type 'exit' to quit.")
    
    while True:
        query = input("Enter your question: ")
        if query.lower() == "exit":
            print("Exiting session. Goodbye!")
            break
        answer = run_rag_query(pipeline, query)
        print("Answer:", answer)
