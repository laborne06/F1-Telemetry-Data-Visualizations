# %%
# Which driver had the fastest lap for the 2024 Monaco GP?
fastest_lap_info = session.laps.pick_fastest()
fastest_lap_driver = print(fastest_lap_info['Driver'])
fastest_lap_driver
# OR 
fastest_lap_driver = print(fastest_lap_info.Driver)
fastest_lap_driver

# %%
# What tire compounds did that driver use?
tire_info = print(fastest_lap_info.Compound)

# %%
# What tire compound did PIA use on lap 22?
pia_laps = session.laps.pick_drivers("PIA")
pia_lap_22 = pia_laps[pia_laps['LapNumber'] == 22].iloc[0]
pia_lap_22_compound = print(pia_lap_22.Compound)

# %%
# How many laps did each pf PIA's stints last?
pia_stint_lengths = session.laps.pick_drivers("PIA").Stint.value_counts().sort_index()

# %%
# How many laps did HAM race?
session_laps_num = len(session.laps.pick_drivers("HAM"))
print(session_laps_num)

# %%
# What was VER speed on lap 20?
ver_laps = session.laps.pick_drivers("VER")
ver_lap_20 = ver_laps[ver_laps["LapNumber"] == 20].iloc[0]
ver_lap_20_speed = ver_lap_20.SpeedST
print(ver_lap_20_speed)

# %%
# What tire compounds did each driver use?
driver_compounds = session.laps[['Driver', 'Compound']]
print(driver_compounds)

# %%
Display PIA laps by stint in pie chart
pia_stint_lengths_df = pia_stint_lengths.to_frame()
df = pia_stint_lengths_df
fig = px.pie(df, 
    names= 'count',  # First column index
    values= 'count'  # Second column index
)
fig.show()