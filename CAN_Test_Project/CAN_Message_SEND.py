import can
import time

# ===== CẤU HÌNH Kvaser =====
CAN_INTERFACE = "kvaser"
CAN_CHANNEL = 0
BITRATE = 500000

def main():
    bus = can.Bus(
        interface=CAN_INTERFACE,
        channel=CAN_CHANNEL,
        bitrate=BITRATE
    )

    msg = can.Message(
        arbitration_id=0x100,
        data=[0x11, 0x21, 0x35, 0x44, 0x55, 0x68, 0x77, 0x88],
        is_extended_id=False
    )

    print("Start sending CAN messages...")

    while True:
        try:
            bus.send(msg)
            print(f"Sent: {msg}")
            time.sleep(1)
        except can.CanError:
            print("Send failed")

if __name__ == "__main__":
    main()
