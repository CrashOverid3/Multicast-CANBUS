#Read CAN Interface and send to UDP Multicast address
import time
import can
from can.interfaces.udp_multicast import UdpMulticastBus

with UdpMulticastBus(channel='224.1.1.1') as udpbus:
    buffer = can.BufferedReader()
    can.Logger('test.txt').on_message_received(buffer.get_message())
#    try:
#        while True:
    can.Notifier(udpbus, [buffer])
#    except KeyboardInterrupt:
#        buffer.stop()
        #writer.stop()
#        print('Stopping...')
#        pass