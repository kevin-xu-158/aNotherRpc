#!/usr/bin/python

'''
controller.py - Socket implementation of Google's Protocol Buffers RPC
service interface.

This package contains classes providing a socket implementation of the
RPCController abstract class.

'''

# Third-party imports
import google.protobuf.service as service

# Module imports
from nrpc import nrpc_pb2


class SocketRpcController(service.RpcController):
    ''' 
    RpcController implementation to be used by the SocketRpcChannel class.
    The RpcController is used to mediate a single method call.
    '''

    def __init__(self):
        '''Constructor which initializes the controller's state.'''
        self._fail = False
        self._error = None
        self._error_code = 0

    def handleError(self, error_code, message=''):
        '''Log and set the controller state.'''
        self._fail = True
        self._error_code = error_code
        self._error = message

    def reset(self):
        '''Resets the controller i.e. clears the error state.'''
        self._fail = False
        self._error = None
        self._error_code = 0

    def failed(self):
        '''Returns True if the controller is in a failed state.'''
        return self._fail

    def error(self):
        return self._error

    def errorCode(self):
        return self._error_code
