#function to clean up data recorded with the flowmeters. This uses a hampel function and pandas.
#Window size is window of data points to be considered
#n= the number of standard deviations of the window of data points to be considered an outlier


# Imports
from hampel import hampel
import pandas as pd
import matplotlib.pyplot as plt

#read dataframe from excel
df = pd.read_excel (r'C:\Users\s.janssens.CI\PycharmProjects\filter_flow_data\20220615_142431f_Flowmeter_test_source_trans.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'



#requires a dataframe, the column to be filtered and name of the filtered data
def filtering(df,column, filteredname):
    #make a series out of the column since this is needed for the hampel filter
    filtered_series = df[column].squeeze()

    #Use the hampel filter
    outlier_indices = hampel(ts = filtered_series, window_size = 12, n=1)

    #remove the outliers
    filtered_d = filtered_series.drop(outlier_indices)
    filtered_d.values.tolist()

    #put the outliers and the filtered values in seperate columns in dataframe
    df['outliers']=(df.loc[outlier_indices])[column]
    df[filteredname]=filtered_d

    # calculate unfiltered mean and standard deviation
    means = df.groupby('no.').mean().reset_index()
    stds = df.groupby('no.').std().reset_index()

    #calculate the mean and standard deviation of the filtered data
    means_filtered=df.groupby('no.').mean().reset_index()
    stds_filtered=df.groupby('no.').std().reset_index()


    #write some results to excel
    df.to_excel("filtered_flow_data.xlsx")
    means_filtered.to_excel("filtered_means.xlsx")
    stds_filtered.to_excel("filtered_stds.xlsx")

    #plot the original series
    plt.plot(df['runtime'],df[column], color="black")
    #plot the filtered series
    plt.plot(df['runtime'],df[filteredname], color="yellow",alpha= 0.3)


    #plot the outliers
    #plt.scatter(outlier_indices, filtered_series[outlier_indices], color="blue",marker='+')
    plt.scatter(df['runtime'], df['outliers'], color="blue",marker='+')
    plt.grid( linestyle='-.', linewidth=0.5)
    #plot the filtered means
    plt.scatter(means_filtered['runtime'],means_filtered[filteredname], color="green",marker='*')
    #plot the unfiltered means
    plt.scatter(means['runtime'],means[column], color="red",marker='.')




#column='q C1'
#column='read_flow C2'
column='read_flow M_1'
filteredname='filtered M1'

filtering(df,column, filteredname)