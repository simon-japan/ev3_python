import truck


class TruckRequestProcessor(object):

    def process_request(self, msg_body):
        print("Processing request: {}".format(msg_body))

        if "command_name" not in msg_body:
            raise ValueError("No command found in message body")
        command_name = msg_body["command_name"]
        if "args" not in msg_body:
            raise ValueError("No args found in message body")
        args = msg_body["args"]

        if command_name == "drive":
            response = self.process_drive_command(args)
        elif command_name == "turn":
            response = self.process_turn_command(args)
        elif command_name == "speak":
            response = self.process_speak_command(args)
        else:
            raise ValueError("Command {} not recognised.".format(command_name))

        return response

    @staticmethod
    def process_drive_command(args):
        time = int(args["time"])
        speed = int(args["speed"])
        reverse = bool(args["reverse"])
        truck.drive(time=time, speed=speed, reverse=reverse)
        return True

    @staticmethod
    def process_turn_command(args):
        degree = int(args["degree"])
        truck.turn(degree=degree)
        return True

    @staticmethod
    def process_speak_command(args):
        words = int(args["words"])
        truck.say(words=words)
        return True
