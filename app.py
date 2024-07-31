import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Set the page configuration
st.set_page_config(
    page_title="Defect Logger App",
    page_icon="🧊",
    # layout="wide",  # Set the layout to wide
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.goodfon.com/original/1920x1080/5/56/color-texture-bosch-colorful.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



# Title with Rainbow Transition Effect and Neon Glow
html_code = """
<div class="title-container">
  <h1 class="neon-text">
    Defect Logger
  </h1>
</div>

<style>
@keyframes rainbow-text-animation {
  0% { color: grey; }
  16.67% { color: black; }
  33.33% { color: grey; }
  50% { color: grey; }
  66.67% { color: white; }
  83.33% { color: white; }
  100% { color: grey; }
}

.title-container {
  text-align: center;
  margin: 1em 0;
  padding-bottom: 10px;
  border-bottom: 4  px solid #fcdee9; /* Magenta underline */
}

.neon-text {
  font-family: Arial, sans-serif;
  font-size: 4em;
  margin: 0;
  animation: rainbow-text-animation 5s infinite linear;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.8),
               0 0 10px rgba(0, 0, 0, 0.7),
               0 0 20px rgba(0, 0, 0, 0.6),
               0 0 40px rgba(0, 0, 0, 0.6),
               0 0 80px rgba(0, 0, 0, 0.6),
               0 0 90px rgba(0, 0, 0, 0.6),
               0 0 100px rgba(0, 0, 0, 0.6),
               0 0 150px rgba(0, 0, 0, 0.6);
}
</style>
"""

st.markdown(html_code, unsafe_allow_html=True)
st.divider()



st.markdown(
    """
    <style>
    .success-message {
        font-family: Arial, sans-serif;
        font-size: 24px;
        color: green;
        text-align: left;
    }
    .unsuccess-message {
        font-family: Arial, sans-serif;
        font-size: 24px;
        color: red;
        text-align: left;
    }
    .prompt-message {
        font-family: Arial, sans-serif;
        font-size: 24px;
        color: #333;
        text-align: center;
    }
    .success-message2 {
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: white;
        text-align: left;
    }
    .message-box {
        text-align: center;
        background-color: white;
        padding: 5px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-size: 24px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load the data from Excel sheets
defects_df = pd.read_excel('quality.xlsx', sheet_name='Defects')
part_no_df = pd.read_excel('quality.xlsx', sheet_name='Part No.')
reporting_area_df = pd.read_excel('quality.xlsx', sheet_name='Reporting Type')

st.sidebar.title("Defect and Production Logger")
date = st.sidebar.date_input('Select Date')
st.sidebar.divider()

# st.sidebar.header("Enter Output")
target_output = st.sidebar.number_input("Enter Target Output", 0,step = 1)
actual_output = st.sidebar.number_input("Enter Actual Output", 0,step = 1)

prod_df = pd.DataFrame({
    "date" : [date],
    "target_output" : [target_output],
    "actual_output" : [actual_output] 
})
st.sidebar.write("Following Output will be Appended",prod_df.set_index("date"))

prod_button = st.sidebar.button("Append Production Output to MySQL Server")
if prod_button:
    # Create a connection to the MySQL database
    # Replace 'username', 'password', 'localhost', 'database_name' with your actual credentials
    database_url = 'mysql+pymysql://root:123%40XXX@localhost/quality_db'
    engine = create_engine(database_url)

    # Append the DataFrame to the database table
    p_table_name = 'Production_output'
    try:
        prod_df.to_sql(p_table_name, con=engine, if_exists='append', index=False)
        st.sidebar.success("Data appended successfully. ✅")
    except:
        st.sidebar.error("⚠️ Error in Appending Production Output to MySQL Server, \nduplicate date entry fould.")
    
st.markdown('<p class="message-box">Enter Defects Data</p>', unsafe_allow_html=True)

col1 , col2 = st.columns(2)
with col1:
    component = st.selectbox("Select Component Type",["Component A","Component B","Component C"])
with col2:
    reporting_area = st.selectbox('Select Reporting Area', reporting_area_df['Reporting Type'].unique())

col3 , col4 = st.columns(2)

with col3:
# Select columns
    category = st.selectbox('Select Category', defects_df['Category'].unique()) 
with col4:
    sub_category = st.selectbox('Select Sub Category', defects_df[defects_df['Category'] == category]['Sub_Category'].unique())

col5 , col6 = st.columns(2)
with col5:
# Filter defects based on selected category and sub-category
    filtered_defects = defects_df[(defects_df['Category'] == category) & (defects_df['Sub_Category'] == sub_category)]
    defect = st.selectbox('Select Defect', filtered_defects['Defect'].unique())
with col6:
    part_no = st.selectbox('Select Part Number', part_no_df['Component Part No.'].unique())


# Input quantity
col7,col8 = st.columns(2)
with col7:
    quantity = st.number_input('Input Quantity', min_value=1, step=1)

st.divider()
st.markdown('<p class="message-box">Following Selection Made for Defect</p>', unsafe_allow_html=True)

with st.container(border=True):
    st.write(f'Selected Date: {date}')
    st.write(f'Selected Reporting Area: {reporting_area}')
    st.write(f'Selected Component: {component}')
    st.write(f'Selected Category: {category}')
    st.write(f'Selected Sub Category: {sub_category}')
    st.write(f'Selected Defect: {defect}')
    st.write(f'Selected Part Number: {part_no}')
    st.write(f'Input Quantity: {quantity}')

if st.button('Add selection into Dataframe to Append'):
    # Create a new DataFrame to store the user inputs
    new_entry = pd.DataFrame({
        'date': [date],
        'reporting_area': [reporting_area],
        'component': [component],
        'category': [category],
        'sub_category': [sub_category],
        'defect': [defect],
        'part_no': [part_no],
        'quantity': [quantity]
        
    })


    # Display the new entry
    st.write('New Entry:')
    st.write(new_entry)
    try:
        pd.read_csv("reported_defects.csv")
        new_entry.to_csv('reported_defects.csv', mode='a', header=False, index=False)
        st.success('Entry Submitted Successfully! ✅')
    except:
        new_entry.to_csv('reported_defects.csv', mode='a', index=False)
        st.success('Entry Submitted Successfully! ✅')

st.divider()
st.markdown('<p class="message-box">Check Entries</p>', unsafe_allow_html=True)
  
try:
    df = pd.read_csv("reported_defects.csv")
except:
    df = pd.DataFrame(columns= ["date","reporting_area","component","category","sub_category","defect","part_no","quantity"])
df.columns = ["date","reporting_area","component","category","sub_category","defect","part_no","quantity"]


if len(df)>0:
    if st.checkbox("Check to filter by Date"):
        da,dda,ddda = st.columns(3)
        with da:
            # Input date
            date_e = st.date_input('Select Date to filter')   
        df = df.sort_values(by='date', ascending=False)
        st.dataframe(df[df["date"] == str(date_e)])
    else:
        st.dataframe(df)
else:
    st.error("No entries yet! Please submit an entry first.")
# Drop entries
st.divider()

if len(df)>0:
    st.markdown('<p class="message-box">Drop Entries</p>', unsafe_allow_html=True)
    e,ee,eee = st.columns(3)
    with e:
        if st.checkbox("Check for Dropping Entries"):
            index_drop = st.number_input("Input Index No. to drop",0,len(df)-1,step = 1)
            if st.button('Delete Entries'):
                df.drop(index= index_drop,inplace = True)
                df = df.reset_index(drop= True)
                df.to_csv('reported_defects.csv',index = False)
                st.dataframe(df)

# Append Data Entries into SQL Server
with st.container(border=True):
    st.header("Append Data Entries into SQL Server")
    if len(df)>0:
        def_button = st.button("Append to MySQL Server")
        if def_button:
            # Create a connection to the MySQL database
            # Replace 'username', 'password', 'localhost', 'database_name' with your actual credentials
            database_url = 'mysql+pymysql://root:123%40XXX@localhost/quality_db'
            engine = create_engine(database_url)

            # Append the DataFrame to the database table
            table_name = 'quality_defects'
            df.to_sql(table_name, con=engine, if_exists='append', index=False)

            st.success("Data appended successfully. ✅")
            df = pd.DataFrame(columns=df.columns)
            df.to_csv('reported_defects.csv',index = False)

    else:
        st.error("No Data to Append")
