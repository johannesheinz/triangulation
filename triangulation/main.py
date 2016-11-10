#!/usr/bin/env python3

import triangulation.input as data
import triangulation.calculate as calc
import triangulation.plot as plot

def start():
    """
    Summary line.
    
    Parameters
    ----------
    arg1 : int
        Description of arg1

    Returns
    -------
    int
        Description of return value
    """
    
    coordinates = data.read_coordinates()
    
    for key, value in coordinates.items():
        
        if(calc.check_intersection() and calc.check_orientation()):
            print(key, value)
            print("Δ")
            # import numpy as np
            # import pyplot as plt
            # linalg.det(a)   

            # Make a quick sin plot
            #x = np.linspace(, 10, 100)
            #y = np.sin(x)
            #plt.plot(x, y)
            #plt.xlabel("Time")
            #plt.ylabel("Amplitude")

            # Save it in png and svg formats
            plot.save("signal", ext="png", close=False, verbose=True)
            plot.save("signal", ext="svg", close=True, verbose=True)
        
if __name__ == '__main__':
    start()
