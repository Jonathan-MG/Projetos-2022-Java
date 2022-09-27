import streamlit as st

st.title("Login")
user_email = st.text_input(label="Digite seu E-mail:")

user_password = st.text_input(label="Digite sua Senha:",
type="password")
    
if st.button(label="Login"):
    print(st.write(user_email),"\n",st.write(user_password))

# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

# # Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1,col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable text input widget", key="disabled")
#     st.radio(
#         "Set text input label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
#     )

# with col2:
#     text_input = st.text_input(
#         "Enter some text 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         placeholder=st.session_state.placeholder,
#     )

#     if text_input:
#         st.write("You entered: ", text_input)        