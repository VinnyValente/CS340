# Grazioso Salvare Animal Shelter Dashboard

## Project Overview
Grazioso Salvare, an international rescue-animal training company, collaborates with animal shelters around Austin, Texas, to identify dogs suitable for search-and-rescue training. This dashboard enables users at Grazioso Salvare to easily view, filter, and analyze shelter data to identify potential rescue dogs for various operations.

## Functionality
- **Display an interactive data table** of shelter animals.
- **Filter the table** based on rescue type: Water, Mountain, Disaster, or display all animals.
- **Visualize breed distribution** with a pie chart.
- **Display geolocation** on a map highlighting the location of a selected animal.
  
![1](https://github.com/user-attachments/assets/11fda99a-baad-48de-bd43-cf5704fe4239)
![2](https://github.com/user-attachments/assets/c8bc566d-1419-4d45-90b2-c0712c7c0af9)
![3](https://github.com/user-attachments/assets/10b2748f-706b-43b8-be67-ca4aca6e6802)
![4](https://github.com/user-attachments/assets/0e4ebc77-f5f1-4504-b8a8-65949b5dd7ee)

## Tools & Technologies
- **MongoDB**: Used as the primary database for storing animal shelter data. MongoDB is a NoSQL database known for its flexibility, performance, and ability to interface with Python.
- **Python**: The core programming language for data manipulation and dashboard functionality.
- **Dash by Plotly**: A web application framework used for creating the interactive dashboard and data visualizations.
- **Dash-Leaflet**: Provides geolocation and mapping capabilities.
- **Plotly Express**: Enables the creation of interactive graphs and plots for data visualization.

## Resources & Software Applications
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)

## Steps to Reproduce the Project
1. **Set up MongoDB**: Install MongoDB and populate it with animal shelter data.
2. **Connect to MongoDB**: Use Python's `pymongo` library to establish a connection to your MongoDB instance.
3. **Create CRUD operations**: Implement the necessary Create, Read, Update, and Delete operations in `AnimalShelter.py`.
4. **Design the Dashboard**: Use Dash components to build the layout of the dashboard.
5. **Implement Callbacks**: Add callback functions to handle user interactions and update data visualizations dynamically.
6. **Test & Deploy**: Ensure that the dashboard works as intended, then deploy it on a server.

## Challenges & Solutions
- **Challenge 1: Handling various data types from MongoDB, especially the ObjectID field**  
  **Solution**: Used `DataFrame.drop` from the pandas library to remove the `_id` field before passing data to Dash components.
  
- **Challenge 2: Providing interactive data visualizations that respond to user filters**  
  **Solution**: Utilized Dash's callback functionality to monitor changes in dropdown selections and update the visual components accordingly.

- **Challenge 3: Displaying geolocation data for selected animals**  
  **Solution**: Integrated `Dash-Leaflet` for interactive maps and utilized callback functions to update the map based on the selected animal's data.

## Conclusion
The Grazioso Salvare Animal Shelter Dashboard provides an intuitive and interactive platform for identifying potential rescue dogs. It combines MongoDB's powerful data management capabilities with Dash's interactive and visually engaging tools.
