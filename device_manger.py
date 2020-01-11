from gpiozero import OutputDevice, Motor

from time import sleep


DEVICE_1 = 4
DEVICE_2 = 17
DEVICE_3 = 27
DEVICE_4 = 22
device1 = OutputDevice(DEVICE_1, active_high=False, initial_value=False)
device2 = OutputDevice(DEVICE_2, active_high=False, initial_value=False)
device3 = OutputDevice(DEVICE_3, active_high=False, initial_value=False)
device4 = OutputDevice(DEVICE_4, active_high=False, initial_value=False)

def update_device(device='dev1',status='on'):
    if device == 'dev1'  :return change_status(device1,status)
    elif device == 'dev2':return change_status(device2,status)
    elif device == 'dev3':return change_status(device3,status)
    elif device == 'dev4':return change_status(device4,status)
    else:return False


def change_status(device,status):
    try:
        if status=='on':
            print("Setting device: OFF")
            device.off()
            return True
        else:
            print("Setting device: ON")
            device.on()
            return True
    except Exception as e:
        print('<--- error --->')
        print(e)
        print('<--- end of error msg <---')
        return False
