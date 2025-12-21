#!/usr/bin/env python
# coding: utf-8

# In[71]:


import streamlit as st

st.set_page_config(
    page_title="AFCON 2025-26 Predictions",   # Title shown in browser tab
)

st.title("AFCON 2025-26 Predictions")

# Define tabs
tab_names = ["Ratings","Group Fixtures W/D/L", "Group Fixtures Goals", "Group Tables", "KO Probabilities", "Final Combinations"]
tabs = st.tabs(tab_names)

for tab, sheet in zip(tabs, tab_names):
    with tab:
        # --- Ratings: only embed Datawrapper chart ---
        if sheet == "Ratings":
            iframe = """
            <iframe src="https://datawrapper.dwcdn.net/wPCfv/4/" 
                    width="100%" 
                    height="100%" 
                    style="min-height: 90vh;" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe, height=770)
        
        # --- Group Fixtures: only embed Datawrapper chart ---
        elif sheet == "Group Fixtures W/D/L":
            iframe = """
            <iframe src="https://datawrapper.dwcdn.net/U0Nyv/10/" 
                    width="100%" 
                    height="100%" 
                    style="min-height: 90vh;" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe, height=1650)

        # --- Group Fixtures: only embed Datawrapper chart ---
        elif sheet == "Group Fixtures Goals":
            iframe = """
            <iframe src="https://datawrapper.dwcdn.net/HpwkH/2/" 
                    width="100%" 
                    height="100%" 
                    style="min-height: 90vh;" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe, height=1650)

        # --- Group Tables: embed two Datawrapper charts under each other ---
        elif sheet == "Group Tables":
            subtab_names = ["Pre-Tournament", "Post Round 1", "Post Round 2", "Post Round 3"]
            subtabs = st.tabs(subtab_names)

            with subtabs[0]:
            iframe1 = """
            <iframe src="https://datawrapper.dwcdn.net/CoBeg/5/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe1, height=300)
            
            iframe2 = """
            <iframe src="https://datawrapper.dwcdn.net/wHAhD/5/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe2, height=240)
            
            iframe3 = """
            <iframe src="https://datawrapper.dwcdn.net/edaIB/6/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe3, height=240)
            
            iframe4 = """
            <iframe src="https://datawrapper.dwcdn.net/8Wmro/3/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe4, height=240)
            
            iframe5 = """
            <iframe src="https://datawrapper.dwcdn.net/sO7rE/4/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe5, height=240)
            
            iframe6 = """
            <iframe src="https://datawrapper.dwcdn.net/sg4z1/5/" 
                    width="100%" 
                    height="500" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe6, height=240)


        # --- Stage Probabilities: placeholder ---
        elif sheet == "KO Probabilities":
            subtab_names = ["Pre-Tournament", "Post Round 1", "Post Round 2", "Post Round 3"]
            subtabs = st.tabs(subtab_names)

            with subtabs[0]:
                iframe = """
                <iframe src="https://datawrapper.dwcdn.net/eaRV8/4/" 
                        width="100%" 
                        height="100%" 
                        style="min-height: 90vh;" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframe, height=1160)

        # --- Stage Probabilities: placeholder ---
        elif sheet == "Final Combinations":
            iframe = """
            <iframe src="https://datawrapper.dwcdn.net/iFkeE/1/" 
                    width="100%" 
                    height="100%" 
                    style="min-height: 90vh;" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe, height=1500)

        # --- Other tabs: placeholders ---
        else:
            st.info(f"{sheet} tab — visualization can be added here.")


# In[ ]:




