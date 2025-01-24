import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# CSS to center the elements
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        text-align: center;
        color: rgba(167, 235, 193, 0.82);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centering the headers
st.markdown("<h2 class='center'>An EsteStyle Streamlit Page Where Python Wiz Meets Data Viz!</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'></h2>", unsafe_allow_html=True)

st.markdown("<img src='https://1drv.ms/i/s!ArWyPNkF5S-foZspwsary83MhqEWiA?embed=1&width=307&height=307' width='300' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)

st.markdown("<h2 class='center'> </h2>", unsafe_allow_html=True)

st.markdown("<h2 class='center'>Bike Rental User Data Analysis</h2>", unsafe_allow_html=True)

st.write("")

st.markdown("<h3 class='center'>What data-driven insights could promote Casual to Member rider conversion?</h3>", unsafe_allow_html=True)

st.write("")

st.markdown("<h2 class='center'>Meet the data</h2>", unsafe_allow_html=True)

col1_blk_1, col2_blk_1= st.columns([1, 1], gap="large")

with col1_blk_1:
    st.markdown("### Data Info")
    st.write("- Bike rental data aggregated over a 12 Month period from 12/2023 - 11/2024")
    st.write("- Casual riders are single use renters, while Members are monthly subscribers to the bike rental service")
    st.write("- 'started_at' timestamp used for day of week designation")
    st.write("- Data manipulations performed using SQL in BigQuery")
    st.write("")
    st.markdown("""
    ### Data Attribution
    **Dataset:** Provided by Motivate International Inc.  
    **Accessed on:** January 20, 2025.
    """)

with col2_blk_1:
    OG_data = {
    "ride_id": [
        "C1D650626C8C899A",
        "EECD38BDB25BFCB0",
        "F4A9CE78061F17F7",
        "0A0D9E15EE50B171",
        "33FFC9805E3EFF9A",
        "C96080812CD285C5",
        "0EA7CB313D4F456A"
    ],
    "rideable_type": [
        "electric_bike",
        "electric_bike",
        "electric_bike",
        "classic_bike",
        "classic_bike",
        "classic_bike",
        "classic_bike"
    ],
    "started_at": [
        "1/12/2024 15:30",
        "1/8/2024 15:45",
        "1/27/2024 12:27",
        "1/29/2024 16:26",
        "1/31/2024 5:43",
        "1/7/2024 11:21",
        "1/5/2024 14:44"
    ],
    "ended_at": [
        "1/12/2024 15:37",
        "1/8/2024 15:52",
        "1/27/2024 12:35",
        "1/29/2024 16:56",
        "1/31/2024 6:09",
        "1/7/2024 11:30",
        "1/5/2024 14:53"
    ],
    "start_station_name": [
        "Wells St & Elm St",
        "Wells St & Elm St",
        "Wells St & Elm St",
        "Wells St & Randolph St",
        "Lincoln Ave & Waveland Ave",
        "Wells St & Elm St",
        "Wells St & Elm St"
    ],
    "start_station_id": [
        "KA1504000135",
        "KA1504000135",
        "KA1504000135",
        "TA1305000030",
        "13253",
        "KA1504000135",
        "KA1504000135"
    ],
    "end_station_name": [
        "Kingsbury St & Kinzie St",
        "Kingsbury St & Kinzie St",
        "Kingsbury St & Kinzie St",
        "Larrabee St & Webster Ave",
        "Kingsbury St & Kinzie St",
        "Kingsbury St & Kinzie St",
        "Kingsbury St & Kinzie St"
    ],
    "end_station_id": [
        "KA1503000043",
        "KA1503000043",
        "KA1503000043",
        "13193",
        "KA1503000043",
        "KA1503000043",
        "KA1503000043"
    ],
    "start_lat": [
        41.90326738,
        41.9029365,
        41.902951333333334,
        41.884295,
        41.948797,
        41.903222,
        41.903222
    ],
    "start_lng": [
        -87.63473678,
        -87.63444017,
        -87.63447033,
        -87.633963,
        -87.675278,
        -87.634324,
        -87.634324
    ],
    "end_lat": [
        41.88917683,
        41.88917683,
        41.88917683,
        41.921822,
        41.88917683,
        41.88917683,
        41.88917683
    ],
    "end_lng": [
        -87.63850577,
        -87.63850577,
        -87.63850577,
        -87.64414,
        -87.63850577,
        -87.63850577,
        -87.63850577
    ],
    "member_casual": [
        "member",
        "member",
        "member",
        "member",
        "member",
        "member",
        "member"
    ]
}

    st.markdown("### Original Dataset")
    st.write("Dataset used contains 144873 rows and 13 columns")
    st.write("Data snapshot: first 7 rows")
    st.dataframe(OG_data)
st.write("")
st.markdown("<h2 class='center'>Question 1:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>Do ride times differ between user types?</h2>", unsafe_allow_html=True)

col1_blk_2, col2_blk_2 = st.columns([1, 1], gap="large")

with col1_blk_2:
    # Define the SQL code
    sql_code = """
    SELECT 
        member_casual,
        AVG(TIMESTAMP_DIFF(end_time, start_time, MINUTE)) AS avg_time_minutes
    FROM (
        SELECT * FROM `Bike_Trip_Data.month_1`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_2`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_3`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_4`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_5`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_6`
    )
    GROUP BY member_casual
    ORDER BY avg_time_minutes DESC;
    """
    st.subheader("SQL | BigQuery") 
    st.write("Join CSV datatables & calculate the average trip time between Casual & Member riders")
    # Display the SQL code with syntax highlighting
    st.code(sql_code, language="sql")
    
with col2_blk_2:
    # Manually create a DataFrame from SQL query values
    ride_time_data = {
    'member_casual': ['casual', 'member'],
    'avg_time_minutes': [22.81, 11.64]
    }
    ride_time_df = pd.DataFrame(ride_time_data)
    st.markdown("### Query Output")
    # Display the DataFrame in Streamlit
    st.dataframe(ride_time_df)

    # Create a bar chart using Plotly
    fig = go.Figure(data=[
        go.Bar(
            x=ride_time_df['member_casual'],
            y=ride_time_df['avg_time_minutes'],
            marker_color=['blue', 'orange']  # Custom colors for bars
        )
    ])
    # Add layout details
    fig.update_layout(
        title='Average Ride Time by Member Type',
        title_x=0.25,  # Center the title
        xaxis_title='Casual type riders take longer trips on average',
        yaxis_title='Average Time (Minutes)',
        template='plotly_white'
    )
    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<h2 class='center'>Data Insight 1:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>As Casual riders, take longer trips, member benefits could offer a price break for rides beyond a certian time point</h2>", unsafe_allow_html=True)
st.write("")

st.write("")
st.markdown("<h2 class='center'>Question 2:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>Are there bike type preferences among casual riders?</h2>", unsafe_allow_html=True)


col1_blk_3, col2_blk_3 = st.columns([1, 1], gap="large")

with col1_blk_3:
    # Define the SQL code
    sql_code = """
    SELECT 
        rideable_type,
        COUNT(rideable_type) AS ride_type_count,
        ROUND(COUNT(rideable_type) * 100.0 / SUM(COUNT(rideable_type)) OVER (), 2) AS percent_of_total
    FROM (
        SELECT * FROM `Bike_Trip_Data.month_1`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_2`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_3`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_4`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_5`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_6`
    )
    WHERE member_casual = 'casual'
    GROUP BY rideable_type
    ORDER BY percent_of_total DESC;
    """
    st.subheader("SQL | BigQuery")
    st.write("Join CSV datatables & calculate the percent of total rides Casual riders rent electic vs classic bikes")
    # Display the SQL code with syntax highlighting
    st.code(sql_code, language="sql")

with col2_blk_3:
    # Data for the dataframe
    ride_type_data = {
        'Rideable Type': ['Electric Bike', 'Classic Bike'],
        'Count': [235518, 195215],
        'Percent': [54.68, 45.32]
    }

    # Create a pandas dataframe
    ride_type_df = pd.DataFrame(ride_type_data)

    # Display the dataframe in Streamlit
    st.markdown("### Query Output")
    st.dataframe(ride_type_df)

    # Data for the pie chart
    labels = ['Electric Bike', 'Classic Bike']
    counts = [235518, 195215]
    percentages = [54.68, 45.32]
    # Create the pie chart using Plotly
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=counts,
                textinfo='label+percent',
                hoverinfo='label+value+percent',
                hole=0.3,  # Optional: Creates a donut chart
                marker=dict(colors=['#636EFA', '#EF553B'])  # Optional: Custom colors
            )
        ]
    )
    # Update layout for the chart
    fig.update_layout(
    title='Distribution of Rideable Types',
    title_x=0.23,  # Center the title
    showlegend=False,  # Hide the legend
    annotations=[
        dict(
            text='Casual riders use ebikes more than classic type',  # Your caption text
            x=0.5,  # Center the text horizontally
            y=-0.1,  # Position below the chart
            showarrow=False,  # Remove the arrow
            font=dict(size=15),  # Optional: Adjust font size
            xref='paper',  # Reference relative to the paper
            yref='paper'   # Reference relative to the paper
        )
    ]
)
    # Display the chart in Streamlit
    st.plotly_chart(fig)
    

