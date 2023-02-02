#Read CAN Interface and send to UDP Multicast address
import time
import can
from can.interfaces.udp_multicast import UdpMulticastBus

with UdpMulticastBus(port=1337) as udpbus, \
                     can.ThreadSafeBus(interface='socketcan', channel='vcan0') as hwrbus:
    buffer = can.BufferedReader()
    can.Notifier(hwrbus, [buffer])
    try:
        while True:
            msg = buffer.get_message()
            #print(msg)
            try:
                udpbus.send(msg)
            except can.CanError:
                print('MSG FAILED!')
    except KeyboardInterrupt:
        buffer.stop()
        print('Stopping...')
        pass