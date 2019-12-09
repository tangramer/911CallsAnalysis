
# COMPONENT  SPECIFICATIONS


# 1. Data extraction (clean data)
### a. The raw data have more than 100 call types. These types need to be better classified into fewer than 10 categories (fewer than 5 is the best)
### b. Remove unnecessary data (e.g. incident number)
### c. Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident numbers in a block (e.g. the sum fire incidents in a block vs. the average temperature in the same block)
### 2 functions are included to realize the data extraction and reorganization: …
## 1.1 ReadCalls
### Name: ReadCalls(data, year (optional), data to pick in each year, data merge similar types or not)
### What it does: 
#### a. Read 911 calls dataset. If the year(s) are specified, then only the calls of certain years will be included. Otherwise it reads all the data from the dataset. 
#### b. Pick given number of calls in a year randomly. If not specified, all data of the year will be read. The raw data updates every 5 min. It is a huge dataset to process if pick number is no specified.
#### c. If choose to merge similar call types, calls such as “brush fire”, “car fire”, “house fire” will be labelled as a new general type “fire”. If this is not specified, call types will not be modified.

### Inputs: raw dataset, year (optional), data to pick in each year, merge=Y/N (optional)
### Output: dataframe of selected year, with types merged or not. Useless columns are dropped. 


## 1.2 AssignBlocks
### Name: AssignBlocks(dataframe)
### What is does: Divide Seattle into blocks. Add the block code column to the dataframe. Later analysis is based on incident numbers in a block (e.g. the sum fire incidents in a block vs. the average temperature in the same block)
### Input: dataframe
### Output: dataframe with a new column of block/community code.

# 2. Map visualization of 911 calls
## 2.1 ShowMap
### 	Name showmap()
### 	What it does: show 911 calls on Seattle map. Users can select call type and browse the distribution changes along time.
### 	Input: dataframe from last component, datapoints from user input.
	
# 3. Interactive visualization of different types of 911 calls (Statistic data)
## 3.1 clean data 
#### 	Clean the data from the original dataset. There were many strange numbers and records in the dataset that needs correction. For example, in the 911 record call in 2019, there were a few calls records that showed the date at 2020, which is simply not possible. These wrong or misrecorded data needs to be removed. Also interactive visualization using altair requires the data as a pandas dataframe in the long-form version. The original data set has to be modified to enable the visualization.

## 3.2 create interaction on the graph
#### 	Information of interest are different for different types of users. For example, firefighting officials might be more interested in 911 calls of fire alarm and wish to know its distribution geographically and chronically so they can redistribute their forces according to the pattern. However, robbery and stabbing calls are less important to them. Therefore we plan to create an interactive graphs that provide many options that users can choose from to show/hide information upon request  
### Name: Interactive graph
### What is does: provide the opportunity to the users to pick the particular types of 911 calls of interest and show some analysis/visualization according to the requirement of the users.
### Input: users’ choice of information and types of analysis
### Output: modified visualization according to users’ request

# 4. Linear regression of specific 911 call type and temperature
## 	4.1 relation of calls and temperatures
### 		Name: TBD
### 		What is does: To answer the question we raised in this project: is the 911 emergency calls related to the environment temperatures. 
### 		Input: dataframe_911calls, call_type (optional), dataframe_temerature
### 		Output: a score from 0 to 1 to show how relevant the 911 call incidents are to the local temperatures.



```python

```
