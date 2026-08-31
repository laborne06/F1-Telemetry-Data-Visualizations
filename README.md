<h3>Formula One Telemetry Visualizations</h3>

<p>main.py contains the code for two main functions: plot_two_driver_lap_times(session, first_driver, second_driver), and two_driver_line_chart(session, first_driver, second_driver, first_data_type, second_data_type)</p>

<h4>plot_two_driver_lap_times()</h4>

<p>This function takes a session object and the three-letter abbreviations for two drivers, and outputs a line chart mapping the comparison in both drivers' lap speeds for the duration of the race.</p>

<h4>two_driver_line_chart()</h4>

<p>This function takes a session object, the three-letter abbreviations for two drivers, as well as a first and second data type to be traced throughout the duration of the race.

<h4>Example output for plot_two_driver_lap_times(session, "PIA", "VER")</h4>

![Piastri vs. Verstappen Lap Times](images/pia-ver-lap-times.png)

<p>Example output for two_driver_line_chart(session, 'PIA', 'VER', 'LapNumber','Position')</h4>

![Piastri vs. Verstappen Track Positions](images/pia-ver-positions.png)

<p>**note that the particular session object for this visualization uses telemetry from the 2024 Monaco Grand Prix. This track is notorious for being difficult to overtake in, so neither of the drivers' positions changed during the race.</p>