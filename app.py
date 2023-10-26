import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai

# Default Path
DEFAULT_PATH = "D:/LD/"

# Your Streamlit App
def app():
    st.title('GEN AI App using OpenAI GPT-3.5')

    # # Text input
    # user_input = st.text_input("Type something here:")

    # # If user provides input, make API call
    # if user_input:
    #     # Make API call to OpenAI GPT-3.5
    #     response = openai.Completion.create(
    #       engine="text-davinci-003",
    #       prompt=user_input,
    #       max_tokens=50  # adjust as needed
    #     )

    #     # Extract and display model's response
    #     st.write(response.choices[0].text.strip())

# Creating sample data
data = pd.DataFrame({
    'x': np.linspace(1, 10, 100),
    'y': np.sin(np.linspace(1, 10, 100)),
    'z': np.cos(np.linspace(1, 10, 100))
})

# Sidebar
# Displaying an image in the sidebar
st.sidebar.image('logo.png', width = 5, caption='', use_column_width=True)

st.sidebar.title('EDA Charts')

# # Sidebar Text and File Upload
# st.sidebar.subheader('Upload Contact Centre Data')
# uploaded_file = st.sidebar.file_uploader("***************", type="csv")

# # If file is uploaded, read and display bar charts
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
    
#     # Sidebar Chart 1
#     if data.shape[1] >= 2:
#         st.sidebar.subheader('RPC%')
#         fig, ax = plt.subplots()
#         ax.bar(data.iloc[:, 0], data.iloc[:, 1])
#         ax.set_title('RPC% for last 6 months')
#         st.sidebar.pyplot(fig)
#     else:
#         st.sidebar.write("File must have at least two columns to create a bar chart.")
    
#     # Sidebar Chart 2
#     if data.shape[1] >= 3:
#         st.sidebar.subheader('Promise%')
#         fig, ax = plt.subplots()
#         ax.bar(data.iloc[:, 0], data.iloc[:, 2])
#         ax.set_title('Promise% for last 6 months')
#         st.sidebar.pyplot(fig)
#     else:
#         st.sidebar.write("File must have at least three columns to create the second bar chart.")
    
#     # Sidebar Chart 3
#     if data.shape[1] >= 4:
#         st.sidebar.subheader('Kept%')
#         fig, ax = plt.subplots()
#         ax.bar(data.iloc[:, 0], data.iloc[:, 3])
#         ax.set_title('Kept% for last 6 months')
#         st.sidebar.pyplot(fig)
#     else:
#         st.sidebar.write("File must have at least three columns to create the second bar chart.")

# else:
#     st.sidebar.write("")

##################
# Main Body
st.markdown("<h1 style='text-align: center; color: black;'>LEASE DIMENSION - GEN AI App</h1>", unsafe_allow_html=True)

# EDA Charts
st.subheader("Main KPI's")
EDA_data = pd.read_csv("data1.csv")
col1, col2, col3 = st.columns(3)

# Sidebar Chart 1
with col1:
    if EDA_data.shape[1] >= 2:
        st.sidebar.subheader('RPC%')
        fig, ax = plt.subplots()
        ax.bar(EDA_data.iloc[:, 0], EDA_data.iloc[:, 1])
        ax.set_title('RPC% for last 6 months')
        st.pyplot(fig)
    else:
        st.write("File must have at least two columns to create a bar chart.")

# Sidebar Chart 2
with col2:
    if EDA_data.shape[1] >= 3:
        st.sidebar.subheader('Promise%')
        fig, ax = plt.subplots()
        ax.bar(EDA_data.iloc[:, 0], EDA_data.iloc[:, 2])
        ax.set_title('Promise% for last 6 months')
        st.pyplot(fig)
    else:
        st.write("File must have at least three columns to create the second bar chart.")

# Sidebar Chart 3
with col3:
    if EDA_data.shape[1] >= 4:
        st.sidebar.subheader('Kept%')
        fig, ax = plt.subplots()
        ax.bar(EDA_data.iloc[:, 0], EDA_data.iloc[:, 3])
        ax.set_title('Kept% for last 6 months')
        st.pyplot(fig)
    else:
        st.write("File must have at least three columns to create the second bar chart.")



#############
st.write("")
st.write("")

st.subheader("GEN AI Engine")
Gen_AI_IP_data = pd.read_csv("data2.csv")

if st.checkbox('Run GEN AI Engine and show sample transcribed data'):
       st.image('work_flow.png', width = 5, caption='', use_column_width=True)
       st.write("Gen AI engine ran successfully to process 5000 transcribed file...")
       st.dataframe(Gen_AI_IP_data.sample(2))

#############
# Search for customer to generate summary
st.write("")
st.write("")

st.subheader("Customer summary data")

customer_AI_IP_data = pd.read_csv("cust_data.csv")
 
if st.checkbox('Run GEN AI Engine and show sample customer data'):
       st.dataframe(customer_AI_IP_data.sample(2))

st.subheader("Search by Customer ID")
search_cust_id = st.text_input("Enter ID to search:")
if st.button('Search'):
    filtered_cust_data = customer_AI_IP_data[customer_AI_IP_data['cust_id'] == search_cust_id]
    st.dataframe(filtered_cust_data)
else:
    st.write("Please enter an ID and click Search.")


# # Search for agent to generate summary
# agent_path = "D:\LD\agent_data.csv"
# agent_AI_IP_data = pd.read_csv(agent_path)

# if st.checkbox('Run GEN AI Engine and show sample agent data'):
#     st.dataframe(agent_AI_IP_data.sample(2))

# st.subheader("Search by Agent ID")
# search_agent_id = st.text_input("Enter ID to search:")
# if st.button('Search'):
#     filtered_agent_data = agent_AI_IP_data[agent_AI_IP_data['agent_id'] == search_agent_id]
#     st.dataframe(filtered_agent_data)
# else:
#     st.write("Please enter an ID and click Search.")

# #uploaded_file_body = pd.read_csv("D:\LD\data2.csv")

# # If the file is uploaded, read and process the data
# if uploaded_file_body is not None:
#     data_body = pd.read_csv(uploaded_file_body)

#     # Checkbox for displaying sample data
#     if st.checkbox('Show sample data (2 rows)'):
#         st.dataframe(data_body.sample(2))

#     # ... (rest of your main body code, like pie charts)
# else:
#     st.write("Please upload a CSV file.")