import streamlit as st
from streamlit_option_menu import option_menu
import os
import json
from PIL import Image

path_json = './links/links.json'

def config():
    st.set_page_config(
        page_title="Save your LINKS",
        page_icon=r"./src/tent_outdoor_camp_camping_holiday_icon_226685.png",
        #layout="wide",
        initial_sidebar_state="expanded",
        
    )
def get_categories():
    file = open(path_json)
    data = json.load(file)

    categories=[]
    for x in data['links']:
        categories.append(x)

    return (categories)

def nav_bar():
    selected_menu = option_menu(None, ["Show links", "Save links"], 
    icons=['bi bi-body-text', 'bi bi-save', 'bi bi-trash'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

    categories = get_categories()

    if selected_menu == "Show links": show_link(categories)
    if selected_menu == "Save links": save_link(categories)
    

def show_link(categories):
    file = open(path_json)
    data = json.load(file)

    options = st.selectbox('Select your category', categories)

    st.json(data['links'][options])


    buff, col, buff2 = st.columns([0.6,2,1])
    
    remove_value = col.text_input('Remove value')

    button_remove = buff2.write('\n')
    button_remove = buff2.write('\n')
    button_remove = buff2.button('Remove')
    if button_remove:
        try:
            if remove_value:
                with st.spinner('Removing ...'):
                    del data['links'][options][int(remove_value)]

                    with open(path_json, "w") as f:
                        json.dump(data, f , indent=4)
                st.success('Removed')
        except:
            if remove_value:
                
                data['links'][options].remove(remove_value)

                with st.spinner('Removing ...'):
                    with open(path_json, "w") as f:
                        json.dump(data, f , indent=4)
                st.success('Removed')

def save_link(categories):
    with open(path_json, 'r+') as file:

        file_data = json.load(file)

        options = st.selectbox('Select your category', categories)
        link_input = st.text_input('Past your link')
        if link_input:
            with st.spinner('Saving ...'):
                file_data['links'][options].append(link_input)
                file.seek(0)

                json.dump(file_data, file, indent=4)
            st.success('Saved')




if __name__ == '__main__':
    config()
    col, dont_copy = st.columns([ 0.1, 4])
    image = Image.open('./src/tent_camp_icon_177133.png')
    
    col.image(image=image, width=100)
    dont_copy.markdown("<h1 style='text-align: center;'>Save your <em>LINKS</em></h1>", unsafe_allow_html=True)

    nav_bar()


