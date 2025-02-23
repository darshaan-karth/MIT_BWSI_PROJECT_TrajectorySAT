import serial

# Open the Bluetooth serial port (change '/dev/rfcomm0' if necessary)
bluetooth_serial = serial.Serial('/dev/rfcomm0', baudrate=9600, timeout=1)

print("Waiting for data from Windows...")

while True:
    if bluetooth_serial.in_waiting > 0:
        data = bluetooth_serial.readline().decode().strip()
        print(f"Received command: {data}")
        # Respond to the command (optional)
        bluetooth_serial.write("Command received".encode())