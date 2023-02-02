#Read CAN Interface and send to UDP Multicast address
import time
import can
from can.interfaces.udp_multicast import UdpMulticastBus

with UdpMulticastBus(port=1337) as udpbus:
    logger = can.Logger('test.txt')
    buffer = can.BufferedReader()
    can.Notifier(udpbus, [buffer])
    try:
        while True:
            msg = buffer.get_message()
            #print(msg)
            logger(msg)
    except KeyboardInterrupt:
        buffer.stop()
        print('Stopping...')
        pass