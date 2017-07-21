"""
Module to handle inbound commands (parsing the contents and calling a registered callback).
"""

import copy


class RequestProcessor(object):
    """
    Class to handle inbound commands (parsing the contents and calling a registered callback).
    """
    def __init__(self, callbacks=None):
        """
        Initialize the RequestProcessor.
        """
        if callbacks:
            self.callbacks = copy.copy(callbacks)
        else:
            self.callbacks = {}

    def register_function(self, name, callback):
        """
        Add a callback.

        :param name: the command name
        :type name: basestring
        :param callback: a function
        :type callback: function
        """
        self.callbacks[name] = callback

    def process_request(self, msg_body):
        """
        Extract command name and arguments; if the command name has been registered, try to call the assigned function
        passing it the arguments.

        :param msg_body: a json object with 'command_name' and 'args'
        :type msg_body: dict
        """
        print("Processing request: {}".format(msg_body))

        if "command_name" not in msg_body:
            raise ValueError("No command found in message body")
        command_name = msg_body["command_name"]
        if "args" not in msg_body:
            raise ValueError("No args found in message body")
        args = msg_body["args"]

        if command_name in self.callbacks:
            self.callbacks[command_name](**args)
        else:
            raise ValueError("Command {} not recognised.".format(command_name))
