# Submission README  
### INFO 4602-5062  
### Project 2 
### Team 12

#### Visualization 1  
Visualization 1 displays the retention rate year-by-year of students who declared their major at different times in college. We then split this up by male and female students. You can select which data set you'd like to see by selecting from the dropdown and can see the specific graduation rate by hovering over the data. 

**Data**
To get the data, we manipulated the original datafile and split it based on the 4 different time periods that colleges allowed their students to declare their major (Upon Enrollment, End of 1st Year, End of 2nd Year and Other). From there we calculated retention as (#Total Students - #New Enrolled - #Transfer)/#Total Students for each gender. There were some inconsistencies with the data (such as there being more new enrolled students than total students for certain years in the Upon Enrollment Category). This resulted in a negative retention rate which we replaced as zero.

**To Run**
Run a server and select visualization 1

#### Visualization 2: Comparing number of female ethnic students in the 2015-2016 school year 
Visual 2 looked into comparing the 6 ethnicities given in the dataset (Asian, Black/African American, Hispanic, Alaskan/Native
American, and Islanders) in the 2015-2016 school year. The visual was made with the intent goal of seeing which ethnicities are
being represented less than others to hopefully craft new strategies for both bringing in and retaining those students.
The visual is a simple pie chart, with each ethnicity represented by a wedge.
When one of the wedges is hovered over, it displays the number of students below the visual.

**To Run**
To create the dataset used in the visual, run the create_vis2_dataset.py file with the raw dataset,
you may need to install Python's Pandas first

Then open up a server and run visualization 2

#### Visualization 3: Graduation trends by gender and when a student declares their major  
This visualization helps to answer several questions: Are the number of graduates 
increasing or decreasing? How does the number of female graduates compare to the number of male graduates. 
Does the timing of declaring a major affect the number of graduates and is there a difference between females and males? 
This visualization is an HTML dashboard containing 3 plots. 
* total graduations by year (m v. f)
* female graduation trend by when major is declared
* male graduation trend by when major is declared  

The two smaller line charts contain interactive elements. By clicking on the elements in the legend, the user can hide/show lines by clicking on the legend.
  
**To run**, run a server and select Visualization 3

**Design Process:** Goal of the visualization was to visualize and compare graduation rates for both males and females. The graphs seemed like a good representation to see if there were any trends in where graduation rates increased or decreased. 

#### Team Roles
* Kristin Robinson: Visualizaton 3, design process, coding
* Joel Marquez: Visualization 1, design process, coding
* Franklin Harvey: Visualization 1, design process, coding
* Julio Lopez: Visualization 2, design process, coding
* Jocelyne Agboglo: Visualiation 3, design process, ReadMe submission

