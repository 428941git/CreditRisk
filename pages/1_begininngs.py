import streamlit as st

st.set_page_config(
    page_title="Credit risk modelling", 
    layout="wide")
col_spanned, col_tab = st.columns([4, 2])

decileTypes = {
    "DTI": "debt_to_income",
    "Monthly income": "monthly_income",
    "Credit utilization": "credit_utilization"
}

tabSelection = st.segmented_control(
    "Select Metric",
    options=list(decileTypes.keys()),
    default="DTI",
    label_visibility="collapsed"
)
selTab = decileTypes[tabSelection]

with st.sidebar:
    st.header = "Variables"
    population_sample = st.number_input("Population", min_value=100, max_value=10000, value=1000, step=10)
    dti_ratio = st.number_input("DTI", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
    late_payments = st.number_input("Late payments", min_value=0, max_value=12, value=1, step=1)
    job_years = st.number_input("Job years", min_value=0, max_value=25, value=6, step=1)
    m_income = st.number_input("Monthly income", min_value=4000, max_value=16000, value = 5000, step=100)
    open_acc = st.number_input("Open accounts", min_value=1, max_value=10, value=6, step=1)
    rec_inquiries = st.number_input("Recent inquiries", min_value=0, max_value=5, value=0, step=1)
    cred_util = st.number_input("Credit utilization", min_value=0.0, max_value=1.0, value=0.5, step=0.01)


with col_spanned:
    st.plotly_chart() #here chart
    st.write() #here matrix with values


