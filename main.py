#function to clean up data recorded with the flowmeters. This uses a hampel function and pandas.
#Window size is window of data points to be considered
#n= the number of standard deviations of the window of data points to be considered an outlier


# Imports
from hampel import hampel
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel (r'C:\Users\s.janssens.CI\PycharmProjects\filter_flow_data\20220615_142431f_Flowmeter_test_source_trans.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
#print (df)
#df.drop([0,1])
means=df.groupby('no.').mean().reset_index()
stds=df.groupby('no.').std().reset_index()

filtered_series = df['q C1'].squeeze()
filtered_series = df['read_flow M_1'].squeeze()
outlier_indices = hampel(ts = filtered_series, window_size = 12, n=1)
filtered_d = filtered_series.drop(outlier_indices)
filtered_d.values.tolist()
df['filtered M1']=filtered_d

#print(f'filtered_d: {filtered_d.values.tolist()}')


filtered_series.to_excel("filtered_flow_data.xlsx")

# Plot Original Series
# filtered_series.plot(color='red')
# plt.title('Original Series')
# plt.show()

# Plot Cleaned Series
# filtered_d.plot(style='k-')
# plt.title('Cleaned Series (Without detected Outliers)')
# plt.show()

plt.plot()


#plot the outliers
#plt.scatter(outlier_indices, filtered_series[outlier_indices], color="blue",marker='+')
plt.scatter(outlier_indices, filtered_series[outlier_indices], color="blue",marker='+')
plt.grid( linestyle='-.', linewidth=0.5)


#find unique values in the 'no.' column
# uniques=df['no.'].unique()
#
# for val in uniques:
#     #filter the source data by uniqe values
#     to_average=df.loc[df['no.'] == uniques[val]]
#     to_average.mean()
#     to_average.std()

means_filtered=df.groupby('no.').mean().reset_index()
stds_filtered=df.groupby('no.').std().reset_index()

means_filtered.to_excel("filtered_means.xlsx")
stds_filtered.to_excel("filtered_stds.xlsx")

plt.scatter(means_filtered['runtime'],means_filtered['filtered M1'], color="green",marker='*')