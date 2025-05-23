# -*- coding: utf-8 -*-
"""Submission_predictive_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yrjqtO5fTU3ILpWNVpesDHWvZGmmaOAP

# Import Library
"""

import kagglehub

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score,f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

"""# Data Loading"""

# Download latest version
path = kagglehub.dataset_download("jayaantanaath/student-habits-vs-academic-performance")

print("Path to dataset files:", path)

df = pd.read_csv(path+'/student_habits_performance.csv')
#df = pd.read_csv(path+'/StudentPerformanceFactors.csv')

df.head()

"""# EDA"""

df.info()

df.describe()

df.isnull().sum()

print(f'Jumlah data duplikat: {df.duplicated().sum()}')

"""terdapat missing value pada kolom parental_education_level
sedangkan duplicated value tidak ada
"""





df.describe()

df.isnull().sum()

numerical_columns = df.select_dtypes(include=np.number).columns

colors = sns.color_palette("Set1", n_colors=len(numerical_columns))

fig1, axes1 = plt.subplots(4, 2, figsize=(15, 20))

for i in range(4):
    var = numerical_columns[i]

    sns.boxplot(x=var, data=df, ax=axes1[i, 0], color=colors[i])
    axes1[i, 0].set_title(f' {var.replace("_", " ")}')

    hist_color_idx = len(colors) - 1 - i
    sns.histplot(df[var], ax=axes1[i, 1], color=colors[hist_color_idx], kde=True, edgecolor='black')
    axes1[i, 1].set_title(f'Distribution of {var.replace("_", " ")}')

plt.tight_layout()
plt.show()

fig2, axes2 = plt.subplots(5, 2, figsize=(15, 15))

for i in range(4, 9):
    var = numerical_columns[i]
    j = i - 4
    sns.boxplot(x=var, data=df, ax=axes2[j, 0], color=colors[i])
    axes2[j, 0].set_title(f' {var.replace("_", " ")}')

    hist_color_idx = len(colors) - 1 - i
    sns.histplot(df[var], ax=axes2[j, 1], color=colors[hist_color_idx], kde=True, edgecolor='black')
    axes2[j, 1].set_title(f'Distribution of {var.replace("_", " ")}')

plt.tight_layout()
plt.show()

"""**Insight yang didapat :**
Dari semua fitur numerik walaupun pada boxplot terlihat banyak nilai yang seperti outlier akan tetapi nil;ai tersebut masih berada di rentang yang seharusnya
"""

# Mengambil kolom kategorikal
categorical_columns = df[['gender','part_time_job','diet_quality','parental_education_level','internet_quality','extracurricular_participation']].columns

df[categorical_columns].nunique()

#Cek unique value yang ada di kolom kategorikal
for col in categorical_columns:
    print(f'Unique values for {col}: {df[col].unique()}')

#Grafik banyaknya unique value tiap kolom kategorikal
# Setup figure
plt.figure(figsize=(20, 30))
plt.suptitle('Distribution of Categorical Variables', y=1.02, fontsize=18, fontweight='bold')

# Create subplots grid
for i, column in enumerate(categorical_columns, 1):
    plt.subplot(5, 3, i)


    ax = sns.countplot(
    x=df[column],
    hue=df[column],
    palette='Blues',
    order=df[column].value_counts().index,
    legend=False
    )


    total = len(df[column])
    for p in ax.patches:
        x = p.get_x() + p.get_width() / 2
        y = p.get_height() + 5
        ax.annotate(
            f'{p.get_height()}',
            (x, y),
            ha='center',
            va='bottom',
            fontsize=10
        )

    # Formatting
    plt.title(f'{column.replace("_", " ").title()}', pad=15)
    plt.xlabel('')
    plt.ylabel('Count', labelpad=10)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

for col in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, y='exam_score', data=df)
    plt.title(f'Exam Score by {col}')
    plt.xticks(rotation=45)
    plt.show()

"""Insight yang didapat variabel exam score tidak terpengaruh oleh semua kolom kategorikal

# Data Preperation
"""

# Handling missing value pada kolom parental_education_level diisi dengan nilai modusnya(nilai yang paling sering muncul)
df['parental_education_level']= df['parental_education_level'].fillna(df['parental_education_level'].mode()[0])

#Drop Kolom student_id k
df.drop('student_id', axis=1, inplace=True)

# Membuat kolom screen time yaitu jumlah dari waktu yang digunakan untuk social media dan netflix
df['screen_time'] = df['social_media_hours'] + df['netflix_hours']
df.drop(['social_media_hours', 'netflix_hours'], axis=1, inplace=True)



#Map exam score menjadi kolom exam result untuk label kalasifikasi
def map_exam_score(score):
  if score >= 70: # Siswa demgam nilai diatas rata rata dinyatakan lulus
    return "Pass"
  else:
    return "Faill"

