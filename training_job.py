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
                            name="Training_Script_01")


# -------------------------------------------------
# Create custom environment
from azureml.core import Environment
from azureml.core.environment import CondaDependencies

# Create the environment
myenv = Environment(name="MyEnvironment")

# Create the dependencies object
myenv_dep = CondaDependencies.create(conda_packages=['pip','scikit-learn'])
myenv.python.conda_dependencies = myenv_dep

# Register the environment
myenv.register(ws)
# Create a script configuration for custom environment of myenv
script_config = ScriptRunConfig(source_directory=".",
                                script="training_script.py",
                                environment=myenv)


# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)


# Create a wait for completion of the script
new_run.wait_for_completion()















