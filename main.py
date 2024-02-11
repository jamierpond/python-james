import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(1, 100, 400)  # Temperature range from 1 to 100
y = 1 / x**2  # Heat applied, inverse square of temperature

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Heat vs Temperature')
plt.title('Heat Applied vs. Temperature Increase (Inverse Square Law)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Heat Applied (arbitrary units)')
plt.legend()
plt.grid(True)
plt.show()

