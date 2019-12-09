# final-project
Xiaojing Xia,
Nicolas Cardozo,
Runbang Tang,

The project repository can be found here: https://github.com/tangramer/final-project.git

Presentation slides are here: https://docs.google.com/presentation/d/1QlV3RJOhp-bY88lfoSlitvNlbrZf6QqFthnPe4m9_ng/edit#slide=id.g73d3cd243b_2_2

1) Functional specification:

      User Input: Users of different backgrounds can selectively browse 911 call data they are interested in, in various parts of Seattle. For example, users can choose to show fire alarm 911 calls which might be more interesting to people in the firefighting department. Officials from hospitals might be more curious on the 911 medic response data for medic        response to try to redistribute their forces according to the geographical patterns in seattle. 
       
      Users will be able to track the changes by selecting time/date.
   
      Use Case: Users can select two main  data to show:
  		1) 911 calls distributions of different types on a map of Seattle
  		
	2) Statistic data of blocks / communities
  	
	3) Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident                    numbers in a block (e.g. the sum fire incidents in a block vs. the average temperature in the same block)


2) Component specification:
     Data extraction (clean-up data)
	
      1.1) The raw data have more than 100 call types. These types need to be better classified into fewer than 10        		       categories (fewer than 5 is the best)
	   
      1.2) Remove unnecessary data (e.g. incident number)
	  
      1.3) Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident                    numbers in a block (e.g. the sum fire incidents in a block vs. the average temperature in the same block)


3) Interactive map visualization of different types of 911 calls
	3.1) The user will be able to select based on the year/type of 911 call they would like to know more about. They will 		   then be given an interactive map that they will be able to use to see where/when the 911 call was made and what                type of call it was. 

4) Linear regression of specific 911 call type and temperature

5) Our detailed project proposal is here:https://docs.google.com/document/d/1yjN52TQ4Yr5t3MxTkFJ5rfq4hBzpksk7TKGCctVqVTY/edit?ts=5dbfa164#

