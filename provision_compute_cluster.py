# -----------------------------------------------------
#  Create a compute cluster using AzureML SDK
# -----------------------------------------------------

# Import the Workspace class
from azureml.core import Workspace


# Access the workspace from the config.json 
ws = Workspace.from_config(path="./config")


# Specify the cluster name
cluster_name = "my-cluster-001"


# Provisioning configuration using AmlCompute
from azureml.core.compute import AmlCompute

# Configuration of the compute cluster
compute_config = AmlCompute.provisioning_configuration(
                                 vm_size="STANDARD_D11_V2",
                                 max_nodes=2)


# Create the cluster
cluster = AmlCompute.create(ws, cluster_name, compute_config)




