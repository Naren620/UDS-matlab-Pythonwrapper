# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:10:33 2024

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Example showing how to simulate a Simulink model (called the_model) with different
parameter and external input signal values using the MATLAB Engine API for Python.

The example requires:
    1. MATLAB and Simulink products installed and licensed
    2. MATLAB Engine API installed as a Python package
       https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

@author: Murali Yeddanapudi
Created on Tue Mar  1 2022
"""
# Install numpy (For example, pip install numpy)
import numpy as np
import matlab.engine

mle = matlab.engine.start_matlab(); # start the matlab engine


## 1st sim: with default parameter values

so = mle.sim_the_model(nargout=1)

if isinstance(so, matlab.engine.matlabnumeric.MLArray):
    # If `so` is a numeric array, convert to numpy array
    so_np = np.array(so)
    print("Simulation Output (as numpy array):", so_np)
else:
    # For a structure or dictionary, convert fields one by one if possible
    try:
        # Assuming `so` has a specific field, e.g., 'yout' or similar
        result = so['yout']  # Replace 'yout' with actual field name
        print("Simulation Output Field 'yout':", np.array(result))
    except AttributeError:
        print("Output:", so)
input("Press enter to close the MATLAB figure and exit ...")
mle.quit() # stop the matlab engine
