import numpy as np 
import matplotlib.pyplot as plt

#SIMULATION PARAMETERS 
size = 200       #number of cells 
c = 1.0          
dx = 1.0         
dt = dx / c     
total_steps = 300 
source_pos = int(size / 2) # Source position in the middle
source_width = 10.0
delay = 3 * source_width
imp0 = 377.0      # Impedance of free space (approx)

ez = np.zeros(size) # Electric field array
hy = np.zeros(size) # Magnetic field array (staggered grid)

plt.ion() # Turn on interactive plotting
fig, ax = plt.subplots()
line, = ax.plot(ez)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("Position (dx)")
ax.set_ylabel("Field Amplitude")
plt.title("1D FDTD Simulation")

for time_step in range(total_steps):

    hy[:-1] = hy[:-1] + (ez[1:] - ez[:-1]) / imp0 * dt / dx
    ez[1:] = ez[1:] + (hy[1:] - hy[:-1]) * imp0 * dt / dx
    ez[source_pos] += np.exp(-(time_step - delay)**2 / (2.0 * source_width**2))
    
    if time_step % 5 == 0: # Update plot every 5 steps
        line.set_ydata(ez)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.001)

plt.ioff()
plt.show()
