import streamlit as st
from util import detect_intent_texts
import uuid

# ----------------- Streamlit Config -----------------
st.set_page_config(page_title="💬 Support Chatbot", page_icon="💬", layout="wide")

# ----------------- Session State Setup -----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# ----------------- Custom CSS Styling -----------------
st.markdown("""
<style>
    body, [data-testid="stAppViewContainer"] {
        background-color: #f4f8fb;
        font-family: 'Segoe UI', sans-serif;
    }
    .app-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1e3a5f;
        text-align: center;
        margin: 20px 0 30px 0;
    }
    [data-testid="stSidebar"] {
        background: #1e3a5f;
        color: white;
    }
    .sidebar-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: white;
    }
    .chat-box {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 20px;
        height: 500px;
        overflow-y: auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .chat-bubble {
        padding: 12px 18px;
        border-radius: 12px;
        margin-bottom: 16px;
        width: fit-content;
        max-width: 75%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        font-size: 1rem;
    }
    .user {
        background-color: #d2e9ff;
        color: #003a70;
        margin-left: auto;
        margin-right: 0;
        text-align: right;
    }
    .bot {
        background-color: #f0f0f0;
        color: #333;
        margin-right: auto;
        margin-left: 0;
        text-align: left;
    }
    .input-container {
        margin-top: 20px;
        background-color: #ffffff;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    input[type="text"] {
        background-color: #f9f9f9 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        color: #000 !important;
    }
    button[kind="secondary"] {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- Sidebar -----------------
st.sidebar.markdown("<div class='sidebar-title'>💡 Quick Options</div>", unsafe_allow_html=True)

QUICK_OPTIONS = [
    "Track my order", "Return an item", "Shipping info",
    "Payment methods", "Contact support", "Refund status",
    "Product availability"
]

for option in QUICK_OPTIONS:
    if st.sidebar.button(option):
        st.session_state.chat_history.append(("You", option))
        bot_reply = detect_intent_texts(option, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", bot_reply))

# ----------------- Title -----------------
st.markdown("<div class='app-title'>💬 Customer Support Chatbot</div>", unsafe_allow_html=True)

# ----------------- Chat Display -----------------
if st.session_state.chat_history:
    st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
    for sender, message in st.session_state.chat_history:
        role = "user" if sender == "You" else "bot"
        st.markdown(f"""
            <div class='chat-bubble {role}'>
                <strong>{'You' if role == 'user' else 'Bot'}:</strong><br>{message}
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)



# ----------------- Submit Function -----------------
def submit():
    user_msg = st.session_state.user_input.strip()
    if user_msg:
        st.session_state.chat_history.append(("You", user_msg))
        bot_response = detect_intent_texts(user_msg, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", bot_response))
        st.session_state.user_input = ""

# ----------------- Input Field -----------------
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
st.text_input(
    "Your message",
    key="user_input",
    placeholder="Type your message and press Enter...",
    label_visibility="collapsed",
    on_change=submit
)
st.markdown("</div>", unsafe_allow_html=True)









