import pandas as pd

#creating a data frame
df=pd.read_csv("C:\\Users\\saish\\OneDrive\\Desktop\\Python_Programming\\0047_Back_Bone_Rd_0.csv")
print("The dataframe is:", df)


#imputer
from sklearn.impute import SimpleImputer
import numpy as np 
data=np.df 
imputer=SimpleImputer(strategy='mean')
imputed_data=imputer.fit_transform(data)

print(data)
print(imputed_data)


#check for the number of duplicate rows 
print(f"\n Number of duplicate rows:{df.duplicated().sum()}")


#Remove duplicate rows, kepping the first occurence
df.drop_duplicates(inplace=True)
print("Duplicates removed:")


#Review the Final cleaned data info
print("\n Cleaned Data info:") 
print(df.info)

#save the cleaned dataframe to a new csv file 
df.to_csv("your_file_cleaned.csv", index=False)
print("\n Cleaned data saved to 'your_file_cleaned.csv'")
