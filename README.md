# 🤖 AI Chatbot – Dialogflow + Streamlit

An intelligent customer support chatbot powered by **Dialogflow ES** and deployed using **Streamlit**. Built for quick integration and clean UI.

---

## 🖼️ Preview

**Chatbox Start:**

![Chatbox Start](images/chatbox%20start.png)

**Chatbox Conversation:**

![Chatbox Convo.png](images/chatbox%20convo.png)

---

## 📁 Project Structure

| Folder/File            | Description                                    |
|------------------------|------------------------------------------------|
| `.gitignore`           | Ignores unnecessary files (like credentials)   |
| `app.py`               | Main Streamlit app                             |
| `dialogflow_creds.json`| Dialogflow service account credentials (hidden)|
| `requirements.txt`     | Python dependencies                            |

---

## 🔧 Setup & Installation

```bash
# ===== Setup =====
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# (Optional) Virtual Environment
# Windows
python -m venv venv && venv\Scripts\activate
# macOS/Linux
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# Or manually:
pip install streamlit requests

# ===== Dialogflow Configuration =====

# 1. Create a Dialogflow ES Agent at:
#    https://dialogflow.cloud.google.com/

# 2. In Google Cloud Console:
#    - Enable Dialogflow API
#    - Create a Service Account with Dialogflow access
#    - Download the JSON key file

# 3. Rename the file to:
#    dialogflow_creds.json

# 4. Place it inside your project root directory

# ===== Important Notes =====

# ❗ Keep dialogflow_creds.json private
# ✅ Already listed in .gitignore
# 🔐 Never upload credentials publicly
# 🎯 Ensure intents are set properly in Dialogflow


streamlit run app.py
# Visit: http://localhost:8501


---

## ✅ Conclusion

This project demonstrates how easily you can integrate Dialogflow ES with a modern UI using Streamlit for responsive, smart chatbot interactions. It's a great base for customer support bots, feedback collectors, or virtual assistants.

Feel free to customize intents, enhance fallback handling, or deploy this bot publicly. Contributions are welcome!

Thanks for checking it out – happy coding! 🚀




