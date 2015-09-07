from numpy import sum
from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .jump import Jump
from .dance import Dance
from .face_tracking import FaceTracking
from .postures import (BasePosture, RestPosture, SafePowerUp)


class PoppyErgoJr(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(sum, axis=0)

        robot.attach_primitive(SafePowerUp(robot), 'safe_power_up')

        robot.attach_primitive(Dance(robot), 'dance')
        robot.attach_primitive(Jump(robot), 'jump')

        robot.attach_primitive(BasePosture(robot, 2.), 'base_posture')
        robot.attach_primitive(RestPosture(robot, 2.), 'rest_posture')

        for m in robot.motors:
            m.pid = (4, 2, 0)
            m.torque_limit = 70.
            m.led = 'off'

        if not robot.simulated:
            robot.attach_primitive(FaceTracking(robot, 10, robot.face_detector),
                                   'face_tracking')