st.markdown("<h2 class='center'>Data Insight 2:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>Electric bikes being more popular among Casual riders, users who become Members could receive discounts on ebike use</h2>", unsafe_allow_html=True)
st.write("")

st.write("")
st.markdown("<h2 class='center'>Question 3:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>What days of the week are most popular among Casual type riders?</h2>", unsafe_allow_html=True)

st.write("")

col1_blk_4, col2_blk_4 = st.columns([1, 1], gap="large")

with col1_blk_4:
    # Define the SQL code
    sql_code = """
    SELECT 
        FORMAT_TIMESTAMP('%A', TIMESTAMP(started_at)) AS day_of_week,
    COUNT(*) AS ride_count
    FROM (
        SELECT * FROM `Bike_Trip_Data.month_1`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_2`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_3`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_4`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_5`
        UNION ALL
        SELECT * FROM `Bike_Trip_Data.month_6`
    )
    WHERE member_casual = 'casual'
    GROUP BY day_of_week
    ORDER BY 
        CASE 
            WHEN day_of_week = 'Sunday' THEN 1
            WHEN day_of_week = 'Monday' THEN 2
            WHEN day_of_week = 'Tuesday' THEN 3
            WHEN day_of_week = 'Wednesday' THEN 4
            WHEN day_of_week = 'Thursday' THEN 5
            WHEN day_of_week = 'Friday' THEN 6
            WHEN day_of_week = 'Saturday' THEN 7
    END;
    """
    st.subheader("SQL | BigQuery")
    st.write("Join CSV datatables, extract & group by day of week only Casual riders")
    # Display the SQL code with syntax highlighting
    st.code(sql_code, language="sql")
    # Manually create a DataFrame from SQL query values

with col2_blk_4:
    week_day_data = {
        'day_of_week': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        'count': [74152, 56477, 55853, 48251, 48729, 59669, 87602]
    }
    week_day_df = pd.DataFrame(week_day_data)
    # Display the DataFrame in Streamlit
    st.markdown("### Query Output")
    st.dataframe(week_day_df)
    
    # Create a Plotly bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                x=week_day_df['day_of_week'],  # Days of the week
                y=week_day_df['count'],        # Ride counts
                marker_color='lightskyblue',  # Bar color
            )
        ]
    )
    # Customize the layout
    fig.update_layout(
        title='Ride Counts by Day of the Week',
        title_x=0.25,  # Center the title
        xaxis_title='Casual rider highest use days are weekends',
        yaxis_title='Ride Count',
        template='plotly_white'
    )
    # Display the chart in Streamlit
    st.plotly_chart(fig)

st.markdown("<h2 class='center'>Data Insight 3:</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'>Casual users peak days of rental are Sat & Sun, rental for these days might be incentivized for Member users</h2>", unsafe_allow_html=True)
