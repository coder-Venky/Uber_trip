# Uber Trip Data Analysis

This project analyzes Uber trip data using Python and implements a simple fare prediction model using only the Python standard library.

## Features

- Data loading and preprocessing
- Basic statistical analysis
- Peak hour analysis
- Weekday pattern analysis
- Simple fare prediction model

## Project Structure

- `src/data_loader.py`: Handles loading and initial processing of trip data
- `src/data_preprocessor.py`: Contains data preprocessing and feature extraction functions
- `src/analysis.py`: Implements various analysis functions
- `src/ml_model.py`: Contains a simple fare prediction model
- `src/main.py`: Main script that ties everything together

## Required Data Format

The program expects a CSV file named `uber_trips.csv` with the following columns:
- pickup_datetime
- dropoff_datetime
- distance
- fare

## Usage

Run the analysis:
```
python src/main.py
```

## Output

The program will generate:
- Basic trip statistics
- Peak hour analysis
- Weekday pattern analysis
- Simple model performance metrics
- Sample fare prediction