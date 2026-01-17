import can

def open_can_channel(interface, channel, bitrate):
    bus = can.interface.Bus(
        interface=interface,
        channel=channel,
        bitrate=bitrate
    )
    print("CAN channel opened")
    return bus


def send_can(bus, arbitration_id, data):
    msg = can.Message(
        arbitration_id=arbitration_id,
        data=data,
        is_extended_id=False
    )
    bus.send(msg)
    print(f"[TX] {msg}")


def receive_can(bus):
    msg = bus.recv()
    if msg:
        print(f"[RX] {msg}")
    return msg