df['Exam_Result'] = df['exam_score'].apply(map_exam_score)

df.head()

exam_result_counts = df['Exam_Result'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(exam_result_counts, labels=exam_result_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Exam Results')
plt.axis('equal')
plt.show()

df = df.drop('exam_score', axis=1)

"""## Encoding Feature Kategorikal"""

# Create a LabelEncoder object
le = LabelEncoder()

# Iterate through each categorical column and apply label encoding
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

df.head()

#encoding kolom exam result
df['Exam_Result']=le.fit_transform(df['Exam_Result'])

df.corr()

#plot korelasi dalam heatmap agar lebih mudah dilihat
f,ax = plt.subplots(figsize=(16, 15))

sns.heatmap(df.corr(), annot=True, linewidths=0.5,linecolor="red", fmt= '.3f',cmap='coolwarm',ax=ax)
plt.show()

"""kolom study_hours_per_day","mental_health_rating","screen_time memiliki nilai korelasi paling tinggi baik kearah positif atau negatif

## Feature Selection
"""

#memilih fitur dengan nilai korelasi tertinggi
df_select = df[["study_hours_per_day","mental_health_rating","screen_time"]]

"""## Split Dataset"""

#Split dataset
X = df_select
y = df['Exam_Result']

#membagi dataset menjadi train dan test

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)



"""## Standarisasi"""

#standarisai data menggunakan standarscaller
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

"""# Modelling"""

# 1. Logistic Regression
Logres = LogisticRegression(
    penalty='l2',
    C=0.5,
    solver='liblinear',
    max_iter=2000,
    random_state=42
).fit(X_train, y_train)

# 2. Decision Tree
dt = DecisionTreeClassifier(
    max_depth=7,
    min_samples_split=15,
    random_state=42
).fit(X_train, y_train)

# 3. Random Forest
rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    min_samples_leaf=5,
    random_state=42
).fit(X_train, y_train)

# 4. XGBoost
xgb = XGBClassifier(
    learning_rate=0.05,
    max_depth=4,
    n_estimators=300,
    random_state=42
).fit(X_train, y_train)

"""# Evaluation"""

#Fungsi evaluate_model untuk mereturn matriks evaluasi seluruh model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    results = {
        'Confusion Matrix': cm,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='macro'),
        'Recall': recall_score(y_test, y_pred, average='macro'),
        'F1-Score': f1_score(y_test, y_pred, average='macro'),
        "Cross Validation": cross_val_score(model, X_test, y_test, cv=5).mean()

    }
    return results

result = {
    'Logistic Regression': evaluate_model(Logres, X_test, y_test),
    'Decision Tree': evaluate_model(dt, X_test, y_test),
    'Random Forest': evaluate_model(rf, X_test, y_test),
    'XGBoost': evaluate_model(xgb, X_test, y_test)
}

summary = pd.DataFrame(columns=[ 'Accuracy', 'Precision', 'Recall', 'F1-Score', "Cross Validation"])

# Isi DataFrame dengan hasil
rows = []
for model_name, metrics in result.items():
    rows.append({
        'Model': model_name,
        'Accuracy': metrics['Accuracy'],
        'Precision': metrics['Precision'],
        'Recall': metrics['Recall'],
        'F1-Score': metrics['F1-Score'],
        "Cross Validation": metrics["Cross Validation"]

    })

# Konversi daftar kamus ke DataFrame
summary = pd.DataFrame(rows)

# Tampilkan DataFrame
summary.head()

#confusion Matrix
for model_name, metrics in result.items():
  cm = metrics['Confusion Matrix']
  plt.figure(figsize=(8, 6))
  sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
              xticklabels=np.unique(y), yticklabels=np.unique(y))
  plt.title(f"Confusion Matrix - {model_name}")
  plt.xlabel("Predicted Label")
  plt.ylabel("True Label")
  plt.show()

#plot perbandingan akurasi dan crossvall seluruh model
plt.figure(figsize=(10, 6))
models = summary['Model']
accuracy = summary['Accuracy']
cross_val = summary['Cross Validation']

X_axis = np.arange(len(models))

bars1= plt.bar(X_axis - 0.2, accuracy, 0.4, label='Accuracy')
bars2 =plt.bar(X_axis + 0.2, cross_val, 0.4, label='Cross Validation')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.,
                 height + 0.01,
                 f'{height:.2f}',
                 ha='center',
                 va='bottom',
                 fontsize=10)
plt.xticks(X_axis, models)
plt.xlabel("Model")
plt.ylabel("Score")
plt.title("Comparison of Accuracy and Cross Validation Scores")
plt.legend()
plt.show()