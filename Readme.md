
---

# PDF Reader Setup Guide

Follow these steps to set up and run the project locally.

---

## Step 1: Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*Note: On Windows, activate the environment using:*

```bash
.venv\Scripts\activate
```

---

## Step 2: Start the Database

Make sure Docker is installed and running, then execute:

```bash
docker compose -f docker-compose.db.yml up
```

This will start the database service defined in the Docker Compose file.

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Add your Large Language Model (LLM) API key and any other necessary variables to the `.env` file.

---

## Step 5: Run the Ingestion Pipeline

```bash
python3 Ingestion.py
```
Injestion Pipeline Activation: This command will ingest your PDF into the vectordb for semantic search.

*Note: Ingestion pipeline should be run only at first time. Make sure your virtual environment is activated and the database is running.*

---

## Step 6: Launch the Streamlit App

```bash
python -m streamlit run queryForm.py
```

This will start the Streamlit server and open the app in your default web browser.

Here you can query the pdf located inside directory

---

## Additional Tips

- Always activate your virtual environment before running commands.
- To stop the Docker containers, press `Ctrl + C` and then run `docker compose down` if needed.
- Keep your `.env` file secure and do not commit it to version control.

## Code Example
[![Watch the Loom video](assets/loom-thumbnail.png)](https://www.loom.com/share/3ddb9681adf74979add9005c59be8694?sid=dfe7e42e-998e-4789-a12d-99227b7e7af8)


---

This version improves clarity, fixes typos (e.g., "Injestion.py" → "Ingestion.py"), and standardizes formatting for better readability. Let me know if you want me to add more sections like troubleshooting or project overview!

---