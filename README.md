# Squirrel_Tracker

## What is it?

Squirrel Tracker Django project for Tools for Analytics course

We are two students at Columbia Univerisity, and we have created a Django app which can be used to track squirrels' locations and behaviours in NYC Central Park. The data used in the app was imported from the [2018 Central Park Squirrel Census Data.](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)


The app created has the following functions:
1. Management command function: 
      
       a. import_squirrel_data: A command that can be used to import the data from the 2018 census file (in CSV format) 
       b. export_squirrel_data: A command that can be used to export the squirrel data in CSV format
       
2. Views in the app:

       a. /map/ shows a map marked with random 100 squireel locations in the Central Park, New York
       b. /sightings/ shows a list of squirrels indicated by their Unique Squirrel IDs and you can edit the squirrel information by clicking on the Unique Squirrel ID. After submission, the database of the squirrels will change accordingly.
       c. /sightings/add/ gives an empty form and you can add your customized squirrel by filling out the attributes. After submission, the database will change accordingly. Notice: the Date format: yyyy-mm-dd.
       d. /sightings/stats shows 5 very important statisitics about the squirrels.



## Group name and section
Project Group **2**
Section **1**
## Members
**UNIs**: [cq2223, hz2703] 

## The link to the server running our application
https://tfa-2021-spring-cq2223.df.r.appspot.com/

 
