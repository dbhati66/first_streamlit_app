import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry Oatmeal')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index('Fruit')

# lets put a pick list here
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]


#display thr table
streamlit.dataframe(fruits_to_show)

#New section to display api response
streamlit.header('Fruityvice Fruit Advice!')


import requests
fruityvice_response =requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
#streamlit.text(fruityvice_response.json())


fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
