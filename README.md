# 📰 News ETL Pipeline Using Airflow, Docker, and PostgreSQL (NeonDB)

## 📌 Overview
This project is an **ETL (Extract, Transform, Load) pipeline** that **automates** the process of fetching news data from **[NewsAPI](https://newsapi.org)**, transforming it into a structured format, and loading it into a **PostgreSQL cloud database ([NeonDB](https://neon.tech))**. The entire pipeline is orchestrated using **Apache Airflow**, deployed within a **Docker container**.

---

## 🛠 Technologies Used
- **Python** – For writing ETL scripts  
- **[NewsAPI](https://newsapi.org) (Open Source)** – For extracting news articles  
- **Pandas** – For transforming JSON data into structured tabular format  
- **PostgreSQL ([NeonDB](https://neon.tech), Open Source)** – For storing the transformed data  
- **Apache Airflow** – For scheduling and orchestrating ETL jobs  
- **Docker** – For containerizing the Airflow environment  
- **AWS EC2 (Optional)** – For deploying the solution in the cloud  

---

## 📂 Project Structure
```
news_etl/
     │── pycache/ # Python cache files (ignore)
     │── venv/ # Virtual environment (ignore)
     │── .gitignore # Git ignore file
     │── docker-compose.yaml # Docker setup for Airflow
     │── extract.py # Extracts news data from NewsAPI
     │── load.py # Loads structured data into NeonDB
     │── transform.py # Transforms JSON data into structured format
     │── automate.py # DAG definition for Airflow orchestration
     │── requirements.txt # Required Python libraries
     │── README.md # Project documentation
```

---

## 🚀 Step-by-Step Guide

### 1️⃣ Setting Up the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/news-etl-pipeline.git
   cd news-etl-pipeline
   ```

2. **Create a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

---

### 2️⃣ Extract: Getting News Data from [NewsAPI](https://newsapi.org)
📌 **File:** `extract.py`  
📌 **Goal:** Fetch live news data from **[NewsAPI](https://newsapi.org)** and store it as a JSON object.

✅ **Why?**  
- We need real-time news data for processing and analysis.  
- **[NewsAPI](https://newsapi.org)** provides an **open-source** API to fetch the latest news.

📌 **How it Works?**
- Makes an HTTP request to **[NewsAPI](https://newsapi.org)**
- Retrieves news articles in **JSON format**
- Returns the extracted data for further processing


### 3️⃣ Transform: Converting JSON to Structured Format
📌 **File:** `transform.py`  
📌 **Goal:** Convert **unstructured JSON** news data into a **structured DataFrame**.

✅ **Why?**  
- JSON format is **nested and unstructured**.  
- PostgreSQL requires data to be in **rows and columns**.

📌 **How it Works?**
- Extracts key fields: **source, author, title, description, URL, timestamp**
- Converts JSON into a **structured Pandas DataFrame**
- Returns the transformed data

### 4️⃣ Load: Storing Data into [NeonDB](https://neon.tech)
📌 **File:** `load.py`  
📌 **Goal:** Store the **structured DataFrame** into a **PostgreSQL cloud database ([NeonDB](https://neon.tech))**.

✅ **Why?**  
- Storing data in a **relational database** makes it easier to **query and analyze**.
- **[NeonDB](https://neon.tech)** is a **serverless PostgreSQL** service, reducing management overhead.

📌 **How it Works?**
- Establishes a connection to **[NeonDB](https://neon.tech)**  
- **Creates a table** if it doesn’t exist  
- **Inserts transformed news data** into the table
  
![image](https://github.com/user-attachments/assets/c55e7052-7639-4ab6-8447-e85b2b0222da)

![image](https://github.com/user-attachments/assets/a3c96894-8b4f-4cf9-87ec-3b8f9d6d91ce)

---

### 5️⃣ Orchestrate with Apache Airflow
📌 **File:** `automate.py`  
📌 **Goal:** Automate the ETL process using **Apache Airflow DAGs**.

✅ **Why Use Airflow?**  
- **Schedules** and **automates** ETL runs  
- **Manages dependencies** between tasks  
- Provides an **interactive UI** for monitoring

📌 **How it Works?**
- **Defines a DAG** (`news_etl_pipeline`)
- **Runs tasks sequentially**: **extract → transform → load**
- **Schedules** the pipeline **daily at 9 AM UTC**  

---
![image](https://github.com/user-attachments/assets/d05fab06-b969-47a9-a6d8-955ef0d49555)
![image](https://github.com/user-attachments/assets/fda93ef9-c2f0-43ae-99e0-f2ec374cbe5a)

---

## 6️⃣ Deploy Using Docker
📌 **Goal:** Run Airflow inside a **Docker container** for easy deployment.

✅ **Why Docker?**  
- **Isolates dependencies** and environment  
- **Easier deployment** across different machines  
- **Pre-configured Airflow setup**  

📌 **How to Run Airflow with Docker?**
1️⃣ **Start Airflow in Docker**
```bash
docker run -d -p 8080:8080 apache/airflow standalone
```
2️⃣ **Access Airflow UI**
```bash
http://localhost:8080
```
3️⃣ **Unpause DAG**
```bash
docker exec -it container_id airflow dags unpause news_etl_pipeline
```
4️⃣ **Trigger DAG**
```bash
docker exec -it container_id airflow dags trigger news_etl_pipeline
```

---

## 🚀 Conclusion
🎉 This project successfully **automates news data extraction, transformation, and storage** using **[NewsAPI](https://newsapi.org), Airflow, Docker, and [NeonDB](https://neon.tech)**.

📌 **Next Steps:**  
- **Add Data Visualization**
- **Implement Error Handling**
- **Scale with Cloud Deployment**

🔥 **Happy Coding!** 🚀
