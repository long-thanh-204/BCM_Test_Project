from utils.can_utils import open_can_channel
from testcases.bcm_light_test import test_bcm_light_status

# -----------------------------
# CAN CONFIG
# -----------------------------
CAN_INTERFACE = "kvaser"
CAN_CHANNEL = 0
BITRATE = 500000


def main():
    # Open CAN
    bus = open_can_channel(
        interface=CAN_INTERFACE,
        channel=CAN_CHANNEL,
        bitrate=BITRATE
    )

    # Run test
    test_bcm_light_status(bus)


if __name__ == "__main__":
    main()
