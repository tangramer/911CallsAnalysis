# final-project
Xiaojing Xia 
Nicolas Cardozo
Runbang Tang

Our final project repository is here: https://github.com/tangramer/final-project.git

Our presentation slides is here: https://docs.google.com/presentation/d/1QlV3RJOhp-bY88lfoSlitvNlbrZf6QqFthnPe4m9_ng/edit#slide=id.g73d3cd243b_2_2

#Our functional specification:
User Profile: Users of different backgrounds can selectively browse the data they are interested in. For example, users can choose to show only fire alarm 911 calls which might be more interesting to people in the firefighting department. Officials from hospitals might be more curious on the 911 medic response data for medic response to try to redistribute their forces according to the geographical patterns in seattle.    Users can track the changes by selecting time/date.
Use Case: Users can select two main  data to show:
  1.911 calls distributions of different types on a Seattle map
  2.Statistic data of blocks / communities
  3.Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident numbers in a block (e.g.    the sum fire incidents in a block vs. the average temperature in the same block)


#Our component specification:

1.Data extraction (clean data)
The raw data have more than 100 call types. These types need to be better classified into fewer than 10 categories (fewer than 5 is the best)
Remove unnecessary data (e.g. incident number)
Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident numbers in a block (e.g. the sum fire incidents in a block vs. the average temperature in the same block)
	X functions are included to realize the data extraction and reorganization: …
1.1 ReadCalls
Name: ReadCalls(data, year (optional), merge similar types or not)
What it does: Read 911 calls dataset. If the year(s) are specified, then only the calls of certain years will be included. Otherwise it reads all the data from the dataset. If choose to merge similar call types, calls such as “brush fire”, “car fire”, “house fire” will be labelled as a new general type “fire”. If this is not specified, call types will not be modified.
	Inputs: raw dataset, year (optional), merge=Y/N (optional)
	Output: dataframe of selected year, with types merged or not.


2.Interactive map visualization of different types of 911 calls

3.Linear regression of specific 911 call type and temperature

Our detailed project proposal is here:https://docs.google.com/document/d/1yjN52TQ4Yr5t3MxTkFJ5rfq4hBzpksk7TKGCctVqVTY/edit?ts=5dbfa164#

