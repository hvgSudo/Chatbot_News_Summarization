import streamlit as st
from streamlit_chat import message as st_message
import pickle
import json
import numpy as np
from tensorflow import keras

@st.experimental_singleton
def get_chatbot():
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    with open("intents.json") as file:
        data = json.load(file)
    
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    model = keras.models.load_model('chat_model')

    return tokenizer, data, lbl_encoder, model

if "history" not in st.session_state:
    st.session_state.history = []


st.title("Hello 'Big News' Morgans")

def generate_answer():
    tokenizer, data, lbl_encoder, model = get_chatbot()
    user_message = st.session_state.input_text
    max_len = 50

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_message]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            message_bot = np.random.choice(i['responses'])
    
    st.session_state.history.append({'message': user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

st.text_input("Talk to the bot", key = "input_text", on_change = generate_answer)

for chat in st.session_state.history:
    st_message(**chat)
