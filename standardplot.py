import matplotlib.pyply as plt
import numpy as np

x = np.linespace(0,20,100)  # Create a list of evenly-spaced numbers over the range
plt.plt(x,np.sin(x))        # Plot the sine of each x point
plt.show()                  # Display the plot