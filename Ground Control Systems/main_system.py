import comms_system
import time

modes = ["SLEEP", "SCIENCE", "COMMS", "DEORBIT"]

print("""
+========================+
| SELECT SATELLITE MODES |
+========================+
|    MODES   |   NUMBER  |
+========================+
|    SLEEP   |     0     |
|   SCIENCE  |     1     |
|    COMMS   |     2     |
|   DEORBIT  |     3     |
+========================+""")
print("="*53)

while True:
    mode_request = int(input("Enter Mode Number: "))
    duration = int(input("Duration of the Mode (Seconds): "))
    mode = modes[mode_request]

    print("Sent request to change to {} mode for {} seconds".format(mode, duration))
    if mode == "COMMS":
        comms_system.send_mode_data(mode, duration)
        time.sleep(10)
        comms_system.recieve_data()
    elif mode == "DEORBIT":
        comms_system.send_mode_data(mode, duration)
        print("="*53)
        break
    else:
        comms_system.send_mode_data(mode, duration)
        time.sleep(duration)

    print("="*53)