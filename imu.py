import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL

i2c = board.I2C()
accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)

def main():
    while True:
        accelx, accely, accelz = accel_gyro.acceleration
        print("| accelx : {} || accely : {} || accelz : {} |".format(round(accelx,3), round(accely,3), round(accelz,3)))
        time.sleep(0.1)

if __name__ == '__main__':
    main()
