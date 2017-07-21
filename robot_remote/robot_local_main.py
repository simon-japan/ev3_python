#!/usr/bin/env python3

from . import request_processor
from . import command_relay
from . import truck

truck_command_processor = request_processor.RequestProcessor({
    'drive': truck.drive,
    'turn': truck.turn,
    'say': truck.say
})
relay = command_relay.CommandRelay(request_processor=truck_command_processor)
relay.start_listening()
