#!/usr/bin/env python3

from . import request_processor
from . import command_relay

truck_command_processor = request_processor.TruckRequestProcessor()
relay = command_relay.CommandRelay(request_processor=truck_command_processor)
relay.start_listening()
