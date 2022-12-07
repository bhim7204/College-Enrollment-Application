
#libraries 
import streamlit as st
import numpy as np
import pandas as pd
#st.set_option('deprecation.showfileUploaderEncoding',False) 



#file_dir = r'c:/Users/praja/database'
file_name = 'college_data.csv'


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>College Enrollment Application</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Enter the applicable data in the form provided</h3>", unsafe_allow_html=True)
  
  df1 = pd.read_csv(f"database/{file_name}")
  #data = st.dataframe(df1)

  with st.sidebar.form(key = 'df1', clear_on_submit = True):
    name = st.text_input('Student Full Name')
    degree = st.text_input('Highest degree achieved')
    year = st.number_input('Year passed out', min_value= 2015)
    program = st.radio(
        "Select the program you want to enroll",
        key="visibility",
        options=["AIMT", "AHCT", "CPM","CCBT","SCMM"],
    )
    
    submit = st.form_submit_button('Submit')
    if submit:
        new_data = {'Name of student': name, 'Degree': degree,
                    'Year Passed Out': year,'Program Enrolled':program}

        df1 = df1.append(new_data, ignore_index = True)
        df1.to_csv(file_name, index = False)

  st.header('Updated Database')
  st.dataframe(df1)




if __name__ =='__main__':
  main()