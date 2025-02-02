# Traffic Accident Analysis Dashboard

This repository contains a Flask-based web application designed to analyze and visualize traffic accident data. The dashboard provides summary statistics and detailed visualizations to help users understand patterns, trends, and contributing factors related to traffic accidents.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)

---

## Overview

The Traffic Accident Analysis Dashboard is a Python-based Flask application that processes a dataset of traffic accidents (`cleaned_traffic_accidents.csv`) and presents insights through a combination of summary statistics and interactive visualizations. The dashboard is designed to be user-friendly, responsive, and visually appealing.

Key features include:
- Summary statistics highlighting total accidents, most common causes, peak hours, and more.
- Seven detailed visualizations exploring various aspects of the data (e.g., accident distribution by hour, weather conditions, and injury severity).

---

## Features

### Summary Statistics
- **Total Accidents**: The total number of accidents recorded in the dataset.
- **Most Common Contributory Cause**: The primary reason for accidents, identified using the mode of the `prim_contributory_cause` column.
- **Most Frequent Weather Condition**: The weather condition most commonly associated with accidents.
- **Peak Hour for Accidents**: The hour of the day when accidents are most frequent.
- **Day with the Most Accidents**: The day of the week with the highest number of accidents.
- **Average Damage Cost**: The most common damage cost range for accidents.

These metrics offer a quick overview of the dataset and highlight critical areas for further investigation.

### Visualizations
1. **Accident Distribution by Hour of Day**:
   - A histogram showing the distribution of accidents across all 24 hours of the day.
   - Highlights peak hours for accidents and helps identify time-based patterns.

2. **Top 10 Primary Contributory Causes**:
   - A bar chart displaying the top 10 reasons for accidents.
   - Provides insights into the most frequent causes of traffic incidents.

3. **Accident Distribution by Weather Conditions**:
   - A pie chart showing the percentage of accidents occurring under different weather conditions.
   - Helps identify how weather impacts accident frequency.

4. **Accidents by Day of Week**:
   - A bar chart comparing the number of accidents across each day of the week.
   - Useful for understanding weekly trends in accident occurrences.

5. **Heatmap: Accident Hotspots (Hour vs Day of Week)**:
   - A heatmap visualizing the intensity of accidents at different times of the day and days of the week.
   - Identifies specific "hotspots" where accidents are most concentrated.

6. **Accident Severity by Damage Cost**:
   - A bar chart categorizing accidents based on the severity of damage costs (e.g., "$500 OR LESS", "OVER $1,500").
   - Highlights the financial impact of accidents.

---

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Data Analysis**: Pandas, Matplotlib, Seaborn
- **Frontend**: HTML, CSS
- **Data Encoding**: Base64 encoding for embedding images in HTML

---
