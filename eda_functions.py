#Libraries
import matplotlib.pyplot as plt

#Functions

def check_data_day(df, year, month):
    ''' This function prints the statistics about number of registers available per day
    given a month and a year

    INPUT: 
            df (dataframe)
            year (string)
            month (string)
    OUTPUT: None
    '''
    
    #Print total number of registers in a month
    num_registers = df[(df.year==year) & (df.month==month)].month.value_counts().to_list()[0]
    print("There are {} registers for this month".format(num_registers))
    
    #Print the total number of days considered in that month
    num_days = len(set(df[(df.year==year) & (df.month==month)].day.value_counts().keys().sort_values().to_list()))
    print("There are {} days registered".format(num_days))
    
    #Print basic statistics about the register in the month
    measure_per_day = df[(df.year==year) & (df.month==month)].day.value_counts().to_list()
    print("The minimum amount of registers in a day for this month was {}".format(min(measure_per_day)))
    print("The maximum amount of registers in a day for this month was {}".format(max(measure_per_day)))
    print("The mean amount of registers for this month was {}".format(sum(measure_per_day)/len(measure_per_day)))
    
    #Show number of register per day as a bar plot
    df[(df.year==year) & (df.month==month)].day.value_counts().sort_index().plot(kind = 'bar')
    plt.title("Number of registers per day from month {} of {}".format(month, year));
    plt.xlabel('Day')
    plt.ylabel('Number of registers')
    plt.pause(0.05) #Add to show plot during for loop

def check_data_month(df, year):
    ''' This function prints the number of registers available per year and also per month
    INPUT: 
            df (dataframe)
            year (string)
    OUTPUT: None
    '''
    df = df[df.year==year]
    print("Checking if there is only data from the selected year: ")
    print(df.year.value_counts())
    print("Checking the months available: ")
    print(df.month.value_counts())

def df_dimensions(df):
    '''
    INPUT: Dataframe
    OUTPUT: Message - Number of the dataframe rows and columns
    '''
    num_rows = df.shape[0]
    num_cols = df.shape[1]
    print("The dataframe has {} rows and {} columns".format(num_rows, num_cols))
    
def cols_missing_values(df):
    '''
    INPUT: Dataframe
    OUTPUT: Message - Number of columns with missing data and the name of the columns
    '''
    no_nulls = set(df.columns[df.isnull().mean()>0])
    print("There are {} from {} columns with missing values".format(len(no_nulls), df.shape[1]))
    print("Columns with no missing values = ", no_nulls)

def most_missing_values(df, threshold):
    '''
    INPUT: Dataframe and threshold (set the percentage from 0 to 1 of how much data should be missing)
    OUTPUT: Message - Number and the name of the columns missing more than X percentage of data
    '''
    most_missing_cols = set(df.columns[df.isnull().mean()> threshold])
    print("There are {} from {} columns with  more than {}% of missing values".format(len(most_missing_cols), df.shape[1], threshold*100))
    print("Columns more than {}% of values missing = ".format(threshold*100))
    print(most_missing_cols)
    
def categorical_cols(df):
    '''
    INPUT: Dataframe
    OUTPUT: Message - Number of columns with categorical data and the name of the columns
    '''
    cat_cols = list(df.select_dtypes(include=["object"]).columns)
    print("There are {} from {} columns with categorical data".format(len(cat_cols), df.shape[1]))
    print("Columns categorical data = ", cat_cols)
    
def numerical_cols(df):
    '''
    INPUT: Dataframe
    OUTPUT: Message - Number of columns with numerical data and the name of the columns
    '''
    num_cols = list(df.select_dtypes(include=["float", "int"]).columns)
    print("There are {} from {} columns with numerical data".format(len(num_cols), df.shape[1]))
    print("Columns numerical data = ", num_cols)