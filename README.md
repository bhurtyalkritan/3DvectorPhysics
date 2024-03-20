# Interactive 3D Vector Plotter with OBJ Files

This application allows users to upload two 3D models in OBJ format, adjust their positions in 3D space, and visualize various vector operations between them. It's built with Streamlit, Plotly for 3D visualization, Trimesh for handling 3D models, and NumPy for mathematical operations.

## Features

- **OBJ File Upload**: Users can upload two OBJ files to be displayed in a 3D plot.
- **Position Adjustment**: Each object's position can be adjusted in 3D space using sliders for X, Y, and Z axes.
- **Vector Calculations**:
  - **Resultant Vector**: Shows the resultant vector of adding the dimensions of the two objects.
  - **Difference Vector**: Shows the difference vector between the dimensions of the two objects.
  - **Cross Product**: Displays the cross product of the dimensions of the two objects.
  - **Center of Mass**: Calculates and shows the center of mass based on the dimensions and masses provided for the objects.
- **Dynamic Scene Dimensions**: The 3D scene's dimensions adjust dynamically based on the objects' positions and dimensions.

## How It Works

1. **File Upload**: Users upload two OBJ files using the file uploaders.
2. **Adjust Position**: Users adjust the position of each object using the provided sliders.
3. **Vector Visualization**: Users can select to visualize the resultant vector, difference vector, cross product, and center of mass by checking the respective checkboxes.
4. **Plot Vectors**: Upon clicking the "Plot Vectors" button, the 3D plot is generated according to the selected options and adjustments.

## Technical Details

- **Trimesh**: Used for loading and processing 3D models from OBJ files.
- **Plotly**: Generates interactive 3D plots to visualize the models and vector operations.
- **NumPy**: Facilitates mathematical calculations, especially for vector operations.
- **Streamlit**: Provides an easy-to-use web app framework for interactive applications.

## Setup and Run

To run this application locally, you need Python and the necessary libraries installed. Follow these steps:

1. Clone the repository or download the source code.
2. Install dependencies: `pip install streamlit plotly numpy trimesh`.
3. Run the app: `streamlit run your_script_name.py`.

Replace `your_script_name.py` with the name of the Python script containing the code.

## Acknowledgements

This project utilizes open-source libraries such as Streamlit, Plotly, NumPy, and Trimesh. Their contributions to the Python community are greatly appreciated.

## License

This project is open-source and available under the MIT License.
