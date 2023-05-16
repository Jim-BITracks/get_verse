# streamlit run get_verse_streamlit.py

import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.title("Day of Life Verse (from Birth)")
today = date.today()
#today = date(1980,2,7)
min_date = today - timedelta(weeks=6000)

birth_date = st.date_input("Enter your birthdate:", value=date(2000, 12, 31), min_value=min_date, max_value=today)
st.write('Using the birthday of:', birth_date.strftime("%A, %B %d, %Y"))
st.divider()
verses_index = (today - birth_date).days
day_of_life_from_birth = verses_index + 1
bible_verse_number = day_of_life_from_birth

st.write("Details for today:", today.strftime("%A, %B %d, %Y"))
st.write('Counting from the day you were born as number 1, you are currently in day number:', day_of_life_from_birth)

if verses_index > 31101:
    verses_index = verses_index - 31102
    bible_verse_number = verses_index + 1

# load Pickle
df = pd.read_pickle('data/verses.pkl')

book_name = df.iloc[verses_index]['book_name'].lower()
book_name = book_name.replace(' ', '_', 1)
chapter = df.iloc[verses_index]['chapter']
verse = df.iloc[verses_index]['verse']

link_to_verse = f'https://biblehub.com/{book_name}/{chapter}-{verse}.htm'

st.write(f"Read verse number: {bible_verse_number} (counting from Genesis 1:1) on [biblehub.com](%s)" % link_to_verse)