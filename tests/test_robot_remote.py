from .context import request_processor

import pytest


def test_process_request():
    processor = request_processor.RequestProcessor()

    def cb(a, b):
        return a + b

    processor.register_function("f", cb)
    request = {
        'command_name': 'f',
        'args':
            {
                'a': 1,
                'b': 2
            }
    }
    assert request_processor.process_request(request) == 3