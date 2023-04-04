import time
import zcanpro

stopTask = False

def z_notify(type, obj):
    zcanpro.write_log("Notify " + str(type) + " " + str(obj))
    if type == "stop":
        zcanpro.write_log("Stop...")
        global stopTask
        stopTask = True

def test_dev_auto_send(busID):
    autoSendFrms = [
        {
            "can_id": 0x280,
            "is_canfd": 0,
            "canfd_brs": 0,
            "data": [0, 0, 0, 0, 0, 80, 0, 0],
            "interval_ms": 500
        },
        {
            "can_id": 0x570,
            "is_canfd": 0,
            "canfd_brs": 0,
            "data": [91, 0, 0, 0, 0, 0, 0, 0],
            "interval_ms": 500
        },
        {
            "can_id": 0x660,
            "is_canfd": 0,
            "canfd_brs": 0,
            "data": [2, 0, 0, 0, 0, 0, 0, 0],
            "interval_ms": 500
        },
        {
            "can_id": 0x4A0,
            "is_canfd": 0,
            "canfd_brs": 0,
            "data": [0, 0, 0, 4, 0, 0, 0, 0],
            "interval_ms": 500
        }
    ]

    result = zcanpro.dev_auto_send_start(busID, autoSendFrms)
    if result == 0:
        zcanpro.write_log("start device auto send failed! ")
    else:
        zcanpro.write_log("device auto send started... ")

    global stopTask
    stopTask = False
    while not stopTask:
        time.sleep(0.1)

    result = zcanpro.dev_auto_send_stop(busID)
    if result == 0:
        zcanpro.write_log("stop device auto send failed! ")
    else:
        zcanpro.write_log("device auto send stopped. ")

def z_main():
    buses = zcanpro.get_buses()
    zcanpro.write_log("Get buses: " + str(buses))
    if len(buses) >= 1:
        test_dev_auto_send(buses[0]["busID"])