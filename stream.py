import streamlit as st
import pandas as pd
import pymysql

def db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="12345",
        database="redbus_project"
    )

def fetch_data(query, params):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return pd.DataFrame(data, columns=columns)

st.set_page_config(page_title='Web Scraper', layout='wide')

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome page'

with st.sidebar:
    st.title('Choose')
    if st.button('Welcome Page', type='primary'):
        st.session_state.current_page = 'welcome page'

    if st.button('Scrap Details', type='primary'):
        st.session_state.current_page = 'scrap details'

if st.session_state.current_page == 'welcome page':
    st.title('Welcome to the Web Scraper')
    st.balloons()
elif st.session_state.current_page == 'scrap details':
    st.title('Web Scraping Application')

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT state_name FROM all_bus_details ORDER BY state_name')
    states = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    state_placeholder = ['Select State'] + states

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_state = st.selectbox('State', state_placeholder)

    if selected_state and selected_state != 'Select State':
        # Fetch available "From" and "To" locations for the selected state
        query = """
            SELECT DISTINCT route_name, duration
            FROM all_bus_details
            WHERE state_name = %s
        """
        routes_df = fetch_data(query, (selected_state,))

        # Extract unique locations from route names
        store_sets = set()
        for route in routes_df['route_name']:
            route_split = route.split(' to ')
            store_sets.update(route_split)

        sorted_sets = sorted(store_sets)
        placeholder = ['Select Location'] + sorted_sets

        with col2:
            from_location = st.selectbox('From', placeholder)

        with col3:
            to_location = st.selectbox('To', placeholder)

        col4, col5, col6 = st.columns(3)

        with col4:
            busoptions = ['Select Bus Type', 'A/C', 'Non A/C']
            bus_type = st.selectbox('Select Bus Type', busoptions)

        with col5:
            price = st.number_input('Price', min_value=0, value=0)

        with col6:
            seat = st.number_input('Seats', min_value=0, value=0)

        col7, col8 = st.columns(2)

        with col7:
            star_rating = st.number_input('Star Rating', min_value=0.0, value=0.0, step=0.1)

        with col8:
            # Duration filter
            duration_options = ['Select Duration'] + list(routes_df['duration'].unique())
            duration = st.selectbox('Duration', duration_options)

        if st.button('Search'):
            if from_location == 'Select Location' or to_location == 'Select Location':
                st.warning('Please fill in the needed locations')

            else:
                route_join = f'{from_location} to {to_location}'

                query = """
                        SELECT * 
                        FROM all_bus_details
                        WHERE route_name = %s
                        AND state_name = %s
                        """
                params = [route_join, selected_state]

                if bus_type == 'A/C':
                    query += " AND bustype LIKE %s"
                    params.append('%A/C%')

                elif bus_type == 'Non A/C':
                    query += ' AND bustype LIKE %s'
                    params.append('%Non A/C%')

                if price > 0:
                    query += ' AND price <= %s'
                    params.append(price)

                if seat > 0:
                    query += ' AND seats_available >= %s'
                    params.append(seat)

                if star_rating > 0:
                    query += ' AND star_rating >= %s'
                    params.append(star_rating)

                if duration != 'Select Duration':
                    query += " AND duration <= %s"
                    params.append(duration)

                data = fetch_data(query, tuple(params))
                if not data.empty:
                    st.dataframe(data)
                else:
                    st.write('No records found')
