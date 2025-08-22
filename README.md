📄 README.md
# RGA Embedding Project

This project implements a Retrieval-Augmented Generation (RAG) pipeline with PDF creation, helper functions, and an interactive Q&A system.  
It is modularized into separate files for better maintainability.

---

## 📂 Project Structure



src/
├── imports.py # Handles all library imports
├── config.py # Stores configuration values (API keys, paths, etc.)
├── helpers.py # Helper functions for common tasks
├── pdf_creation.py # Functions for generating PDFs
├── rag_pipeline.py # RAG pipeline initialization and execution
├── interactive_qa.py # Interactive Q&A session logic


---

## ⚙️ Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

---

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

---

Install dependencies:

pip install -r requirements.txt

---

🚀 Usage

1. Run Interactive Q&A
python src/interactive_qa.py

2. Generate PDFs
python src/pdf_creation.py

3. Customize Config

Set your API keys and paths in:

src/config.py

📌 Notes

Make sure to add your API keys in config.py before running.

You can expand the RAG pipeline inside rag_pipeline.py with embeddings, vector databases, and LLMs.

---
## 👨‍💻 Author

**Arvind A.**

* 🎓 B.E. CSE student from Anna University Regional Campus, Tirunelveli
* 💡 Machine Learning & AI Enthusiast | Aspiring AI/ML Engineer
* 📫 Reach me: [arvindashok2305@gmail.com](mailto:arvindashok2305@gmail.com)

---