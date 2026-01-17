# testcases/bcm_light_test.py

import time
import cantools
from utils.can_utils import send_can, receive_can


DBC_PATH = r"D:\DBC file\BCM-dbc-file.dbc"
MESSAGE_NAME = "BCM_Light_Status"


def test_bcm_light_status(bus):
    print("\n=== BCM LIGHT STATUS TEST START ===")

    # Load DBC
    db = cantools.database.load_file(DBC_PATH)
    msg = db.get_message_by_name(MESSAGE_NAME)

    print(f"[INFO] Loaded DBC message: {MESSAGE_NAME}")

    # -------------------------
    # STEP 1: Prepare TX data
    # -------------------------
    tx_signals = {
        
        "Hazard": 1,
        "TurnLeft": 0,
        "TurnRight": 0
    }

    tx_data = msg.encode(tx_signals)

    # -------------------------
    # STEP 2: Send CAN message
    # -------------------------
    print("[STEP] Sending BCM_Light_Status...")
    send_can(bus, msg.frame_id, tx_data)

    time.sleep(0.2)

    # -------------------------
    # STEP 3: Receive CAN
    # -------------------------
    print("[STEP] Waiting for response...")

    rx_msg = receive_can(bus)

    if rx_msg is None:
        print("[FAIL] No CAN frame received")
        return

    if rx_msg.arbitration_id != msg.frame_id:
        print("[FAIL] Received wrong CAN ID")
        return

    # -------------------------
    # STEP 4: Decode & Check
    # -------------------------
    rx_signals = msg.decode(rx_msg.data)

    print("[RX SIGNALS]", rx_signals)

    if rx_signals["Hazard"] == 1:
        print("[PASS] Hazard ON as expected")
    else:
        print("[FAIL] Hazard status incorrect")

    print("=== BCM LIGHT STATUS TEST END ===\n")
