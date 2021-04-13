# Import required classes from Azureml
from azureml.core import Workspace, Datastore, Dataset, Experiment
from azureml.core import Run

# Access the Workspace, Datastore and Datasets
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, 'azure_sdk_blob01')
az_dataset        = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store  = ws.get_default_datastore()

# Get the context of the experiment run
new_run = Run.get_context()

# Do your stuff here
df = az_dataset.to_pandas_dataframe()

# Count the observations
total_observations = len(df)

# Get the null/missing values
nulldf = df.isnull().sum()


# Create a new dataframe with new features 
# and write to outputs folder
new_df = df[["Gender", "Married", "Education", "Loan_Status"]]
new_df.to_csv("./outputs/loan_trunc.csv", index=False)

# Log metrics and Complete an experiment run
# Log the metrics to the workspace
new_run.log("Total Observations", total_observations,snapshot_directory=None)

# Log the missing data values
for columns in df.columns:
    new_run.log(columns, nulldf[columns])

new_run.complete()