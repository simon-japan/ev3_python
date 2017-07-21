#!/usr/bin/env python3

import command_relay
import request_processor

truck_command_processor = request_processor.TruckRequestProcessor()
relay = command_relay.CommandRelay(request_processor=truck_command_processor)
relay.start_listening()
