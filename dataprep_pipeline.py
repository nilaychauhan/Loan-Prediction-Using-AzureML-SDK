# --------------------------------------------------------------
# Data preparation step of the pipeline run
# --------------------------------------------------------------

from azureml.core import Run


# Get the run context
new_run = Run.get_context()


# Get the workspace from the run
ws = new_run.experiment.workspace


# --------------------------------------------------------
# Do your stuff here
# --------------------------------------------------------

import pandas as pd

# Read the input dataset
df = new_run.input_datasets['raw_data'].to_pandas_dataframe()

# Select relevant columns from the dataset
dataPrep = df.drop(["ID"], axis=1)

all_cols = dataPrep.columns


# Check the missing values
dataNull = dataPrep.isnull().sum()


# Replace the missing values of string variable with mode
mode = dataPrep.mode().iloc[0]
cols = dataPrep.select_dtypes(include='object').columns

dataPrep[cols] = dataPrep[cols].fillna(mode)


# Replace numerical columns with mean
mean = dataPrep.mean()
dataPrep = dataPrep.fillna(mean)


# Create Dummy variables - Not required in designer/Classic Studio
dataPrep = pd.get_dummies(dataPrep, drop_first=True)


# Normalise the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
columns = df.select_dtypes(include='number').columns
dataPrep[columns] = scaler.fit_transform(dataPrep[columns])


# Get the arguments from pipeline job
from argparse import ArgumentParser as AP

parser = AP()
parser.add_argument('--datafolder', type=str)
args = parser.parse_args()


# Create the folder if it does not exist
import os
os.makedirs(args.datafolder, exist_ok=True)

# Create the path
path = os.path.join(args.datafolder, 'defaults_prep.csv')

# Write the data preparation output as csv file
dataPrep.to_csv(path, index=False)


# Log null values
for column in all_cols:
    new_run.log(column, dataNull[column])


# Complete the run
new_run.complete()
























