# College Assistant Chatbot

This project is a semantic chatbot that answers college-related questions using embeddings and vector similarity search. It retrieves the most relevant answer from a predefined FAQ dataset.

---

## Project Structure

```
college_chatbot/
│
├── data/
│   └── faqs.json
│
├── build_index.py
├── chatbot.py
├── app.py
├── requirements.txt
```

---

## Setup Instructions

### Create Virtual Environment

```
python -m venv env
```

### Activate Environment

Windows:

```
env\Scripts\activate
```

Linux / Mac:

```
source env/bin/activate
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Build Vector Index

```
python build_index.py
```

---

### Run Application

```
streamlit run app.py
```

---

## How It Works

* FAQ data is stored in a JSON file
* Questions are converted into embeddings using a pre-trained model
* Embeddings are indexed using FAISS
* User input is converted into an embedding
* The closest matching question is retrieved
* The corresponding answer is returned

---

## Technologies

* Python
* FAISS
* Sentence Transformers
* Streamlit
* NumPy

---

## Customization

Modify the FAQ dataset in:

```
data/faqs.json
```

After updating the file, rebuild the index:

```
python build_index.py
```

---

## Notes

* Initial run may take time due to model download
* Use Python 3.10 or 3.11 for better compatibility
* Ensure all dependencies are installed correctly

---

## Future Improvements

* Add fallback responses using language models
* Add voice input support
* Deploy the application online
* Extend to multiple institutions
* Add session-based chat history
"# task_23_03_2026" 
