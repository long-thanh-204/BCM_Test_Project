import can

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

    print("Waiting for CAN messages...")

    while True:
        msg = bus.recv(timeout=1.0)
        if msg:
            print(
                f"ID: {hex(msg.arbitration_id)} | "
                f"Data: {msg.data.hex()} | "
                f"Timestamp: {msg.timestamp}"
            )

if __name__ == "__main__":
    main()
