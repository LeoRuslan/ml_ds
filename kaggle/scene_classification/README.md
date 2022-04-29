Create virtual environment with conda:

    conda create -n scene_env python=3.10


To activate this environment, use:

    conda activate scene_env

To deactivate an active environment, use:

    conda deactivate

Install required packages in the activated environment:
	
	pip install -r requirements.txt

Jupyter configuration for working with specific environment (execute from inside the activated environmentin):

	ipython kernel install --user --name=scene_env --display-name "Python (scene_env)"
