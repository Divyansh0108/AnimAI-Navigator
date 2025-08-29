# 🍿 GetAnime | Anime Recommendation System

---

### 🚀 This is the demo for the project: **GetAnime**  
[🌐 Try it live here!](https://getanime.streamlit.app/)

---

### 📖 Want to know how it works?  
Read the full blog: [Building Your Very Own Anime Recommendation System 🎬🤖 (Medium)](https://medium.com/@divyanshpandey0108/building-your-very-own-anime-recommendation-system-6ec98298ef12)

---

> **Your AI-powered gateway to discovering perfect anime titles with just one click!** ✨

---

## 📝 Name of the Project

**GetAnime – Anime Recommendation System**

An interactive recommendation engine that brings together the latest GenAI techniques, retrieval-augmented pipelines, and production-ready architecture to help users explore and discover anime tailored to their preferences.

---

## 💡 What the Project Does

GetAnime takes any natural language anime prompt—such as “adventure with an underdog protagonist” or “sci-fi mecha set in space”—and, using semantic search and generative AI, returns curated anime recommendations.  
- It accepts open-ended queries, deciphers themes and genres using embeddings, finds relevant anime, and crafts user-friendly explanations.  
- Each recommendation not only names the anime but also summarizes it and provides a rationale for why it fits the user’s unique query.

---

## 🚀 Motive of the Project

- **Democratize Recommendations:** Make anime discovery as easy and enjoyable as possible for anyone—from seasoned fans to total newcomers 🎯.
- **Showcase AI in Action:** Highlight the power of retrieval-augmented generation (RAG) in a fun, accessible application ⚡.
- **Modern MLOps:** Demonstrate best practices for building, deploying, and monitoring scalable AI systems in production environments 🤖.
- **Open Source:** Provide an educational codebase for anyone interested in combining NLP, GenAI, and MLOps principles.

---

## 🔧 Tools Used

- **Python 3.11** 🐍: Core project scripting and pipeline logic.
- **Streamlit** 🌐: Instantly builds modern, interactive UIs for AI/ML prototypes.
- **LangChain** ⛓️: Orchestrates retrieval, vector search, prompt templates, and LLM calls.
- **Hugging Face Sentence Transformers** 🤗: Translates natural language into high-quality vector embeddings for semantic comparison.
- **ChromaDB / FAISS** 🗄️: Offers fast, robust similarity search over large sets of embeddings.
- **Groq LLM API** 🚀: Performs the final step—explains and recommends, using state-of-the-art natural language generation.
- **GCP VM** ☁️: Delivers reliable, scalable cloud compute for deployment.
- **Kubernetes (Minikube)** ⚡: Orchestrates scaling and reliability across containers.
- **Docker** 🐳: Ensures easily reproducible environments across development, CI/CD, and prod.
- **Grafana Cloud** 📊: Monitors system and app health, ensuring high uptime and fast bug-tracing.
- **dotenv, logging** 🛡️: Separates credentials for security and creates centralized, timestamped error logs.

---

## 📚 Dataset Used

- **Primary Data Source:**  
  `anime_with_synopsis.csv` — a rich dataset containing anime titles, genres, plot synopses, and potentially more user-centric fields.
- **Preprocessed Data:**  
  `processed_anime_data.csv`, created by combining and cleaning raw fields for increased context and completeness during retrieval and recommendation.
- **Origin:**  
  Data gathered from trusted platforms like Kaggle, MyAnimeList, Anilist, or through custom scraping scripts for comprehensive coverage.

---

## 🔍 Dataset Details

| Column           | Description                        |
|------------------|------------------------------------|
| Name             | Anime title (string)               |
| Genres           | All genres, comma separated        |
| Synopsis         | Brief summary/description          |
| ...              | Additional info (score, year, etc) |

- The cleaned dataset is optimized for semantic search—text fields are merged for better context awareness during embedding.

---

## 🌟 Findings

- **Embeddings Power the Search:**  
  Unlike simple genre tags or keyword matching, vector embeddings let GetAnime interpret *ideas*—such as "dark fantasy," "slow-burn romance," or "strong female lead"—and map them to the most relevant anime, even if those exact terms aren't in the data 🔎.
- **LLM-Enhanced Output:**  
  The use of structured, constrained LLM prompts ensures recommendations are accurate, concise, and include a justification 📢.
- **Hybrid System Robustness:**  
  By fusing retrieval (precision) with generation (depth and usability), recommendations are both relevant and richly explained.

---

## 🧠 Models Tested

- **Sentence Transformers:**  
  Various embeddings including `all-MiniLM-L6-v2`, evaluated for semantic precision and efficiency.
- **LLM Providers:**  
  Groq, OpenAI (GPT), and Gemini compared for fluency, factuality, and response time.
- **Vector Stores:**  
  FAISS and ChromaDB, benchmarked for retrieval speed and scalability.

---

## 🏆 Model Chosen

- **Embeddings:**  
  Sentence Transformers for their balance of speed, semantic accuracy, and support for a wide range of queries.
- **LLM:**  
  Groq LLM API for its seamless integration with LangChain and low-latency, cost-effective inference.
- **Vector DB:**  
  FAISS/ChromaDB for best-in-class performance in local, production-ready environments.

---

## 🤔 Why?

- **Best-of-Both-Worlds:**  
  Combining semantic retrieval and LLM reasoning gives users precise *and* engaging recommendations.
- **State-of-the-Art Stack:**  
  Uses the latest open-source libraries and frameworks, keeping the project modern, modular, and maintainable.
- **Production Ready:**  
  End-to-end containerization and orchestration allow this system to scale in real environments—on-prem, cloud, or hybrid setups.

---

## 🗄️ About the Data

- **Privacy:**  
  All data is anonymized, stripped of personal identifiers, and used solely for the improvement of recommendations.
- **Quality:**  
  Processed regularly for accuracy and the inclusion of new shows or metadata.

---

## 🖱️ Usability

- **Effortless Interface:**  
  The Streamlit UI offers instant, natural language searching—no need to know titles or genres in advance.
- **Engaging Explanations:**  
  Each recommendation comes with clear descriptions and reasons, making discovery both informative and fun.
- **Robust Feedback Design:**  
  Handles edge cases, missing data, and errors gracefully, with all issues logged for maintainers.

---

## ⚖️ License

[Apache 2.0](LICENSE)

This open-source license encourages contribution and reuse with clear attributions and minimal restrictions.

---

## 🔄 Expected Update Frequency

- **Regular Updates:**  
  Expect versions to drop when new anime seasons start, fresh data sets are available, or advances in language and vector models bring further improvements!

---

## 🏷️ Tags

Anime 💮 • Recommendation Engine 🍿 • Machine Learning 🧑‍💻 • LLM/GenAI 🤖 • Streamlit App ⚡ • MLOps ☁️

---

## 🏁 About This File

This README introduces **GetAnime**—a full-stack, GenAI-powered anime recommender that combines semantic search, prompt engineering, and modern deployment practices to provide an out-of-the-box exploration experience.  
**Try it live:** [🌐 https://getanime.streamlit.app/](https://getanime.streamlit.app/)

---

**Made with ❤️ by anime fans, for anime fans.**
