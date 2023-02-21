import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry Oatmeal')

python -m pip install --upgrade pip
import pandas
my_fruit_list=pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
