import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Ka Data visualization')

selected_state = st.sidebar.selectbox('Select a state', list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))

secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text("size represents primary parameter")
    st.text("color represents secondary parameter")

    if selected_state == 'Overall India':

        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=35, width=1200, height=700,
                                hover_name='District', mapbox_style="carto-positron")

        st.plotly_chart(fig, use_container_width=True)


    else:
        # plot for state and for this we need to filter the df.
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=35, width=1200, height=700,
                                hover_name='District', mapbox_style="carto-positron")

        st.plotly_chart(fig, use_container_width=True)