"""
Classes for controlling EV3 robots.
Generic features that could be used in a variety of robots.
"""

from enum import Enum
import ev3dev.ev3 as ev3


class Polarity(Enum):
    NORMAL = 'normal'
    INVERSED = 'inversed'


class RobotBody(object):
    """
    Represents an EV3 unit.
    Auto-detects motors that are connected.
    Can be used as a simple interface for sending commands to the motors.
    """
    def __init__(self):
        motors = {}
        self.motors = motors

    def detect_connected_motors(self):
        for motor in ev3.list_motors():
            letter = motor.address[-1:].lower()
            if letter in self.motors:
                self.motors[letter].set_motor(motor)
            else:
                self.motors[letter] = ConfiguredMotor(motor=motor)

    def get_motor(self, output_letter):
        if output_letter not in 'abcd':
            raise ValueError("Motor port letter {} not valid, must be in [a,b,c,d]".format(output_letter))
        if output_letter not in self.motors:
            print("No motor mapped to port {}; checking for attached motor...".format(output_letter))
            #motor = self._detect_motor(output_letter)
            #if motor is None:
            #    raise ValueError("No motor".format(output_letter))
        return self.motors[output_letter]

    # def _detect_motor(self, output_letter):

    @staticmethod
    def speak(words):
        ev3.Sound.speak(words).wait()


class ConfiguredMotor(object):
    """
    Represents a motor used for a specific purpose in a robot body.
    Provides an interface that abstracts over the low-level motor commands.
    """
    def __init__(self, motor=None, default_polarity=Polarity.NORMAL):
        """
        :param default_polarity: The default polarity to use for this motor
        :type default_polarity: Polarity
        """
        self.motor = motor
        self.default_polarity = default_polarity
        self.reverse_polarity = Polarity.NORMAL if default_polarity == Polarity.INVERSED else Polarity.INVERSED

    def set_motor(self, motor):
        self.motor = motor

    def run_timed(self, time=1000, speed=600, reverse=False):
        if reverse:
            self.motor.polarity = self.reverse_polarity.value
        else:
            self.motor.polarity = self.default_polarity.value
        self.motor.run_timed(time_sp=time, speed_sp=speed)
