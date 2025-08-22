# ID of our fine-tuned model on the Hugging Face Hub
EMBEDDING_MODEL_ID = "arvindcreatrix/bge-baes-my-qna-model"
# The specific LLM we want to use for generation via Ollama
GENERATOR_MODEL_ID = "llama2"
# Path to the PDF file you want to ask questions about
PDF_PATH = "/content/sample_explain.pdf"
# ChromaDB settings
CHROMA_PATH = "./rag_chroma_db"
COLLECTION_NAME = "rag_collection"
# The instruction prefix required by the BGE embedding model
INSTRUCTION_PREFIX = "Represent this sentence for searching relevant passages: "

def load_and_split_pdf(file_path: str) -> list[str]:
    """Loads a PDF, extracts text, and splits it into chunks."""
    print(f"Loading and splitting document: {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found at: {file_path}")
    reader = PdfReader(file_path)
    text = "\n".join(page.extract_text() for page in reader.pages)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    print(f"Document split into {len(chunks)} chunks.")
    return chunks
def setup_rag_pipeline(pdf_path: str):
    """Sets up the entire RAG pipeline: embedding, chunking, and indexing."""
    print("--- Setting up RAG pipeline ---")
    # 1. Load and split the document
    chunks = load_and_split_pdf(pdf_path)
    # 2. Load the fine-tuned embedding model
    print(f"Loading embedding model: {EMBEDDING_MODEL_ID}")
    embedding_model = SentenceTransformer(EMBEDDING_MODEL_ID)
    # 3. Setup ChromaDB
    print(f"Setting up ChromaDB at: {CHROMA_PATH}")
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    # 4. Embed and index the chunks
    print(f"Embedding and indexing {len(chunks)} chunks...")
    chunk_ids = [str(i) for i in range(len(chunks))]
    collection.add(
        ids=chunk_ids,
        documents=chunks,
        embeddings=embedding_model.encode(chunks).tolist()
    )
    print("--- RAG pipeline setup complete! ---")
    return collection, embedding_model
def ask_question(question: str, collection, embedding_model):
    """Handles the retrieval and generation for a single question."""
    # 1. Embed the user's question
    instructed_query = INSTRUCTION_PREFIX + question
    query_embedding = embedding_model.encode(instructed_query).tolist()
    # 2. Retrieve relevant context from ChromaDB
    retrieved_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    retrieved_context = "\n\n---\n\n".join(retrieved_results['documents'][0])
    # 3. Construct the prompt for the LLM
    prompt = f"""
    Context:
    {retrieved_context}
    Question: {question}
    Based on the context provided, please answer the question. If the context does not contain the answer, state that.
    Answer:
    """
    # 4. Get the response from the LLM
    answer = get_llm_response(prompt)
    return answer

# ID of our fine-tuned model on the Hugging Face Hub
EMBEDDING_MODEL_ID = "BAAI/bge-base-en-v1.5"
# The specific LLM we want to use for generation via Ollama
GENERATOR_MODEL_ID = "llama2"
# Path to the PDF file you want to ask questions about
PDF_PATH = "/content/sample_explain.pdf"
# ChromaDB settings
CHROMA_PATH = "./rag_chroma_db"
COLLECTION_NAME = "rag_collection"
# The instruction prefix required by the BGE embedding model
INSTRUCTION_PREFIX = "Represent this sentence for searching relevant passages: "
