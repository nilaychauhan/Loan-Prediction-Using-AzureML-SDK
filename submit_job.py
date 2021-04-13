# ------------------------------------------------------------
# Run a script in an Azureml environment
# ------------------------------------------------------------
# This code will submit the script provided in ScriptRunConfig
# and create an Azureml environment on the local machine
# including the docker for Azureml
# ------------------------------------------------------------

# Import the Azure ML classes
from azureml.core import Workspace, Experiment, ScriptRunConfig

# Access the workspace using config.json
ws = Workspace.from_config("./config")


# Create/access the experiment from workspace 
new_experiment = Experiment(workspace=ws,
                            name="Loan_Script")


# Create a script configuration
script_config = ScriptRunConfig(source_directory=".",
                                script="script_to_run.py")


# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)


# Create a wait for completion of the script
new_run.wait_for_completion()