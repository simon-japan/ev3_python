import rpyc

robo_conn = rpyc.classic.connect('ev3dev.local')
ev3 = robo_conn.modules['ev3dev.ev3']

right_wheel = ev3.LargeMotor('outC')
left_wheel = ev3.LargeMotor('outB')
steering = ev3.MediumMotor('outA')

assert right_wheel.connected
assert left_wheel.connected
assert steering.connected


def drive(time=1000, speed=600, forwards=True):
    polarity = 'inversed' if forwards else 'normal'
    right_wheel.polarity = polarity
    left_wheel.polarity = polarity
    right_wheel.run_timed(time_sp=time, speed_sp=speed)
    left_wheel.run_timed(time_sp=time, speed_sp=speed)


def turn(degree):
    """
    :param degree: Positive means right, negative means left.
    """
    if degree < 0:
        steering.polarity = 'inversed'
        degree = 0 - degree
    else:
        steering.polarity = 'normal'
    steering.run_timed(time_sp=degree, speed_sp=500)


def speak(words):
    ev3.Sound.speak(words).wait()
