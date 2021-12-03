"""
Produces an animated GIF, entirely through YASARA,
by rotating and obtaining screenshots of a sample molecule.

This code is meant to be executed from
the YaPyCon Python Console.
"""

from yasara_kernel import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# Load a sample molecule here
LoadPDB("1crn", download="latest")
# Obtain the first frame from YASARA
frame = SavePNG("frame.png", menu="No")

# Prepare the plot to visualise the frame
fig, ax = plt.subplots()
fig.set_tight_layout(True)

def on_update(i):
    RotateObj(1, y=11.25)
    frame = SavePNG("frame.png", menu="no")
    ax.imshow(frame)
    return [ax, ]

anim = FuncAnimation(fig, on_update, frames=range(0,32), interval=200)
anim.save(os.path.expanduser('~/1crn_rotating.gif'), dpi=92,)