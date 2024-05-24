This Python script analyses and visualises a land survey traverse defined by its coordinates in a csv file.

Tools Functionality:

dataParsing.py:
1.read_traverse_data function reads traverse data from a traverse_data.csv file.
2.read_traverse_data function validates the data format in the submitted file.
3.read_traverse_data function handles potential errors associated with the data to allow for continuous flow of code.

traverseAnalysis.py:
1.calculate_traverse_characteristic function calculates the total number of traverse points.
2.calculate_traverse_characteristic function returns the minimum and maximum Easting and Northing values.
3.calculate_distance function calculates the distance between two input traverse points within the csv file.
4.calculate_bearing function calculates the distance between two input traverse points within the csv file.

plotting.py:
1.plot_traverse function generates a scatter plot using matplotlib that shows all traverse points numbered according to corresponding point number.

main.py:
1.TraverseAnalyzerApp class combines all project functions into a simple GUI(Graphical User Interface) using the Tkinter library allowing users to easily select the traverse data file , select the two points to compute distance and direction and initiate the analysis and visualisation process.
2.Displays the final traverse plot and analysis figures and values to the user.

Usage Instructions:
1.Run the whole code through main.py and provide information asked on the Graphical User Interface.
2.Ensure that the selected file is a csv file.
3.Labels Select Point To and Select Point from accepts integers not strings.
4.Install Python libraries like Matplotlib ,pandas and Tkinter or use conda environment to be able to run code without errors


