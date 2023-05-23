# Import Statement
import streamlit as st
import pandas as p

# Setting up the page layout to be wide
st.set_page_config(layout='wide')

df = p.read_csv('data.csv', sep=';')

# Creating columns for the website through the st.columns()
# method which returns columns objects
c1, c2 = st.columns(2)

# Header column 1
with c1:
    c1.image('images/photo.jpg', width=500)

# Header column 2
with c2:
    c2.title('Paul Lavoie')
    content = """Hello, my name is Paul Lavoie, a current student studying Information Technology at George Mason University. I created this portfolio web-app, specifically through the Streamlit module, to keep records and showcase projects that I have developed throughout my academic career. I have interned at TGI Fridays for their Digital Team and am excited to seek out and find new opportunities that may come my way! """
    c2.info(content)

st.title("My Application")

c1,c2 = st.columns(2)

for index, row in df.iterrows():
    with c1:
        if (index + 1) % 2 != 0:
            c1.header(df['title'][index])
            c1.image('images/{}.png'.format(index+1))
            c1.write(df['description'][index])
            

    with c2:
        if (index + 1) % 2 == 0:
            c2.header(df['title'][index])
            c2.image('images/{}.png'.format(index+1))
            c2.write(df['description'][index])




    

