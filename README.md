# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Project Description
The **Redbus Data Scraping and Filtering with Streamlit Application** provides an automated solution for collecting, analyzing, and visualizing bus travel data from the Redbus website. This project utilizes **Selenium** for web scraping, extracting details like routes, schedules, prices, and seat availability. The scraped data is stored in a **MySQL** database, and the **Streamlit** application queries this data using **PyMySQL** to display it as a user-friendly data frame with dynamic filtering options.

By offering an intuitive interface and effective data presentation, this project helps stakeholders make informed decisions in the transportation industry, improving operational efficiency and strategic planning.

---

## Features
- **Automated Data Scraping**: Extracts bus details from Redbus using Selenium for 10 different states.
- **Data Conversion**: Converts the extracted data to CSV format.
- **Data Storage**: Stores the CSV data into a MySQL database.
- **Interactive Dashboard**: Developed using Streamlit for real-time data visualization and analysis.
- **MySQL Integration**: Connects to the database using PyMySQL to query data based on user inputs.
- **Dynamic Filtering**: Users can filter buses based on:
  - Bus Type
  - Route
  - Price Range
  - Star Rating
  - Seat Availability
- **Data Analysis**: Provides insights using SQL queries based on user-defined filters.

---

## Tech Stack
- **Python**
- **Selenium**
- **Streamlit**
- **MySQL**
- **PyMySQL**
- **Pandas**
- **Matplotlib / Seaborn (Optional for Visualization)**

---

## Dataset Structure
The following table represents the structure of the SQL database used for storing the scraped data:

| Column Name        | Data Type   | Description                                      |
|--------------------|-------------|--------------------------------------------------|
| id                 | INT         | Primary Key (Auto-increment)                    |
| route_name         | TEXT        | Bus Route information for each state transport  |
| route_link         | TEXT        | Link to the route details                       |
| busname            | TEXT        | Name of the bus                                 |
| bustype            | TEXT        | Type of the bus                                 |
| departing_time     | TIME        | Departure time                                  |
| duration           | TEXT        | Duration of the journey                         |
| reaching_time      | TIME        | Arrival time                                    |
| star_rating        | FLOAT       | Rating of the bus                               |
| price              | DECIMAL     | Price of the ticket                             |
| seats_available    | INT         | Number of seats available                       |

---

## Installation Instructions
Follow these steps to set up the project locally:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-repo/redbus-data-scraping.git
    cd redbus-data-scraping
    ```
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Perform Data Scraping:**
    - Run the Selenium scraper to extract data from Redbus for 10 states.
    - The scraped data will be stored in CSV files.
4. **Set Up MySQL Database:**
    - Create a database using MySQL.
    - Import the CSV files into the database using SQL queries or MySQL import functions.
5. **Configure Database Connection:**
    - Update `config.py` with your MySQL database credentials.
6. **Launch the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

---

## Usage Guide
1. Open the application in your browser using the Streamlit link.
2. Enter necessary input details using the Streamlit sidebar.
3. Streamlit will generate a SQL query using the inputs.
4. The query will be executed using PyMySQL to retrieve data from MySQL.
5. The results will be displayed in a data frame on the application interface.

---

## Future Enhancements
- Implement **real-time data updates** with scheduled scraping.
- Add **data visualization** for enhanced insights.
- Provide **export options** for filtered data.
- Enhance error handling and logging.

---

