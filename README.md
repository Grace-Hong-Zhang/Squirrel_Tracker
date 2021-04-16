# Squirrel_Tracker

## What is it?

Squirrel Tracker Django project for Tools for Analytics course

We are two students at Columbia Univerisity, and we have created a Django app which can be used to track squirrels' locations and behaviours in NYC Central Park. The data used in the app was imported from the [2018 Central Park Squirrel Census Data.](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)


The app created has the following functions:
1. Management command function: 
      
       a. import_squirrel_data: A command that can be used to import the data from the 2018 census file (in CSV format) 
       b. export_squirrel_data: A command that can be used to export the squirrel data in CSV format
       
2. Views in the app:

       a. /map/ randomly selects 100 squirrels and presents their coordinates on the map, providing us with the general range of activity of squirrels.
       b. /sightings/ lists the information of all squirrels. The first column is the unique squirrel id of each squirrel. We can click it to view the details of this squirrel.
       c. /sightings/update/ We can click it to modify and update the details of this squirrel.
       d. /sightings/add/ When we see a new squirrel, we can register all the information of the squirrel through this function.
       e. /sightings/stats/ statistics some important information of squirrel population in Central Park, such as age ratio, fur color ratio and so on.



## Group name and section
Project Group **2**
Section **1**
## Members
**UNIs**: [cq2223, hz2703] 

## The link to the server running our application
https://tfa-2021-spring-cq2223.df.r.appspot.com/

 
