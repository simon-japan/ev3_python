import rpyc


class RobotBody(object):
    def __init__(self, ev3_address='ev3dev.local'):
        self.ev3_address = ev3_address
        self.robo_conn = None
        self.motors = {}

    def connect(self):
        self.robo_conn = rpyc.classic.connect(self.ev3_address)
        ev3 = self.robo_conn.modules['ev3dev.ev3']
        for motor in ev3.list_motors():
            letter = motor.address[-1:].lower()
            self.motors[letter] = motor

    def _get_motor(self, output_letter):
        if output_letter not in 'abcd':
            raise ValueError("Motor port letter {} not valid, must be in [a,b,c,d]".format(output_letter))
        if output_letter not in self.motors:
            print("No motor mapped to port {}; checking for attached motor...".format(output_letter))
            #motor = self._detect_motor(output_letter)
            #if motor is None:
            #    raise ValueError("No motor".format(output_letter))
        return self.motors[output_letter]

    # def _detect_motor(self, output_letter):

    def run_timed(self, motor_letter='a', time=1000, speed=600, forwards=True):
        motor = self._get_motor(motor_letter)
        polarity = 'inversed' if forwards else 'normal'
        motor.polarity = polarity
        motor.run_timed(time_sp=time, speed_sp=speed)

