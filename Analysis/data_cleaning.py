"""This module will allow the data obtained from our 2 data sets to be cleaned and merged together to allow for downstream analysis."""
def create_csv():
    url = "Seattle_Real_Time_Fire_911_Calls.csv"
    df = pd.read_csv(url)
    return(df)

def clean_dataframe(df, column_list, length):
    """This module will clean-up our dataframe by making general groups
    of calls (medical, fire, police) and also by removing dates
    that are shown to occur in the future."""
    list_of_actual_columns = list(dataframe.columns.values)
    for each_column in column_list:
        if each_column not in list_of_actual_columns:
            return False
    if number_of_rows < 1000:
        return False
    return True

    category_value_counts = df['Type'].value_counts()
    category_value_counts.to_csv('category_value_counts')
    cdf = pd.read_csv('category_value_counts')
    df = df.merge(cdf, left_on='Type', right_on='OldCategory')
    df['Datetime'] =  pd.to_datetime(df['Datetime'])
    df[(df['Datetime'] > '2019-12-31')]
    df.sort_values(by='Datetime', ascending=False)
    
