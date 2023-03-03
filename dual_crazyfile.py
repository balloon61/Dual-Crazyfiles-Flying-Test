import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M/E7E7E706'
URI2 = 'radio://0/90/2M/E7E7E707'
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # We take off when the commander is created
        with MotionCommander(scf) as mc:
            print('Taking off!')
            time.sleep(1)
            with SyncCrazyflie(URI2) as scf2:
                # We take off when the commander is created
                with MotionCommander(scf2) as mc2:
                    print('Taking off!')
                    time.sleep(1)

                    # There is a set of functions that move a specific distance
                    # We can move in all directions
                    print('Moving forward 0.5m')
                    mc.forward(0.5)
                    mc2.forward(1.5)

                    # Wait a bit
                    time.sleep(1)

                    print('Moving up 0.2m')
                    mc.up(0.2)
                    mc2.down(0.2)
                    # Wait a bit
                    time.sleep(1)


                    # We land when the MotionCommander goes out of scope
                    print('Landing!')

            # We land when the MotionCommander goes out of scope
            print('Landing!')