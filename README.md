# Car Sales Dashbord

**This application is an Automobile Sales Dashboard built using Dash, a Python framework for building analytical web applications. It visualizes historical automobile sales data, providing insights through various interactive charts. Users can select between yearly statistics and recession period statistics to explore trends and patterns in automobile sales.**

## Key features include:

- Yearly Statistics: Displays yearly average automobile sales, total monthly sales, sales by vehicle type, and advertisement expenditure by vehicle type.
- Recession Period Statistics: Shows average automobile sales fluctuations and sales by vehicle type during recession periods.
- The dashboard is designed to be user-friendly, with dropdown menus for selecting report types and years, making it easy to navigate and analyze the data.

## Two solutions

- dash_Cars_Sales.py - **object-oriented solution**. This application is designed using object-oriented principles, encapsulating the functionality within a class called **AutomobileDashboard**. This approach enhances modularity, making the code more organized and easier to maintain. By creating an instance of the **AutomobileDashboard class**, you can initialize the dashboard, set up the layout, define callbacks for interactivity, and run the server. This structure promotes reusability and scalability, allowing for easy updates and extensions in the future.

### Features

- **Yearly Statistics**:
  - Displays yearly average automobile sales using a line chart.
  - Shows total monthly automobile sales using a line chart.
  - Visualizes the number of vehicles sold by vehicle type using a bar chart.
  - Illustrates total advertisement expenditure by vehicle type using a pie chart.

- **Recession Period Statistics**:
  - Shows average automobile sales fluctuations over recession periods using a line chart.
  - Displays the average number of vehicles sold by vehicle type during recession periods using a bar chart.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automobile-sales-dashboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd automobile-sales-dashboard
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the dashboard, execute the following command:
```bash
python app.py

  




