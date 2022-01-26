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