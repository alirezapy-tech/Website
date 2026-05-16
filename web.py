from streamlit import *

title("Welcome TO Our Learning Website")

markdown("**[This funny video](https://youtu.be/NNeor6gJm10?si=7VWaAiKlDiT1pp57)**")

fruit_list = ["apple", "banana", "grapes", "pine apple"]
fruit = selectbox("Enter your favorite fruit:", fruit_list)

subheader(f"Your favorite fruit is {fruit}. That is a great choice!")
