# Movie Recommendation System

## Overview

This project is a **Movie Recommendation System** built using **Streamlit**. It allows users to receive movie recommendations based on their favorite movie, using a precomputed similarity matrix.

## Features

- Interactive Streamlit interface.
- Movie selection from a dropdown menu.
- Five movie recommendations based on the selected movie.

## Technologies Used

- **Python**: Backend and logic implementation.
- **Streamlit**: For creating an interactive web interface.
- **Pickle**: For loading precomputed data files.

## Files Included

1. `movie_recomender_system.ipynb`: Jupyter Notebook containing the code for preprocessing, model training, and similarity computation.
2. `app.py`: Streamlit application script for the frontend.

## How to Run the Project

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Streamlit

### Installation Steps

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required Python libraries:
   ```bash
   pip install streamlit
   ```
4. Place the `movies.pkl` and `similarity.pkl` files in the project directory.

### Running the Application

1. Open a terminal in the project directory.
2. Run the Streamlit app using:
   ```bash
   streamlit run app.py
   ```
3. The application will open in your default web browser.

## How It Works

1. The user selects a movie from the dropdown menu.
2. When the "Recommend" button is clicked, the app:
   - Finds the index of the selected movie.
   - Retrieves the top 5 most similar movies based on a precomputed similarity matrix.
   - Displays the recommended movies on the screen.

## Data Files

- `movies.pkl`: Contains movie metadata, including titles.
- `similarity.pkl`: Contains the precomputed similarity matrix.

## Future Enhancements

- Add movie posters for the recommended movies.
- Improve recommendation algorithm with collaborative filtering or content-based filtering.

## Acknowledgments

This project is inspired by the need for personalized movie recommendations to enhance user experience.

