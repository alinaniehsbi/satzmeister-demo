import streamlit as st

 

st.set_page_config(

    page_title="SatzMeister",

    page_icon="🇩🇪"

)

 

st.title("🇩🇪 SatzMeister")

st.write("Lerne Deutsch mit Spaß!")

 

st.progress(0.3)

 

st.subheader("Lektion 1: Satzbau")

 

antwort = st.radio(

    "Welcher Satz ist richtig?",

    [

        "Ich heute lerne Deutsch.",

        "Ich lerne heute Deutsch.",

        "Ich Deutsch heute lerne."

    ],

    index=None

)

 

if st.button("Antwort überprüfen"):

    if antwort is None:

        st.warning("Bitte wähle eine Antwort aus.")

    elif antwort == "Ich lerne heute Deutsch.":

        st.success("Richtig! 🎉 +10 XP")

    else:

        st.error("Leider falsch!")

        st.info(

            "Im deutschen Hauptsatz steht "

            "das konjugierte Verb an zweiter Position."

        )

 

 
