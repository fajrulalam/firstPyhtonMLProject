# -*- coding: utf-8 -*-
"""FP Analitika Bisnis Kelompok 8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J2xjdGeuj6U3qITFYmK5dH4GIhSaZYii

**Anggota Kelompok 8** 

Jessica Patricia Halim (05211940000004)

Muhammad Fajrul Alam Ulin Nuha (05211940000011)

Salsa Putri Islammia (05211940000064)

# **Tentang Dataset**

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ipsum purus, euismod et risus non, egestas scelerisque odio. Curabitur nec dui in lorem tempus rhoncus. Vivamus et nibh sit amet risus hendrerit semper in in turpis. Phasellus ut dolor et arcu tristique pellentesque vitae in orci. Fusce tincidunt nunc tellus, id maximus massa dignissim vel. In vulputate, justo in maximus cursus, neque massa tristique lectus, sed placerat felis odio eu ante.

## **Deskripsi Variabel**
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ipsum purus, euismod et risus non, egestas scelerisque odio. Curabitur nec dui in lorem tempus rhoncus. Vivamus et nibh sit amet risus hendrerit semper in in turpis. Phasellus ut dolor et arcu tristique pellentesque vitae in orci.

# Exploratory Data Analysis (EDA)
"""

#Import EDA Library
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib as mpl

# Insert dataset
from google.colab import files
uploaded_file = files.upload()
df = pd.read_csv('StudentsPerformance.csv')

#Cari informasi dataset (info, shape, describe)
df.info()

"""Dari informasi di atas terlihat bahwa dataset terdiri dari 8 kolom dan setiap kolom terdiri dari 1000 baris yang tidak null."""

df.shape

#dataset terdiri dari 8 kolom dan 1000 baris

df.describe()

"""## Eksplorasi masing-masing Categorical data menggunakan bar chart"""

#gender
sns.set_style('darkgrid')
sns.countplot(x='gender',data=df,palette=sns.color_palette(palette='Set1'),order=df['gender'].value_counts().index)
plt.show()
lis = df['gender'].unique()
for j in lis:
        print(j+':',len(df[df['gender']==j]))

#race/ethnicitity
sns.set_style('darkgrid')
sns.countplot(x='race/ethnicity',data=df,palette=sns.color_palette(palette='Set1'),order=df['race/ethnicity'].value_counts().loc[['group A', 'group B', 'group C', 'group D', 'group E']].index)
plt.show()
lis = df['race/ethnicity'].unique()
for j in lis:
        print(j+':',len(df[df['race/ethnicity']==j]))

#parental level of education
sns.set_style('darkgrid')
sns.countplot(y='parental level of education',data=df,palette=sns.color_palette(palette='Set1'),order=df['parental level of education'].value_counts().index)
plt.show()
lis = df['parental level of education'].unique()
for j in lis:
        print(j+':',len(df[df['parental level of education']==j]))

#lunch
sns.set_style('darkgrid')
sns.countplot(x='lunch',data=df,palette=sns.color_palette(palette='Set1'),order=df['lunch'].value_counts().index)
plt.show()
lis = df['lunch'].unique()
for j in lis:
        print(j+':',len(df[df['lunch']==j]))

#test preparation course
sns.set_style('darkgrid')
sns.countplot(x='test preparation course',data=df,palette=sns.color_palette(palette='Set1'),order=df['test preparation course'].value_counts().index)
plt.show()
lis = df['test preparation course'].unique()
for j in lis:
        print(j+':',len(df[df['test preparation course']==j]))

"""**Lessons Learned** (Apa yang didapatkan dari EDA)

📃Jumlah siswa laki-laki dan perempuan hampir sama. Perempuan: 518. Laki-laki: 482

📃Mayoritas ras siswa berasal dari grup C

📃Orang tua siswa terbanyak merupakan lulusan D3 dan suatu universitas

📃Lebih dari 3/5 siswa tergolong mampu dan tidak memerlukan dana pemerintah untuk makan siang di sekolah

📃Sebagian besar siswa tidak mengambil kursus persiapan tes

## Eksplorasi Korelasi Antar Variabel
"""

#correlation matrix/correlation graph 
sns.heatmap(df.corr(),annot=True,cmap=sns.color_palette("magma", as_cmap=True))
plt.show()

