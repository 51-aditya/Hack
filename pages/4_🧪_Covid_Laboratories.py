import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Testing laboratory information
labs_data = {
    "Laboratory": ["Lab A", "Lab B", "Lab C", "Lab D"],
    "Capacity": [100, 150, 120, 200],
    "Samples Received": [80, 120, 100, 150],
    "Processing Time (hours)": [6, 8, 10, 5]
}

# Convert data to a Pandas DataFrame
df_labs = pd.DataFrame(labs_data)

# Streamlit app
def main():
    st.title("COVID Testing Laboratories")

    st.subheader("Testing Laboratory Information:")
    st.dataframe(df_labs)

    st.write(" ")

    strategy = st.selectbox("Strategy Selection", ["Default", "Priority by Capacity", "Priority by Processing Time"])

    if strategy == "Priority by Capacity":
        df_labs_sorted = df_labs.sort_values(by="Capacity", ascending=False)
    elif strategy == "Priority by Processing Time":
        df_labs_sorted = df_labs.sort_values(by="Processing Time (hours)")
    else:
        df_labs_sorted = df_labs

    st.write(" ")

    st.subheader("Prioritized Laboratory List:")
    st.dataframe(df_labs_sorted)

    st.write(" ")

    st.subheader("Laboratory Processing Time Distribution:")
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Laboratory", y="Processing Time (hours)", data=df_labs_sorted)
    plt.title("Laboratory Processing Time Distribution")
    st.pyplot(plt)

if __name__ == "__main__":
    main()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
