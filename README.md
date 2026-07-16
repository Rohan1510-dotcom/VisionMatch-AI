# 👁️ VisionMatch AI

> AI-powered visual product search using **OpenAI CLIP**, **FAISS**, **FastAPI**, and **React**.

VisionMatch AI is an end-to-end visual search engine that allows users to upload an image of a fashion product and instantly discover visually similar products from a catalog of **44,000+ fashion items**.

The system leverages **OpenAI's CLIP model** to generate semantic image embeddings and **FAISS** for efficient vector similarity search, delivering fast and accurate recommendations.

---

## 📸 Demo

### Home Page

<img width="1913" height="868" alt="image" src="https://github.com/user-attachments/assets/e308f17b-e9d3-4de8-b01a-3fe63614da7a" />


### Search Results

<img width="1919" height="863" alt="image" src="https://github.com/user-attachments/assets/98faf4a8-10f7-490c-a14b-832f7884a4b7" />

<img width="1913" height="870" alt="image" src="https://github.com/user-attachments/assets/729781bf-af3f-44ea-b43a-79c0a10e141c" />



---

## 🚀 Features

- 📷 Upload any fashion product image
- 🧠 Generate semantic image embeddings using OpenAI CLIP
- ⚡ Perform ultra-fast similarity search using FAISS
- 👕 Search across **44,000+ fashion products**
- 🖼 Display visually similar products with images
- 📋 Show product metadata including:
  - Product Name
  - Category
  - Gender
  - Color
  - Season
  - Usage
- 🎨 Modern responsive React frontend
- 🔗 FastAPI REST API backend

---

# 🏗 System Architecture

```
                 User Upload
                      │
                      ▼
              React Frontend
                      │
                      ▼
           FastAPI REST API
                      │
                      ▼
           OpenAI CLIP Encoder
                      │
                      ▼
             Query Embedding
                      │
                      ▼
               FAISS Search
                      │
                      ▼
           Top Similar Products
                      │
                      ▼
          Product Metadata Lookup
                      │
                      ▼
          Display Search Results
```

---

# 🛠 Tech Stack

## Frontend

- React.js
- Vite
- CSS3

## Backend

- FastAPI
- Python

## AI & Machine Learning

- OpenAI CLIP
- PyTorch
- FAISS
- NumPy
- Pandas

## Dataset

- Fashion Product Dataset
- 44,000+ Images
- Product Metadata (styles.csv)

---

# 📂 Project Structure

```
VisionMatch-AI
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── routers/
│   │   ├── data/
│   │   └── uploads/
│   │
│   ├── dataset/
│   ├── embeddings/
│   ├── requirements.txt
│   └── main.py
│
└── README.md
```

---

# ⚙️ Workflow

### 1. Upload Image

The user uploads a fashion product image through the React interface.

↓

### 2. Generate Embedding

The backend uses OpenAI CLIP to convert the uploaded image into a 512-dimensional embedding vector.

↓

### 3. Similarity Search

The embedding is searched against **44,000 precomputed product embeddings** using FAISS.

↓

### 4. Metadata Retrieval

Matching product IDs are mapped to product metadata using `styles.csv`.

↓

### 5. Display Results

The frontend displays the top similar products along with their images and details.

---

# 📊 Dataset

Dataset contains:

- **44,000+ Fashion Product Images**
- Product Metadata
- Categories
- Colors
- Gender
- Season
- Usage

---

# 🧠 AI Pipeline

```
Input Image

↓

OpenAI CLIP

↓

Image Embedding

↓

FAISS Index

↓

Top K Similar Products

↓

Metadata Lookup

↓

Frontend Display
```

---

# ⚡ Performance

- Dataset Size: **44,000+ Products**
- Image Embeddings: **44,000 vectors**
- Search Engine: **FAISS**
- Approximate Search Time: **< 1 second** *(hardware dependent)*

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/VisionMatch-AI.git

cd VisionMatch-AI
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# API Endpoints

## Upload Image

```
POST /upload
```

Uploads an image to the backend.

---

## Search Similar Products

```
POST /search
```

Returns the top visually similar fashion products.

---

# Future Improvements

- User authentication
- Category filters
- Brand filters
- Cloud deployment
- Docker support
- Mobile application
- Recommendation history
- Hybrid image + text search

---

# Challenges Faced

- Managing a large-scale image dataset
- Generating embeddings for 44,000 products
- Integrating CLIP with FastAPI
- Building a scalable FAISS search pipeline
- Serving product images efficiently
- Connecting React frontend with FastAPI backend

---

# Key Learnings

Through this project I gained practical experience with:

- React.js
- FastAPI
- REST APIs
- OpenAI CLIP
- Image Embeddings
- Vector Databases
- FAISS
- Similarity Search
- Computer Vision
- AI-powered Recommendation Systems
- Git & GitHub

---

# Author

**Rohan Patil**

Computer Science Engineering (AI & Analytics)

GitHub:
https://github.com/Rohan1510-dotcom

LinkedIn:
*(Add your LinkedIn profile)*

---

# License

This project is intended for educational and portfolio purposes.
