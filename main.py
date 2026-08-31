#%%
import fastf1
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import math
pio.renderers.default = "notebook"
fastf1.Cache.enable_cache("cache")
#%%
session = fastf1.get_session(2024, "Monaco", "R")
session.load()
# Create a line chart for PIA lap time vs. lap number
# pia_lap_info = session.laps.pick_drivers("PIA")
# # Extract a copy of the LapNumber and LapTime data
# pia_laps_and_time = pia_lap_info[['LapNumber', 'LapTime']].copy()
# # Add "LapTimeSeconds" column to df
# pia_laps_and_time["LapTimeSeconds"] = (pia_laps_and_time['LapTime'].dt.total_seconds()
# )
# # Update the variable to reference LapTimes less than 180 seconds
# pia_laps_and_time = pia_laps_and_time[
#     pia_laps_and_time["LapTimeSeconds"] < 180
# ]
# # Display the chart
# fig = px.line(pia_laps_and_time, 
#     x = 'LapNumber',
#     y = 'LapTimeSeconds',
#     markers = True,
#     title = "Oscar Piastri — 2024 Monaco GP Race Lap Times"
# )
# fig.update_layout(
#     title_x=0.5,
#     xaxis_title = "Lap Number",
#     yaxis_title = "Lap Time"
# )
# fig.update_yaxes(
#     range=[
#         75, 85.5
#     ],
#         # Major ticks
#         tick0 = 75,
#         dtick = 5,
#         ticktext = ["1:15", "1:20", "1:25"],
#         # Minor ticks
#         minor=dict(
#             tick0=75,
#             dtick=1,
#             ticks="outside",
#             showgrid=True
#         )
# )
# fig.show()

#%%
# Now update the function to plot the lap times of two different drivers
def plot_driver_lap_times(session, driver):
    driver_lap_info = session.laps.pick_drivers(driver)
    driver_laps_and_time = driver_lap_info[['LapNumber', 'LapTime']].copy()
    driver_laps_and_time["LapTimeSeconds"] = (driver_laps_and_time['LapTime'].dt.total_seconds()
    )
    driver_laps_and_time = driver_laps_and_time[
    driver_laps_and_time["LapTimeSeconds"] < 180
    ]
    fig = px.line(driver_laps_and_time, 
    x = 'LapNumber',
    y = 'LapTimeSeconds',
    markers = True,
    title = driver + " Lap Times"
    )
    fig.update_layout(
        title_x=0.5,
        xaxis_title = "Lap Number",
        yaxis_title = "Lap Time"

    )
    fastest_lap = math.floor(driver_laps_and_time['LapTimeSeconds'].min())
    slowest_lap = math.floor(driver_laps_and_time['LapTimeSeconds'].max())
    fig.update_yaxes(
        range=[
            math.floor(fastest_lap) - 2, 
            math.ceil(slowest_lap) + 2
        ],
            # Major ticks
            tick0 = (fastest_lap // 5) * 5,
            dtick = 5,
            # Minor ticks
            minor=dict(
                tick0=fastest_lap,
                dtick=1,
                ticks="outside",
                showgrid=True
            )
    )
    fig.show()
#%%
def get_driver_laps_data(session, driver):
    driver_lap_info = session.laps.pick_drivers(driver)
    driver_laps_and_time = driver_lap_info[['LapNumber', 'LapTime']].copy()
    driver_laps_and_time["LapTimeSeconds"] = (driver_laps_and_time['LapTime'].dt.total_seconds()
    )
    driver_laps_and_time = driver_laps_and_time[
    driver_laps_and_time["LapTimeSeconds"] < 180
    ]
    return driver_laps_and_time

# Now update the function to compare the lap times of two drivers
def plot_two_driver_lap_times(session, first_driver, second_driver):
    first_driver_laps_and_time = get_driver_laps_data(session, first_driver)
    second_driver_laps_and_time = get_driver_laps_data(session, second_driver)
    
    fig = px.line(first_driver_laps_and_time, 
    x = 'LapNumber',
    y = 'LapTimeSeconds',
    markers = True,
    title = first_driver + " and " + second_driver + " Lap Times",
    )

    fig.update_traces(
        name = first_driver + " Lap Times",
        showlegend = True
    )

    # Add second driver lap times
    second_y = second_driver_laps_and_time["LapTimeSeconds"]
    fig.add_scatter(
        x = second_driver_laps_and_time['LapNumber'],
        y = second_y, 
        mode = "lines+markers",
        name = second_driver + " Lap Times"
    )

    first_driver_min_time = first_driver_laps_and_time['LapTimeSeconds'].min()
    first_driver_max_time = first_driver_laps_and_time['LapTimeSeconds'].max()
    second_driver_min_time = second_driver_laps_and_time['LapTimeSeconds'].min()
    second_driver_max_time = second_driver_laps_and_time['LapTimeSeconds'].max()

    if first_driver_min_time > second_driver_min_time:
        fastest_lap = second_driver_min_time
    else: 
        fastest_lap = first_driver_min_time

    if first_driver_max_time > second_driver_max_time:
        slowest_lap = first_driver_max_time
    else: 
        slowest_lap = second_driver_max_time

    fastest_lap = math.floor(fastest_lap)
    slowest_lap = math.ceil(slowest_lap)
    
    fig.update_layout(
        title_x=0.5,
        xaxis_title = "Lap Number",
        yaxis_title = "Lap Time",
    )

    fig.update_yaxes(
        range=[
            fastest_lap - 2, 
            slowest_lap + 2
        ],
            # Major ticks
            tick0 = (fastest_lap // 5) * 5,
            dtick = 5,
            # Minor ticks
            minor=dict(
                tick0=fastest_lap,
                dtick=1,
                ticks="outside",
                showgrid=True
            )
    )
    fig.show()

# %%
plot_two_driver_lap_times(session, "PIA", "VER")

# %%
def get_driver_lap_info(session, driver, first_data_type, second_data_type):
    driver_lap_info = session.laps.pick_drivers(driver)[[first_data_type, second_data_type]].copy()
    return driver_lap_info

# %%
# Create a function that takes a session and two drivers, and outputs a line chart for
# data type one (x) and data type two (y)
def two_driver_line_chart(session, first_driver, second_driver, first_data_type, second_data_type):
    first_driver_laps_info = get_driver_lap_info(session, first_driver, first_data_type, second_data_type)
    second_driver_laps_info = get_driver_lap_info(session, second_driver, first_data_type, second_data_type)

    fig = px.line(first_driver_laps_info, 
    x = 'LapNumber',
    y = second_data_type,
    markers = True,
    title = first_driver + " and " + second_driver + ' ' + second_data_type + 's by ' + first_data_type,
    )

    fig.update_traces(
        name = first_driver + '' + second_data_type + 's',
        showlegend = True
    )

    # Add second driver lap times
    second_y = second_driver_laps_info[second_data_type]
    fig.add_scatter(
        x = second_driver_laps_info['LapNumber'],
        y = second_y, 
        mode = "lines+markers",
        name = second_driver + '' + second_data_type + 's'
    )

    fig.update_yaxes(
        dtick = 1
    )

    fig.show()

#%%
two_driver_line_chart(session, 'PIA', 'VER', 'LapNumber','Position')