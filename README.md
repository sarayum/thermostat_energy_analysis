
# Smart Thermostat Energy Analysis: Exploring Indoor Climate & Energy Patterns

## Project Overview
This project analyzes smart thermostat and weather data to uncover patterns in HVAC usage, temperature control, and energy efficiency. The goal is to derive insights that help balance indoor comfort, energy cost, and environmental factors. The analysis spans a 14-month period, focusing on operational trends, comparing setpoint and actual indoor temperatures, and examining the relationship between indoor climate and outdoor weather.

## Project Objective
To evaluate how indoor HVAC behavior correlates with outdoor weather and usage patterns, and to identify opportunities to optimize comfort and efficiency. Key questions addressed include:

- How often does the HVAC run daily?
- How closely does the actual indoor temperature align with setpoints?
- What is the relationship between indoor and outdoor temperature?

## Technologies Used

### Python
 The core programming language for this project, used for data manipulation, cleaning, visualization, and database interaction.

### Jupyter Notebooks
Used to document the entire data cleaning and analysis process in a step-by-step, interactive format

### Pandas
Used extensively for loading, cleaning, transforming, and analyzing data. It enabled tasks like missing value handling, resampling 5-minute data to hourly intervals, and merging datasets.

### NumPy
NumPy supported mathematical operations, particularly during preprocessing and aggregation.

### Matplotlib & Seaborn
Utilized to create informative visualizations, including line plots, boxplots, and time series graphs that revealed indoor-outdoor climate patterns and HVAC runtime behaviors.

### SQLite (via sqlite3)
Used to store the final processed thermostat and weather datasets in structured tables. It provided a lightweight database to query and manage cleaned data efficiently.

### Requests
Used to programmatically access the Open-Meteo Historical Weather API and download hourly weather data in JSON format.

### ipykernel 
Ensured Jupyter notebooks run smoothly within the selected Python environment.

### Visual Studio Code (VS Code)
The primary development environment, equipped with Python and Jupyter Notebook extensions to support interactive coding and markdown narration.

### Git & GitHub
Git was used for version control throughout the development process to track progress and manage changes efficiently. GitHub served as the central repository for hosting the project, enabling collaboration, backup, and easy sharing of the final deliverable.

## Project Setup Instructions

### Prerequisites

Before running this project, ensure your development environment is ready:

1. #### **Install Visual Studio Code (VS Code)**

- Download and install VS Code from:

    👉 https://code.visualstudio.com/

2. #### **Install Python**

- Download and install Python (version 3.10+) from:

    👉 https://www.python.org/downloads/

- During installation, check “Add Python to PATH” option.

3. #### **Install Python and Jupyter Extension in VS Code**

- Open VS Code → Go to Extensions (⇧⌘X / Ctrl+Shift+X)

- Search for and install:
  - Python extension by Microsoft
  - Jupyter extension by Microsoft

4. #### **Set up a Virtual Environment (Recommended)**

   Run the following commands in the VS Code terminal:

- ##### **Create virtual environment**
  python -m venv venv

- ##### **Activate the environment**

    ##### **Windows:**
     venv\Scripts\activate

    ##### **macOS/Linux:**
     source venv/bin/activate

5. #### **Install Required Python Packages**

- If a requirements.txt file is available:

    pip install -r requirements.txt

- Or manually install commonly used libraries:

    pip install pandas numpy matplotlib seaborn jupyter sqlite3

6. #### **Launch Jupyter Notebook in VS Code**

    Once setup is complete:

- Clone the Repository 

       Open your terminal or command prompt and run:

       git clone https://github.com/sarayum/thermostat_energy_analysis.git
       cd thermostat_energy_analysis

       This downloads the project files onto your computer.

- Open the project folder in VS Code
         
       Open the workspace folder thermostat_energy_analysis

- Open .ipynb files

- Select the appropriate Python interpreter (from virtual environment) in the top right corner

- Execute Notebooks in Order

       Run the notebooks in the following sequence for a smooth pipeline:

       1. clean_thermostat_data_final.ipynb

          Cleans and preprocesses thermostat runtime data

          Detects missing values, aggregates hourly data

       2. clean_weather_data_final.ipynb

          Cleans historical weather data and prepares it for merging

          Standardizes format

        3. create_sql_db.ipynb

           Creates SQLite database

           Inserts cleaned data into tables

        4. analysis.ipynb

           Performs exploratory data analysis

           Visualizes relationships between indoor/outdoor factors and HVAC behavior

           Draws insights and actionable conclusions


