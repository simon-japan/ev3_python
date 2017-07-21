#!/usr/bin/env python3

from robot_remote import request_processor
from robot_remote import command_relay
from robot_remote import truck

truck_command_processor = request_processor.RequestProcessor({
    'drive': truck.drive,
    'turn': truck.turn,
    'say': truck.say
})
relay = command_relay.CommandRelay(request_processor=truck_command_processor)
relay.start_listening()
