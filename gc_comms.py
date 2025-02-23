import serial
import time

# Set the COM port to the one found in Device Manager (e.g., COM4)
com_port = 'COM4'

# Create a serial connection to the Raspberry Pi
bluetooth_serial = serial.Serial(com_port, baudrate=9600, timeout=1)

# Send a command to the Raspberry Pi
bluetooth_serial.write("Hello Raspberry Pi!".encode())

# Wait for a response from the Raspberry Pi
time.sleep(2)  # Wait for the response
response = bluetooth_serial.readline().decode().strip()
print(f"Received response: {response}")

# Close the connection
bluetooth_serial.close()