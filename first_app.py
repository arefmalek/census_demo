import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

race_composite = pd.read_csv("data/race.csv")
age_composite = pd.read_csv("data/age.csv")
sex_composite = pd.read_csv("data/sex.csv")

st.title("Why its F the Electoral College")

year = st.sidebar.select_slider( 
        "Select the Year",
        [*range(2010, 2020)],
)

st.write("Year: ", year)

race = pd.DataFrame(race_composite[str(year)])
race.index = race_composite["Label"]

age = pd.DataFrame(age_composite[str(year)])
age.index = age_composite["Label"]

sex = pd.DataFrame(sex_composite[str(year)])
sex.index = sex_composite["Label"]


st.bar_chart(race)

st.bar_chart(age)

st.bar_chart(sex)
