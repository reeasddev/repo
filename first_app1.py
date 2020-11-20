#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import streamlit as st


#https://blog.jcharistech.com/2019/10/20/streamlit-python-tutorial-crash-course/

st.write("""
#My first app
Hello  *world!*
""")


# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")


st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")

# Get Help
st.help(range)

# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")


# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)


# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")


# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname", "Type Here..")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area("Enter Your message", "Type Here..")
#if st.button("Submit"):
    #result = message.title()
    #st.success(result)

# Date Input
import datetime

today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.time())


# Images
from PIL import Image
#img = Image.open("example.jpeg")
#st.image(img,width=300,caption="Simple Image")


# Videos
#vid_file = open("example.mp4","rb").read()
# vid_bytes = vid_file.read()
#st.video(vid_file)

# Audio
#audio_file = open("examplemusic.mp3","rb").read()
#st.audio(audio_file,format='audio/mp3')


# Writing Text/Super Fxn
st.write("Text with write")

st.write(range(10))


# Displaying Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code
#with st.echo():
# This will also show as a comment
#import pandas as pd
#df = pd.DataFrame()


# Displaying JSON
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})


# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")


# Balloons
#st.balloons()


# Plot
st.pyplot()

# DataFrames
#st.dataframe(df)

# Tables
#st.table(df)


# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")


# Normal Function
def run_fxn():
    return range(100)

st.write(run_fxn())

# To Improve Performance/Speed via caching
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())