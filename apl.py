import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import joblib

def main():
    st.title('Loan Defaulters Prediction')
    filename = 'Adaboost.pkl'
    loaded_model = joblib.load(filename)
    col1, col2 = st.columns(2)
    with col1:
            Income = st.number_input("Income", min_value=30000, max_value=149994)

            Savings= st.number_input("Savings", min_value=648, max_value=447608)
            Home_Ownership = st.selectbox("Home_Ownership", ['Rent', 'Own Home', 'Mortage'])
            if Home_Ownership == 'Mortage':
                Home_Ownership = 0
            elif Home_Ownership == 'Own Home':
                Home_Ownership = 1
            else:
                 Home_Ownership =2

            Credit_history = st.number_input("Credit_history", min_value=1, max_value=19)

            Open_accounts = st.number_input("Open_accounts", min_value=1, max_value=12)

            Credit_cards = st.number_input("Credit_cards", min_value=0, max_value=4)

            Overdraft = st.number_input("Overdraft", min_value=0, max_value=4)

            
    with col2:
 
            Student_Loan = st.selectbox("Student_Loan", ["No", "Yes"])
            if Student_Loan == "No":
                Student_Loan = 0
            else:
                Student_Loan = 1

            Non_performing_Accs = st.number_input("Non_performing_Accs", min_value=0, max_value=16)

            Open_Accounts = st.number_input("Open_Accounts", min_value=0, max_value=3)

            Current_In_Arrears = st.number_input("Current_In_Arrears", min_value=0, max_value=3)

            Current_balance_Amt = st.number_input("Current_balance_Amt", min_value=9000, max_value=29900)
            
            Past_due_Amt = st.number_input("Past_due_Amt", min_value=0.0, max_value=20930.0)

            Grade = st.selectbox("Grade", ['GG', 'AA', 'FF', 'BB', 'CC','EE','DD'])
            if Grade == 'AA':
                Grade = 0
            elif Grade == 'BB':
                Grade = 1
            elif Grade == 'CC':
                Grade = 2
            elif Grade== 'DD':
                Grade = 3
            elif Grade == 'EE':
                Grade = 4
            elif Grade== 'FF':
                Grade = 5
            else:
                Grade = 6

            



    input_dict = { 'Income':Income, 'Savings':Savings, 'Home_ownership':Home_Ownership, 'Credit_history':Credit_history,
       'Open_accounts':Open_accounts, 'Credit_cards':Credit_cards, 'Overdraft':Overdraft, 'Student_Loan':Student_Loan,
       'Non_perfoming_Accs':Non_performing_Accs, 'Open_Accounts':Open_Accounts, 'Current_In_Arrears':Current_In_Arrears,
       'Current_balance_Amt':Current_balance_Amt, 'Past_due_Amt':Past_due_Amt, 'Grade':Grade}
    input_df = pd.DataFrame(input_dict, index=[0])
        ## predict button
    button = st.button('Predict')

    if button:

            outcome = loaded_model.predict(input_df)
            if outcome == 0:
                st.success("will not default")
            else:
                st.error("will default")
            


        





if __name__ == '__main__':
    main()