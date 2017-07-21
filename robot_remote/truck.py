from . import robot_body

RIGHT_WHEEL = 'c'
LEFT_WHEEL = 'b'
STEERING_WHEEL = 'a'

body = robot_body.RobotBody()
body.motors[RIGHT_WHEEL] = robot_body.ConfiguredMotor(default_polarity=robot_body.Polarity.INVERSED)
body.motors[LEFT_WHEEL] = robot_body.ConfiguredMotor(default_polarity=robot_body.Polarity.INVERSED)
body.detect_connected_motors()


def drive(time=1000, speed=600, reverse=False):
    body.get_motor(RIGHT_WHEEL).run_timed(time=time, speed=speed, reverse=reverse)
    body.get_motor(LEFT_WHEEL).run_timed(time=time, speed=speed, reverse=reverse)


def turn(degree=100):
    """
    :param degree: Positive means right, negative means left.
    """
    reverse = False
    if degree < 0:
        reverse = True
        degree = 0 - degree
    body.get_motor(STEERING_WHEEL).run_timed(time=degree, speed=500, reverse=reverse)


def say(words):
    body.speak(words)
