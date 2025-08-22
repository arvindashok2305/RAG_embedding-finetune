import os
import chromadb
import ollama # Added for the live LLM call
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

if __name__ == "__main__":
    # Create a dummy PDF for demonstration if one doesn't exist
    if not os.path.exists(PDF_PATH):
        print(f"Creating a dummy PDF at: {PDF_PATH}")
        try:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,
                "The theory of general relativity was proposed by Albert Einstein. It describes gravity as a fundamental property of spacetime. "
                "Isaac Newton developed the laws of motion and universal gravitation, which were the dominant theories for centuries before Einstein. "
                "In biology, the mitochondrion is known as the powerhouse of the cell, responsible for generating most of the cell's supply of adenosine triphosphate (ATP)."
            )
            pdf.output(PDF_PATH)
        except ImportError:
            print("Please install `fpdf` (pip install fpdf) to create the dummy PDF.")
            exit()
    # Setup the RAG pipeline (this will take a moment)
    collection, embedding_model = setup_rag_pipeline(PDF_PATH)
    # Start the interactive Q&A loop
    print("\n--- Ollama and Qwen2-0.5B Ready! ---")
    print("Enter your questions. Type 'exit' to quit.")
    while True:
        user_question = input("\nYour Question: ")
        if user_question.lower() == 'exit':
            break
        answer = ask_question(user_question, collection, embedding_model)
        print("\nAnswer:")
        print(answer)
    print("\n--- Session Ended ---")

if __name__ == "__main__":
    # Create a dummy PDF for demonstration if one doesn't exist
    if not os.path.exists(PDF_PATH):
        print(f"Creating a dummy PDF at: {PDF_PATH}")
        try:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,
                "The theory of general relativity was proposed by Albert Einstein. It describes gravity as a fundamental property of spacetime. "
                "Isaac Newton developed the laws of motion and universal gravitation, which were the dominant theories for centuries before Einstein. "
                "In biology, the mitochondrion is known as the powerhouse of the cell, responsible for generating most of the cell's supply of adenosine triphosphate (ATP)."
            )
            pdf.output(PDF_PATH)
        except ImportError:
            print("Please install `fpdf` (pip install fpdf) to create the dummy PDF.")
            exit()
    # Setup the RAG pipeline (this will take a moment)
    collection, embedding_model = setup_rag_pipeline(PDF_PATH)
    # Start the interactive Q&A loop
    print("\n--- Ollama and Qwen2-0.5B Ready! ---")
    print("Enter your questions. Type 'exit' to quit.")
    while True:
        user_question = input("\nYour Question: ")
        if user_question.lower() == 'exit':
            break
        answer = ask_question(user_question, collection, embedding_model)
        print("\nAnswer:")
        print(answer)
    print("\n--- Session Ended ---")

if __name__ == "__main__":
    # Create a dummy PDF for demonstration if one doesn't exist
    if not os.path.exists(PDF_PATH):
        print(f"Creating a dummy PDF at: {PDF_PATH}")
        try:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,
                "The theory of general relativity was proposed by Albert Einstein. It describes gravity as a fundamental property of spacetime. "
                "Isaac Newton developed the laws of motion and universal gravitation, which were the dominant theories for centuries before Einstein. "
                "In biology, the mitochondrion is known as the powerhouse of the cell, responsible for generating most of the cell's supply of adenosine triphosphate (ATP)."
            )
            pdf.output(PDF_PATH)
        except ImportError:
            print("Please install `fpdf` (pip install fpdf) to create the dummy PDF.")
            exit()
    # Setup the RAG pipeline (this will take a moment)
    collection, embedding_model = setup_rag_pipeline(PDF_PATH)
    # Start the interactive Q&A loop
    print("\n--- Ollama and Qwen2-0.5B Ready! ---")
    print("Enter your questions. Type 'exit' to quit.")
    while True:
        user_question = input("\nYour Question: ")
        if user_question.lower() == 'exit':
            break
        answer = ask_question(user_question, collection, embedding_model)
        print("\nAnswer:")
        print(answer)
    print("\n--- Session Ended ---")
