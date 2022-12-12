import pytest
import json
import os
from tests.types import UserOperation


@pytest.fixture
def badSigUserOp(wallet_contract):
    return UserOperation(
        wallet_contract.address,
        hex(0),
        '0x',
        wallet_contract.encodeABI(fn_name='setState', args=[1111111]),
        hex(30000),
        hex(1213945),
        hex(47124),
        hex(2107373890),
        hex(1500000000),
        '0x',
        '0xdead'
    )


@pytest.fixture(scope='session')
def openrpcschema():
    current_dirname = os.path.dirname(__file__)
    spec_filename = 'openrpc.json'
    spec_path = os.path.realpath(current_dirname + '/../../spec/')
    return json.load(open(os.path.join(spec_path, spec_filename)))


@pytest.fixture
def schema(openrpcschema, method):
    return next(m['result']['schema'] for m in openrpcschema['methods'] if m['name'] == method)
