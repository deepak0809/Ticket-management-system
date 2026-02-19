import streamlit as st
import pandas as pd
import os

FILE = "tickets.csv"

st.title("Mini Ticket Management System")

# Create file if not exist
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Name","Issue","Priority","Status"])
    df.to_csv(FILE,index=False)

# Load data
df = pd.read_csv(FILE)

st.subheader("Create Ticket")

name = st.text_input("Your Name")
issue = st.text_area("Describe Issue")
priority = st.selectbox("Priority",["Low","Medium","High"])

if st.button("Submit Ticket"):
    new_ticket = pd.DataFrame([[name,issue,priority,"Open"]],
                              columns=df.columns)
    df = pd.concat([df,new_ticket],ignore_index=True)
    df.to_csv(FILE,index=False)
    st.success("Ticket Created")

st.subheader("All Tickets")

for i,row in df.iterrows():
    st.write(row)

    status = st.selectbox(f"Update Status {i}",
                          ["Open","In Progress","Resolved"],
                          key=i)

    if st.button(f"Save {i}"):
        df.loc[i,"Status"] = status
        df.to_csv(FILE,index=False)
        st.success("Updated")
