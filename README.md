
# Smart Thermostat Energy Analysis: Exploring Indoor Climate & Energy Patterns

## Project Overview
This project analyzes smart thermostat and weather data to uncover patterns in HVAC usage, temperature control, and energy efficiency. The goal is to derive insights that help balance indoor comfort, energy cost, and environmental factors. The data includes over 40,000 records of 5-minute thermostat logs and hourly weather data collected over a 1-year period.

## Project Objective
To evaluate how indoor HVAC behavior correlates with outdoor weather and usage patterns, and to identify opportunities to optimize comfort and efficiency. Key questions addressed include:

- How often does the HVAC run daily?
- How closely does the actual indoor temperature align with setpoints?
- What is the relationship between outdoor temperature and fan runtime?

## Technologies Used

| Tool                       | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| **Python (Pandas, NumPy)** | Data cleaning, transformation, aggregation   |
| **Matplotlib / Seaborn**   | Visualization and plotting                   |
| **SQLite3**                | Storing cleaned data for structured analysis |
| **Jupyter Notebook**       | Interactive analysis and presentation        |
| **Git & GitHub**           | Version control and project sharing          |
| **VS Code**                | Code Editor                                  |

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
│   ├── clean_thermostat_data.ipynb              # Raw thermostat data cleaning
│   ├── clean_weather_data.ipynb                 # Raw weather data cleaning
│   ├── clean_thermostat_data_final.ipynb        # Finalized thermostat preprocessing
│   ├── clean_weather_data_final.ipynb           # Finalized weather preprocessing
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