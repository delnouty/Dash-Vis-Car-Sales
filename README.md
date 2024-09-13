# Car Sales Dashbord

**This application is an Automobile Sales Dashboard built using Dash, a Python framework for building analytical web applications. It visualizes historical automobile sales data, providing insights through various interactive charts. Users can select between yearly statistics and recession period statistics to explore trends and patterns in automobile sales.**

### Features

- **Yearly Statistics**:
  - Displays yearly average automobile sales using a line chart.
  - Shows total monthly automobile sales using a line chart.
  - Visualizes the number of vehicles sold by vehicle type using a bar chart.
  - Illustrates total advertisement expenditure by vehicle type using a pie chart.

- **Recession Period Statistics**:
  - Shows average automobile sales fluctuations over recession periods using a line chart.
  - Displays the average number of vehicles sold by vehicle type during recession periods using a bar chart.

## First solution

- dash_Cars_Sales.py - **object-oriented solution**. This application is designed using object-oriented principles, encapsulating the functionality within a class called **AutomobileDashboard**. This approach enhances modularity, making the code more organized and easier to maintain. By creating an instance of the **AutomobileDashboard class**, you can initialize the dashboard, set up the layout, define callbacks for interactivity, and run the server. This structure promotes reusability and scalability, allowing for easy updates and extensions in the future.

### Class: AutomobileDashboard

* Attributes:
  - data: A DataFrame containing the automobile sales data loaded from a CSV file.
  - app: An instance of the Dash application.
  - color_map: A dictionary mapping vehicle types to specific colors for consistent chart coloring.
  - month_order: A list defining the order of months for sorting and displaying monthly data.
  - vehicle_type_order: A list defining the order of vehicle types for sorting and displaying vehicle type data.
  - year_list: A list of years from 1980 to 2023 for the dropdown menu.
  - dropdown_options: A list of options for the statistics type dropdown menu.
* Methods:
  - _ _init__(self, data_url): The constructor method that initializes the class attributes, loads the data, and sets up the layout and callbacks.
  - layout(self): Defines the layout of the dashboard, including the title, dropdown menus, and output container.
  - callbacks(self): Defines the callback functions for interactivity. These functions update the dropdown menu and output container based on user selections.
  - update_input_container(selected_statistics): Enables or disables the year dropdown based on the selected statistics type.
  - update_output_container(selected_statistics, input_year): Updates the output container with the appropriate charts based on the selected statistics type and year.

## Second solution

* dash_IBM_DV.py - This solution itself primarily relies on functional programming concepts, where functions (such as the callback functions) take inputs and return outputs based on user interaction. The app is designed to be modular, with clear separation of concerns between data processing and visualization. The app is built using declarative programming and event-driven programming, two common paradigms in web development, particularly for interactive dashboards like this one.
  - Declarative Programming: Dash, a framework built on top of Flask, React.js, and Plotly, follows a declarative approach. In this app, you define the structure (layout) of the dashboard using high-level components (html.Div, dcc.Dropdown, etc.) and specify the desired outcome (charts) without directly manipulating the DOM or focusing on how to render elements step by step. For example, you describe the dropdown and chart elements, and Dash takes care of rendering them based on the given data.
  - Event-Driven Programming: The app relies heavily on callbacks (functions that automatically trigger when user input changes), making it event-driven. For example, when a user selects a different year or statistic type, an event is triggered that updates the displayed charts. This dynamic behavior is central to Dash apps. Input-output binding in Dash (Input, Output) is an example of handling events in response to user actions.
  - Reasons It's Not Primarily Object-Oriented:
    -- No Classes or Objects: The code does not define any custom classes or objects, which are the key components of OOP. Instead, it primarily uses functions to handle tasks (e.g., update_output_container).
    -- No Inheritance or Polymorphism: OOP concepts like inheritance, encapsulation, and polymorphism are not used here. The app is built using Dash components (which themselves might be object-oriented internally), but the app code is not structured in an OOP way.
    -- Declarative Approach: Dash components (e.g., html.Div, dcc.Dropdown) are used declaratively, and their behavior is managed through functions, not through creating objects or class hierarchies.


