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

# Sectioning off my applications list
st.title("My Application")

# Creating new columns (to list the apps)
c3,c4 = st.columns(2)

# Going through each row in the dataframe
for index, row in df.iterrows():
    # With C3 (adding onto column 3)
    with c3:
        # If index+1 of row is not evenly divisible by 2 (odd numbers)
        if index % 2 == 0:
            # Create header with the title of the row at the current index
            c3.header(df['title'][index])
            # Render image of the row at the current index
            c3.image('images/{}'.format(df['image'][index]))
            # Render description of row at the current index
            c3.write(df['description'][index])
            # Render link to source code 
            c3.write("[Source Code]({})".format(df['url'][index]))
            
    # Same process as above for column 4
    with c4:
        if index % 2 != 0:  
            c4.header(df['title'][index])
            c4.image('images/{}'.format(df['image'][index]))
            c4.write(df['description'][index])
            c4.write("[Source Code]({})".format(df['url'][index]))






    

