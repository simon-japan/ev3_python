from .context import request_processor

import pytest


def test_process_request():
    processor = request_processor.RequestProcessor()

    result = 0

    def cb(a, b):
        nonlocal result
        result = a + b

    processor.register_function("f", cb)
    request = {
        'command_name': 'f',
        'args':
            {
                'a': 1,
                'b': 2
            }
    }
    processor.process_request(request)
    assert result == 3
