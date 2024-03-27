import streamlit as st
import random


prompts = {
    "feeling_tired": [
        "Are you getting enough sleep? Aim for 7-8 hours per night.",
        "Have you been drinking enough water? Dehydration can cause fatigue.",
        "Consider incorporating some light exercise into your routine."
    ],
    "headache": [
        "Try taking a pain reliever like ibuprofen or acetaminophen.",
        "Apply a cold compress to your forehead or temples.",
        "Relax in a quiet, dark room and avoid screens for a while.",
    ],
    "sore_throat": [
        "Gargle with warm salt water several times a day.",
        "Drink plenty of fluids to soothe your throat.",
        "Consider using a humidifier to add moisture to the air.",
    ],
     "stomach_pain": [
        "Avoid large meals, spicy foods, or foods that are difficult to digest.",
        "Consider eating smaller, more frequent meals throughout the day.",
        "Try over-the-counter antacids to alleviate indigestion or heartburn symptoms.",
        "Keep track of your food intake and symptoms to identify potential dietary triggers.",
        "Ensure you're adequately hydrated, as dehydration can worsen stomach pain.",
        "If stomach pain is severe or accompanied by other concerning symptoms, seek medical attention."
    ],
    "muscle_aches": [
        "Apply a warm compress or take a warm bath to relax tense muscles.",
        "Engage in gentle stretching exercises to improve flexibility and reduce muscle tension.",
        "Consider using over-the-counter topical analgesics or muscle rubs for localized pain relief.",
        "Ensure you're staying properly hydrated to prevent muscle cramps.",
        "Gradually increase physical activity to build strength and endurance, but avoid overexertion.",
        "If muscle aches persist despite home remedies, consult a healthcare provider."
    ]
}


st.title("Your AI Health Companion")

st.set_page_config(page_title="Your AI Health Companion", page_icon=None, layout='wide', initial_sidebar_state='auto', 
                   background='#f0f0f0')
user_concern = st.text_input("How are you feeling today?")

processed_concern = user_concern.lower().replace(" ", "_")


if processed_concern in prompts:
    # Display random response from the list
    response = random.choice(prompts[processed_concern])
    st.write(response)
else:
    st.write("I am still learning about various health concerns. Please consult a doctor for any serious issues.")


st.write("* This is a health app and does not replace professional medical advice. Always consult a doctor for any health concerns.")
