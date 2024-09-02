import streamlit as st

# Sidebar for quick navigation
st.sidebar.title("Skills")
st.sidebar.write("Here are some of the technical skills I have acquired:")
st.sidebar.write("- Python")
st.sidebar.write("- JavaScript")
st.sidebar.write("- SQL")
st.sidebar.write("- Git")
st.sidebar.write("- Software Testing")



# Initialize the session state if it's not already
if "show_gallery" not in st.session_state:
    st.session_state.show_gallery = False

def display_gallery():
    st.title("Certifications")
    st.image("cert1.png", use_column_width=True)
    st.image("cert2.jpg",  use_column_width=True)
    st.image("cert3.jpg",  use_column_width=True)
    st.image("cer4.png",  use_column_width=True)

col1, col2 = st.columns([1.5, 5])

image_path = "profile.jpg"

with col1:
    st.image(image_path, use_column_width=True)
    # Read the image file
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()

    # Create a download button
    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="profile.jpg",
        mime="image/jpeg"
    )

with col2:
    st.write("")
    st.write("")
    st.title("John Oscar Roble")

st.write("I am a passionate 4th-year BSIT student with a diverse interest in the tech field. I have chosen to focus my career on Quality Assurance (QA) testing, where I can leverage my technical skills and attention to detail. Currently, I am enhancing my expertise by pursuing the Google IT Automation with Python certification on Coursera, sponsored by the DTI x Google Career Certification Program. I am eager to learn new skills and apply my knowledge in a professional environment.")
st.divider()
choices = st.multiselect("What's your favorite programming language?", ["Java", "Python", "SQL", "Typescript"])

# Toggle button to show/hide the gallery
if st.session_state.show_gallery:
    if st.button("Hide ▵"):
        st.session_state.show_gallery = False
    display_gallery()
else:
    if st.button("Show Certificates ▿"):
        st.session_state.show_gallery = True
st.divider()
st.header("How do you find my website?")
feedback = st.text_area("Please provide your feedback here:")

if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.error("Please enter your feedback before submitting.")
