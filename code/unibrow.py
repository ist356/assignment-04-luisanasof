'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
from pandaslib import get_column_names, get_columns_of_type, get_unique_values, get_file_extension, load_file

st.title("UniBrow")
st.caption("The Universal data browser")

file_input = st.file_uploader("Upload a cvs, json or excel file:",
                              type=['csv','json','xlsx'])


if file_input:
    filename = file_input.name
    ext = get_file_extension(filename)
    dataframe = load_file(file_input, ext)
    columns = get_column_names(dataframe)

    column_select = st.multiselect("Select which columns to view:",
                                   placeholder="Choose at least one column",
                         options = columns,
                         default=columns)
    
    filter = st.toggle("Filter")
    if filter: 
        object_cols = get_columns_of_type(dataframe,"object")
        object_col = st.selectbox("Choose a column to filter on:",
                                    options = object_cols)
        unique_vals = get_unique_values(dataframe, object_col)
        #unique_vals = dataframe[object_col].unique()
        unique_val = st.selectbox("Choose a value to filter on:",
                                    options=unique_vals)
        
        filtered_df = dataframe[dataframe[object_col]==unique_val]

        st.dataframe(filtered_df)
        st.write(filtered_df.describe())

    else:
        dataframe = dataframe[column_select]
        st.dataframe(dataframe)
        st.write(dataframe.describe())


#import sys

#for line in sys.path:
#     print(line)
    
    




