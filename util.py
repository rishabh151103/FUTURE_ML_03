import os
import uuid
from google.cloud import dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./dialogflow_creds.json"

PROJECT_ID = "customer-support-bot-ped9"

def detect_intent_texts(text, session_id=None, language_code="en"):
    session_client = dialogflow.SessionsClient()

    # Create new session if not passed
    if not session_id:
        session_id = str(uuid.uuid4())

    session = session_client.session_path(PROJECT_ID, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text
