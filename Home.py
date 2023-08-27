import streamlit as st

st.set_page_config(
    page_title = "Resource Tracker",
)

st.title("Home")
st.sidebar.markdown(":black[Select one of the pages from above.]")

st.write(" ") 

st.write(
    "Resource Tracker is here to help you efficiently manage essential resources "
    "and get assistance quickly. Our platform connects individuals and "
    "governments to allocate resources where they're needed most. Together, "
    "we can make a difference!"
)

st.write(" ")

st.write(
    "Whether it's medical supplies, food distribution, or emergency services, "
    "our platform provides a user-friendly experience for real-time tracking "
    "and collaboration. Join us in building a stronger community!"
)

st.write(" ")

st.write("Click on the other tabs to know more about the website!")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #0c0080;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)