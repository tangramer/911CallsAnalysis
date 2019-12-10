'''
This module deal with statistical analysis of the different types of 911 calls over time
and use altair for the output to provide relationship between the data and interaction
with the potential users
'''

import altair as alt
from vega_datasets import data

# properly render the altair environment
alt.renderers.enable('notebook')

# upload data for analysis
dfweather = pd.read_csv("C:/Users/Runbang Tang/Downloads/Road_Weather_Information_Stations.csv",nrows=20000) 
df = pd.read_csv("C:/Users/Runbang Tang/Downloads/Seattle_Real_Time_Fire_911_Calls2.csv",nrows=20000)

#data clean process to make the data appropirate for the altair analysis
k=0
for i in df["Datetime"]:
    df["date"][k] = i.date()
    k+=1
t = ['Aid Response', 'Trans to AMR', 'Auto Fire Alarm', 'Medic Response', 'Aid Response Yellow','Rescue Elevator',
     'MVI - Motor Vehicle Incident','Fire in Building','Natural Gas Leak','Car Fire Freeway']
numbers = [0,0,0,0,0,0,0,0,0,0]
dfb0 = df[df["date"] == b[0]]
bnumbers = []
Types = []
bdates = []
for i in range(113):
    numbers = [0,0,0,0,0,0,0,0,0,0]
    dfw = df[df["date"]==b[i]]
    for k in range(len(dfw)):
        if df.iloc[k]["Type"] == "Aid Response":
            numbers[0]+=1
        elif df.iloc[k]["Type"] == 'Trans to AMR':
            numbers[1]+=1
        elif df.iloc[k]["Type"] == 'Auto Fire Alarm':
            numbers[2]+=1
        elif df.iloc[k]["Type"] == 'Medic Response':
            numbers[3]+=1
        elif df.iloc[k]["Type"] == 'Aid Response Yellow':
            numbers[4]+=1
        elif df.iloc[k]["Type"] == 'Rescue Elevator':
            numbers[5]+=1
        elif df.iloc[k]["Type"] == 'MVI - Motor Vehicle Incident':
            numbers[6]+=1
        elif df.iloc[k]["Type"] == 'Fire in Building':
            numbers[7]+=1
        elif df.iloc[k]["Type"] == 'Natural Gas Leak':
            numbers[8]+=1
        elif df.iloc[k]["Type"] == 'Car Fire Freeway':
            numbers[9]+=1
    bnumbers.append(numbers)
    Types.append(['Aid Response', 'Trans to AMR', 'Auto Fire Alarm', 'Medic Response', 'Aid Response Yellow',
                  'Rescue Elevator','MVI - Motor Vehicle Incident','Fire in Building','Natural Gas Leak','Car Fire Freeway'])
    bdates.append([pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i]),
                  pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i]),pd.Timestamp(b[i])])
bnumbers2 = []
bdates2 =[]
Types2 = []
for l in bnumbers:
    for s in l:
        bnumbers2.append(s)
for l in bdates:
    for s in l:
        bdates2.append(s)
for l in Types:
    for s in l:
        Types2.append(s)
# intialise data of lists. 
data = {'Date':bdates2, 
        'Type':Types2,
        "counts":bnumbers2} 
  
# Create DataFrame 
df1 = pd.DataFrame(data) 

source = df1

scale = alt.Scale(domain=['Aid Response', 'Trans to AMR', 'Auto Fire Alarm', 'Medic Response', 'Aid Response Yellow',
                         'Rescue Elevator','MVI - Motor Vehicle Incident','Fire in Building','Natural Gas Leak',
                          'Car Fire Freeway'],
                  range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd',
                         '#BD9467','#67BD94','#BD67BB','#6967BD','#BBBD67'])
color = alt.Color('Type:N', scale=scale)

'''
altair output as a sample test for the data analysis of different 911 types of Calls
'''
# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

#slider = alt.binding_range(min=0, max=100, step=1, name='cutoff:')
#selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
#                                bind=slider, init={'cutoff': 50})

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_line(point=True).encode(
    alt.X('monthdate(Date):T', title='Date',),
    alt.Y('counts:Q',
        title='Daily counts of records',
        #scale=alt.Scale(range=[0,100])
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    #size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=550,
    height=300
).add_selection(
    brush
).transform_filter(
    click
)


# Bottom panel is a bar chart of 911 type
bars = alt.Chart().mark_bar().encode(
    x='counts:Q',
    y='Type:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=550,
).add_selection(
    click
)
alt.vconcat(
    points,
    bars,
    data=df1,
    title="Sample Test"
)

