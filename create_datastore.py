# Import the workspace and Datastore class
from azureml.core import Workspace, Datastore

# Access the workspace from the config.json
ws = Workspace.from_config(path="./config")

# Create a datastore
az_store = Datastore.register_azure_blob_container(
    workspace=ws,
    datastore_name="azure_sdk_blob01",
    account_name="azuremlopsst",
    container_name="azuremlblob",
    account_key="Lxyp9KRBXFNKOdHcfNoOVR9FJDJLVw1vPhPGYbJb+23xjuHKdBYYFVTItPqW+P66DB5dMYmyrmGZSJM17KYfZw=="
)