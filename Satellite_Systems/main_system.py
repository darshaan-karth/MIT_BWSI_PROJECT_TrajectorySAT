from power_temp_system import main as power_temp_system
from adcs_system import main as adcs_system
from camera_system import main as camera_system

voltage, temperature = power_temp_system()
acceleration, gyro, magnetic = adcs_system()

camera_system()

print("Voltage: {}V".format(voltage))
print("Temperature: {}'C".format(temperature))
print("Acceleration: {} (m/s^2)".format(acceleration))
print("Gyro: {} (rad/s)".format(gyro))
print("Magnetic: {} (gauss)".format(magnetic))