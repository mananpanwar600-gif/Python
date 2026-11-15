import streamlit as st

## basic element
st.title("Streamlit Intro")
st.write("This is where we learn about streamlit" \
" Welcome")

## Getting user input

name=st.text_input("What's your name?")

if name:
    st.write(f"Welcome, {name}! Ready to build something amazing")

## more interactive element

age=st.slider("Your age",0,100)
gender=st.radio("Gender",("Male","Female","Other"))
interest=st.selectbox("Interested in",("CV","ML","Both"))

if st.button("Create profile"):
    st.write(f"Name : {name}, Age : {age}, Gender : {gender}, Interest : {interest}")

# all_profile = []
# new_profile={"Name" : name, "Age" : age, "Gender" : gender, "Interest" : interest
# }

# all_profile.append(new_profile)

# if st.button("Submit"):
#     st.write(all_profile)## Stream lit re runs the whole page from top to bottom, all the variables gets initialized again hence use stream session state


if "profiles" not in st.session_state:
    st.session_state.profiles = []

new_profile={"Name" : name, "Age" : age, "Gender" : gender, "Interest" : interest
}

if st.button("Save and show profile"):
    st.session_state.profiles.append(new_profile)

    st.write("All profiles : ",st.session_state.profiles)