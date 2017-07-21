from setuptools import setup

setup(
   name='robot_remote',
   version='1.0',
   description='For executing commands from a remote source on an ev3',
   author='Simon Holland',
   author_email='simon.holland@gmail.com',
   packages=['robot_remote'],
   install_requires=['pika', 'ev3dev'],
)