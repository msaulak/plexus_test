# Plexus coding challenge
## Author - Manveer Singh


#### Language, build environments and dependencies

This solution has been coded in Python3.7 using PyCharm IDE on Ubuntu. It was tested on Windows as well.
Please note that when running on Windows, the method GlassTriangle.export_as_graph_image will not generate
an image. However, it will not raise an error.

To export the glass triangle as an image, please ensure that pydot is installed in your python interpreter. 
I used a conda environment to set this up. Instructions are below. You can skip this if you are okay with
viewing the output on the console. Please ensure the console window is maximized to a better output view.

Alternatively, you can print the graph data, copy it and paste it on https://dreampuf.github.io/GraphvizOnline
to generate the image online.

I have added some output images from my testing in the images folder.

See below for more information on setting up the conda environment.
    
    1. Please install miniconda if not installed.
        Windows : https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html
        Linux : https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
    2. Once installed, open a 
        a. Shell if using Linux
        b. Anaconda prompt if using Windows
    3. Run the following and follow the prompts.
        a. conda create -n plexus_test
        b. conda activate plexus_test
        c. conda install -c conda-forge pydot

#Running the sample code

1. Activate conda environment
        
        conda activate plexus_test
        
2. Go to the repo directory and run

        python main.py
        
## Run tests

There are 7 test cases in total.
1. Activate conda environment
        
        conda activate plexus_test

2. Go to the repo directory and run

        python -m unittest
        
## Alternative solution

I started an alternative solution for this challenge using Binary Trees. The partial solution is under the module
libs/partial_tree_solution/glass. Running the file with python will produce an output on the console.
I abandoned this solution as it required additional time and work which would have been outside the scope of
this exercise.  