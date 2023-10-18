import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai

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

# Sidebar Text and File Upload
st.sidebar.subheader('Upload Contact Cetre Data')
uploaded_file = st.sidebar.file_uploader("***************", type="csv")

# If file is uploaded, read and display bar charts
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Sidebar Chart 1
    if data.shape[1] >= 2:
        st.sidebar.subheader('RPC%')
        fig, ax = plt.subplots()
        ax.bar(data.iloc[:, 0], data.iloc[:, 1])
        ax.set_title('Promise% for last 6 months')
        st.sidebar.pyplot(fig)
    else:
        st.sidebar.write("File must have at least two columns to create a bar chart.")
    
    # Sidebar Chart 2
    if data.shape[1] >= 3:
        st.sidebar.subheader('Promise%')
        fig, ax = plt.subplots()
        ax.bar(data.iloc[:, 0], data.iloc[:, 2])
        ax.set_title('Promise% for last 6 months')
        st.sidebar.pyplot(fig)
    else:
        st.sidebar.write("File must have at least three columns to create the second bar chart.")
    
    # Sidebar Chart 3
    if data.shape[1] >= 4:
        st.sidebar.subheader('Kept%')
        fig, ax = plt.subplots()
        ax.bar(data.iloc[:, 0], data.iloc[:, 3])
        ax.set_title('Kept% for last 6 months')
        st.sidebar.pyplot(fig)
    else:
        st.sidebar.write("File must have at least three columns to create the second bar chart.")

else:
    st.sidebar.write("")


# Main Body
# st.title('Main Body Charts')
st.markdown("<h1 style='text-align: center; color: black;'>LEASE DIMENSION - GEN AI App</h1>", unsafe_allow_html=True)

# Upload CSV data for Main Body
uploaded_file_body = st.file_uploader("Upload the reasons data", type="csv")

# If files are uploaded, read and display charts
if uploaded_file_body is not None:
    data_body = pd.read_csv(uploaded_file_body)

    # 1st Row: 3 Pie Charts
    st.subheader('INTERACTION ANALYTICS SUMMARY')
    col1, col2, col3 = st.columns(3)

    with col1:
        fig, ax = plt.subplots()
        data_body.iloc[:, 1].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_title('Failed Transcription')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        data_body.iloc[:, 2].value_counts().plot(kind='pie', ax=ax)
        ax.set_title('Reasons for Delay')
        st.pyplot(fig)

    with col3:
        fig, ax = plt.subplots()
        data_body.iloc[:, 3].value_counts().plot(kind='pie', ax=ax)
        ax.set_title('Key Concerns')
        st.pyplot(fig)
    
    # Set up OpenAI API Key (Do this securely in your production environment)
    openai.api_key = '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'
    app()

 

    # 3rd Row: Additional Charts...
    # (Add additional charts code here...)

else:
    st.sidebar.write("")
    st.write("")

# Upload CSV data for Main Body
csv_path = "D:\LD\data2.csv"
Gen_AI_IP_data = pd.read_csv(csv_path)

if st.checkbox('Run GEN AI Engine and show sample trascribed data'):
       st.dataframe(Gen_AI_IP_data.sample(2))




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

