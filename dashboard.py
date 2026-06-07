import streamlit as st
import pandas as pd

st.title("📊 Student Performance Analysis System")

df = pd.read_csv("data/students.csv")

df["Total"] = (
    df["Math"] +
    df["Science"] +
    df["English"] +
    df["Computer"]
)

df["Percentage"] = df["Total"] / 4

# Metrics
st.subheader("Quick Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    len(df)
)

col2.metric(
    "Average Percentage",
    round(df["Percentage"].mean(), 2)
)

col3.metric(
    "Highest Percentage",
    round(df["Percentage"].max(), 2)
)

st.subheader("Student Data")

st.dataframe(df)

st.subheader("Percentage Comparison")

st.bar_chart(
    df.set_index("Name")["Percentage"]
)

st.subheader("Subject Marks")

st.bar_chart(
    df.set_index("Name")[
        ["Math","Science","English","Computer"]
    ]
)

# searching student by name

student_name = st.text_input("Search Student")

if student_name:
    result = df[
        df["Name"].str.contains(
            student_name,
            case=False
        )
    ]

    st.dataframe(result)


    