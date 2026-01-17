import can
import cantools

DBC_PATH = r"D:\DBC file\BCM-dbc-file.dbc"

def open_can_bus():
    bus = can.interface.Bus(
        channel=0,
        interface='kvaser',
        bitrate=500000
    )
    return bus

def load_dbc():
    return cantools.database.load_file(DBC_PATH)