#Korelasi Race/Ethnicity dengan Test Preparation Course
df1 = df[df['test preparation course']=='completed']
lis = df['race/ethnicity'].unique()
average_len=[]
for i in lis:
    y=(len(df1[df1['race/ethnicity']==i ])/len(df[df['race/ethnicity']==i]))*100
    average_len.append(y)
plt.xlabel('persentase siswa yang mengambil kursus')
plt.ylabel('race/ethnicity')
sns.barplot(y=lis,x=average_len,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Race/Ethnicity dengan Lunch
df1 = df[df['lunch']=='standard']
lis = df['race/ethnicity'].unique()
average_len=[]
for i in lis:
    y=(len(df1[df1['race/ethnicity']==i ])/len(df[df['race/ethnicity']==i]))*100
    average_len.append(y)
plt.xlabel('persentase siswa yang makanannya standard')
plt.ylabel('race/ethnicity')
sns.barplot(y=lis,x=average_len,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Pengambilan Kursus Persiapan Test dengan Lunch
df1 = df[df['test preparation course']=='completed']
lis = df['lunch'].unique()
average_len=[]
for i in lis:
    y=(len(df1[df1['lunch']==i ])/len(df[df['lunch']==i]))*100
    average_len.append(y)
plt.xlabel('presentase siswa mengambil kursus')
plt.ylabel('Lunch')
sns.barplot(y=lis,x=average_len,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Pengambilan Kursus Persiapan Test dengan Gender
df1 = df[df['test preparation course']=='completed']
lis = df['gender'].unique()
average_len=[]
for i in lis:
    y=(len(df1[df1['gender']==i ])/len(df[df['gender']==i]))*100
    average_len.append(y)
plt.xlabel('persentase siswa yang mengambil kursus')
plt.ylabel('gender')
sns.barplot(y=lis,x=average_len,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Test Prep Course dengan Parental Level of Education
df1 = df[df['test preparation course']=='completed']
lis = df['parental level of education'].unique()
average_len=[]
for i in lis:
    y=(len(df1[df1['parental level of education']==i ])/len(df[df['parental level of education']==i]))*100
    average_len.append(y)
plt.xlabel('persentase siswa yang mengambil kursus')
plt.ylabel('pendidikan terakhir orang tua')
sns.barplot(y=lis,x=average_len,palette=sns.color_palette(palette='Set1'))
plt.show()

"""**Lessons Learned** (Apa yang didapatkan dari EDA)

📃Siswa yang memiliki reading score bagus, cenderung memiliki writing score yang bagus

📃Siswa dengan grup ras E paling banyak mengambil kursus dan makanan standard

📃Siswa yang mengambil makanan free banyak mengambil kursus

📃Tidak ada korelasi antara gender siswa dengan pengambilan kursus

📃Orang tua dengan pendidikan terendah, justru lebih mendorong anaknya untuk mengambil kursus

## Eksplorasi Korelasi Varibel dengan Target Variabel (Feature Extraction)

Menghitung avarage score
"""

#Average Score
average_score = np.sum(df[['math score','reading score','writing score']],axis=1)
average_score=average_score/3
df['average score'] = average_score
df

#Korelasi Average Score dengan Gender
sns.set_style('darkgrid')
sns.barplot(y='gender',x='average score',data=df,order=df['gender'].value_counts().index,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Average Score dengan Race/Ethnicity
sns.set_style('darkgrid')
sns.barplot(y='race/ethnicity',x='average score',data=df,order=df['race/ethnicity'].value_counts().index,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Average Score dengan Parental Level of Education
sns.set_style('darkgrid')
sns.barplot(y='parental level of education',x='average score',data=df,order=df['parental level of education'].value_counts().index,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Average Score dengan Lunch
sns.set_style('darkgrid')
sns.barplot(y='lunch',x='average score',data=df,order=df['lunch'].value_counts().index,palette=sns.color_palette(palette='Set1'))
plt.show()

#Korelasi Average Score dengan Test Preparation Course
sns.set_style('darkgrid')
sns.barplot(y='test preparation course',x='average score',data=df,order=df['test preparation course'].value_counts().index,palette=sns.color_palette(palette='Set1'))
plt.show()

"""**Lessons Learned** (Apa yang didapatkan dari EDA)

📃Siswa perempuan memiliki rata-rata score yang lebih tinggi

📃Siswa dengan grup ras E memiliki rata-rata score lebih tinggi dibanding grup ras lain. Hal ini karena siswa grup E paling banyak mengikuti kursus

📃Siswa yang memiliki orang tua dengan pendidikan terakhir S2 memiliki rata-rata score yang paling tinggi, walaupun relatif sedikit dari mereka mengikuti kursus

📃Siswa yang mampu memiliki rata-rata score yang lebih tinggi dari siswa yang kurang mampu. Padahal siswa kurang mampu lebih banyak mengambil kursus

📃Siswa yang mengambil kursus memiliki rata-rata score yang lebih tinggi

# Data Preprocessing
"""

#Import Libraries
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Check for Outlier
sns.boxplot(df['average score'])

#Feature Selection
df = df.drop(['math score', 'writing score', 'reading score'], axis = 1)

df

#Encoding Categorical Data
encoder = LabelEncoder()
df['gender'] = encoder.fit_transform(df['gender'])
df['race/ethnicity'] = encoder.fit_transform(df['race/ethnicity'])
df['lunch'] = encoder.fit_transform(df['lunch'])
df['parental level of education'] = encoder.fit_transform(df['parental level of education'])
df['test preparation course'] = encoder.fit_transform(df['test preparation course'])
df.head()

#Splitting Dataset
y = df['average score']
features = df.drop(['average score'], axis  = 1)
x = features
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

"""# Model Building

**Penjelasan Model yang akan digunakan**

Format: 
1. Tipe Modelnya (Supervised, Regression). Jelasin kenapa kok ini cocok
2. Algoritma 1: What, how it works, why algoritma ini dipilih
3. Algoritma 1: What, how it works, why algoritma ini dipilih
"""

#Import Model Building Libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

"""## Linear Regression"""

#Build Linear Regression
linreg = LinearRegression().fit(x_train, y_train)

"""## Random Forest"""

#Build Random Forest
ranfor = RandomForestRegressor(random_state=0).fit(x_train, y_train)

"""# Model Evaluation

**Metode Evaluasi**
1. MSE
2. MAE
3. RMSE
4. R_Squared

**Function for Model Evaluation**
"""

#import libraries
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

"""Functions"""

def PlotPrediction(true,predicted, title = "Dataset: "):
    fig = plt.figure(figsize=(20,20))
    ax1 = fig.add_subplot(111)
    ax1.set_title(title + 'True vs Predicted')
    ax1.scatter(list(range(0,len(true))),true, s=10, c='r', marker="o", label='True')
    ax1.scatter(list(range(0,len(predicted))), predicted, s=10, c='b', marker="o", label='Predicted')
    plt.legend(loc='upper right');
    plt.show()

def evaluateRegressor(true,predicted,message):
    MSE = mean_squared_error(true,predicted,squared = True)
    MAE = mean_absolute_error(true,predicted)
    RMSE = mean_squared_error(true,predicted,squared = False)
    R_squared = r2_score(true,predicted)
    print(message)
    print("MSE:", MSE)
    print("MAE:", MAE)
    print("RMSE:", RMSE)
    print("R-squared:", R_squared)

"""**Linear Regression Evaluation**"""

#Evaluasi Linreg
linreg_predicted = linreg.predict(x_test)
plt.scatter(y_test, linreg_predicted)

sns.distplot((y_test-linreg_predicted), bins=10);

MSE_linreg = mean_squared_error(y_test,linreg_predicted,squared = True)
    MAE_linreg = mean_absolute_error(y_test,linreg_predicted)
    RMSE_linreg = mean_squared_error(y_test,linreg_predicted,squared = False)
    R_squared_linreg = r2_score(y_test,linreg_predicted)
    print('Test Set')
    print("MSE:", MSE_linreg)
    print("MAE:", MAE_linreg)
    print("RMSE:", RMSE_linreg)
    print("R-squared:", R_squared_linreg)

#Visualisi True vs Predicted
PlotPrediction(y_test, linreg_predicted)

"""**Random Forest Regression Evaluation**"""

#Evaluasi Linreg
ranfor_predicted = ranfor.predict(x_test)
plt.scatter(y_test, ranfor_predicted)

sns.distplot((y_test-ranfor_predicted), bins=10);

MSE_ranfor = mean_squared_error(y_test,ranfor_predicted,squared = True)
    MAE_ranfor = mean_absolute_error(y_test,ranfor_predicted)
    RMSE_ranfor = mean_squared_error(y_test,ranfor_predicted,squared = False)
    R_squared_ranfor = r2_score(y_test,ranfor_predicted)
    print('Test Set')
    print("MSE:", MSE_ranfor)
    print("MAE:", MAE_ranfor)
    print("RMSE:", RMSE_ranfor)
    print("R-squared:", R_squared_ranfor)

#Visualisi True vs Predicted
PlotPrediction(y_test, ranfor_predicted)

"""**What we learned**
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ipsum purus, euismod et risus non, egestas scelerisque odio. Curabitur nec 

📃lorem

📃lorem

📃lorem

📃lorem

# Model Tuning

**Encoding dengan One Hot Encoder**
"""

#Preprocessing data
df = pd.read_csv('StudentsPerformance.csv')
average_score = np.sum(df[['math score','reading score','writing score']],axis=1)
average_score=average_score/3
df['average score'] = average_score
df = df.drop(['math score', 'writing score', 'reading score'], axis = 1)

#Remove outlier
def remove_outliers(df,column_name,lower,upper):
    removed_outliers = df[column_name].between(df[column_name].quantile(lower), df[column_name].quantile(upper))
    
    print(str(df[column_name][removed_outliers].size) + "/" + str(SP_csv[column_name].size) + " data points remain.") 

    index_names = df[~removed_outliers].index # INVERT removed_outliers!!
    return df.drop(index_names)

#Separate Features (x) and from target (y)
y = df['average score']
features = df.drop(['average score'], axis  = 1)
x = features

#Encode categorical features(x)
x = pd.get_dummies(x)
x

sns.heatmap(df.corr(),annot=True,cmap=sns.color_palette("magma", as_cmap=True))
plt.show()

"""**Data Splitting**"""

#Train test split
x_train,y_train,x_test,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

"""**Data Predicting**"""

#Predict Data with both algoritms
linreg = LinearRegression()
linreg.fit(x_train, x_test)

ranfor = RandomForestRegressor()
ranfor.fit(x_train, x_test)

"""**Evaluate Model with Linear Regression**"""

#Evaluate LinReg
linreg_predicted = linreg.predict(y_train)
plt.scatter(y_test, linreg_predicted)

sns.distplot((y_test-linreg_predicted), bins=10);

MSE_linreg2 = mean_squared_error(y_test,linreg_predicted,squared = True)
    MAE_linreg2 = mean_absolute_error(y_test,linreg_predicted)
    RMSE_linreg2 = mean_squared_error(y_test,linreg_predicted,squared = False)
    R_squared_linreg2 = r2_score(y_test,linreg_predicted)
    print('Test Set')
    print("MSE:", MSE_linreg2)
    print("MAE:", MAE_linreg2)
    print("RMSE:", RMSE_linreg2)
    print("R-squared:", R_squared_linreg2)

"""**Evaluate Model with Random Forest**"""

#
ranfor_predicted = ranfor.predict(y_train)
plt.scatter(y_test, ranfor_predicted)

sns.distplot((y_test-ranfor_predicted), bins=10);

#Visualisasi True vs Predicted
PlotPrediction(y_test, linreg_predicted)

#Evaluate RanFor
MSE_ranfor2 = mean_squared_error(y_test,ranfor_predicted,squared = True)
MAE_ranfor2 = mean_absolute_error(y_test,ranfor_predicted)
RMSE_ranfor2 = mean_squared_error(y_test,ranfor_predicted,squared = False)
R_squared_ranfor2 = r2_score(y_test,ranfor_predicted)
print('Test Set')
print("MSE:", MSE_ranfor2)
print("MAE:", MAE_ranfor2)
print("RMSE:", RMSE_ranfor2)
print("R-squared:", R_squared_ranfor2)

#Visualisasi True vs Predicted
PlotPrediction(y_test, ranfor_predicted)

"""# Kesimpulan"""

model_ev2 = pd.DataFrame({'Model': ['Linear Regression', 'Linear Regression 2', 'Random Forest', 'Random Forest 2'], 'MAE': [MAE_linreg,
                    MAE_linreg2,MAE_ranfor,MAE_ranfor2], 'MSE': [MSE_linreg,
                    MSE_linreg2,MSE_ranfor,MSE_ranfor2], 'RMSE': [RMSE_linreg,
                    RMSE_linreg2,RMSE_ranfor,RMSE_ranfor2], 'R Squared': [R_squared_linreg,
                    R_squared_linreg2,R_squared_ranfor,R_squared_ranfor2]})
model_ev2