# Import Workspace class 
from azureml.core import Workspace

#  Create the workspace
ws = Workspace.create(name='Azureml-SDK-WS-003',
                      subscription_id='3b025e46-21bc-4e85-9e84-652af4918dca',
                      resource_group='AzuremlSDKRG003',
                      create_resource_group=True,   # True if it does not exist
                      location='westus')

# Write the config.json file to local directory
ws.write_config(path="./config")