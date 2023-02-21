import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry Oatmeal')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.Datarame(my_fruit_list)
