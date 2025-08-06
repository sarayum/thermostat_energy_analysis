
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

1. Install Visual Studio Code (VS Code)

- Download and install VS Code from:
 👉 https://code.visualstudio.com/

2. Install Python

- Download and install Python (version 3.10+) from:
 👉 https://www.python.org/downloads/
- During installation, check “Add Python to PATH” option.

3. Install Python and Jupyter Extension in VS Code
- Open VS Code → Go to Extensions (⇧⌘X / Ctrl+Shift+X)
- Search for and install:
 - Python extension by Microsoft
 - Jupyter extension by Microsoft

4. Set up a Virtual Environment (Recommended)
Run the following commands in the VS Code terminal:

#### Create virtual environment
python -m venv venv

#### Activate the environment

##### Windows:
venv\Scripts\activate

##### macOS/Linux:
source venv/bin/activate