### Project Directory Structure
<pre lang="md"> 
THERMOSTAT_ENERGY_ANALYSIS/
│
├── .venv/                           # Virtual environment (excluded from Git)
├── data/
│   ├── raw/                         # Original thermostat & weather data (CSV/JSON)
│   └── processed/                   # Cleaned & transformed datasets for analysis
│
├── database/
│   └── thermostat_analysis.db       # SQLite DB with processed weather & thermostat tables
│
├── docs/
│   └── requirements.txt             # Python dependencies for reproducibility
│
├── notebooks/
│   ├── clean_thermostat_data_final.ipynb        # Finalized thermostat data
│   ├── clean_weather_data_final.ipynb           # Finalized weather data
│   ├── download_weather_data.ipynb              # Script to call Open-Meteo API
│   ├── weather_json_to_csv.ipynb                # Converts JSON response to CSV
│   ├── create_sql_db.ipynb                      # Creates DB and populates tables
│   └── analysis.ipynb                           # Final analysis & visualization notebook
│
├── outputs/
│   ├── charts/                     # Visualizations like boxplots, heatmaps, time series
│   └── reports/                    # Summary insights and key observations (optional)
│
├── scripts/
│   ├── raw_combined_file.py        # Combines uncleaned monthly thermostat CSVs
│   └── utilities.py                # Reusable Python functions for EDA & preprocessing
│
├── uncleaned_thermostat_data/      # Original monthly thermostat CSVs before merging
├── .gitignore                      # Prevents pushing `.db`, processed data, etc. to Git
└── README.md                       # Project overview and execution instructions
</pre>

## Dataset 1: Thermostat Data (thermostat_data_cleaned_final.csv)

### Data Dictionary
| Variable Name          | Data Type | Description                                                    |
| ---------------------- | --------- | -------------------------------------------------------------- |
| `timestamp`            | object    | Date and time of thermostat reading (recorded every 5 minutes) |
| `system_setting`       | object    | HVAC setting preference (`cool` / `heat`)                      |
| `system_mode`          | object    | Actual system status (e.g., `compressorcooloff`, `heat`)       |
| `program_mode`         | object    | Program mode active at that time (`sleep`, `home`)             |
| `cool_set_temp_f`      | float64   | Temperature set for cooling in Fahrenheit                      |
| `heat_set_temp_f`      | float64   | Temperature set for heating in Fahrenheit                      |
| `current_temp_f`       | float64   | Current indoor temperature in Fahrenheit                       |
| `current_humidity_rh`  | float64   | Indoor relative humidity (%)                                   |
| `outdoor_temp_f`       | float64   | Outdoor temperature in Fahrenheit                              |
| `fan_sec`              | float64   | Fan runtime in seconds for the interval                        |
| `date`                 | object    | Date part extracted from timestamp                             |
| `hour`                 | int64     | Hour part of the timestamp                                     |
| `minute`               | int64     | Minute part of the timestamp                                   |
| `weekday`              | object    | Day of the week                                                |
| `month`                | object    | Month name                                                     |
| `fan_runtime_category` | object    | Categorized fan runtime (e.g., `Low`, `Medium`, `High`)        |

### Data Summary

- Total Records: 122,470

- Date Range: May 1, 2024 – July 2025

- Program Modes: home, sleep

- Most Common System Setting: cool (71,779 records)

- Fan Runtime (Seconds): Avg = 278s, Max = 300s

- Indoor Temp: Min = 62.1°F, Max = 79.1°F, Avg = 71.45°F

- Indoor Humidity: Min = 27%, Max = 73%, Avg = 52.26%

### Data Source

- Source: [Ecobee Smart Thermostat Data Export](https://www.ecobee.com/)

- Collected From: User’s personal smart thermostat via CSV export

- Collection Period: May 2024 – June 2025

- License: Private dataset for academic use (Capstone Project)

## Dataset 2: Weather Data (weather_data_cleaned_final.csv)

### Data Dictionary
| Variable Name      | Data Type | Description                                             |
| ------------------ | --------- | ------------------------------------------------------- |
| `timestamp`        | object    | Date and time of weather observation (hourly intervals) |
| `outdoor_humidity` | int64     | Outdoor relative humidity (%)                           |
| `wind_speed_kmh`   | float64   | Wind speed in kilometers per hour                       |
| `outdoor_temp_f`   | float64   | Outdoor temperature in Fahrenheit                       |

### Data Summary

- Total Records: 10,224

- Date Range: May 1, 2024 – June 30, 2025

- Outdoor Temp: Min = -4.54°F, Max = 96.08°F, Avg = 57.18°F

- Humidity: Min = 19%, Max = 100%, Avg = 70.88%

- Wind Speed: Min = 0.0 km/h, Max = 55.7 km/h, Avg = 11.09 km/h

### Data Source

- Source: [Open-Meteo Historical Weather API](https://open-meteo.com/)

- API Endpoint Used: Historical Hourly Forecast API

- Location: Based on user’s ZIP code

- License: Free for non-commercial use with attribution