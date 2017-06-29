# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------#
#  Copyright © 2015-2016 VMware, Inc. All Rights Reserved.                    #
#                                                                             #
#  Licensed under the BSD 2-Clause License (the “License”); you may not use   #
#  this file except in compliance with the License.                           #
#                                                                             #
#  The BSD 2-Clause License                                                   #
#                                                                             #
#  Redistribution and use in source and binary forms, with or without         #
#  modification, are permitted provided that the following conditions are met:#
#                                                                             #
#  - Redistributions of source code must retain the above copyright notice,   #
#      this list of conditions and the following disclaimer.                  #
#                                                                             #
#  - Redistributions in binary form must reproduce the above copyright        #
#      notice, this list of conditions and the following disclaimer in the    #
#      documentation and/or other materials provided with the distribution.   #
#                                                                             #
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"#
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE  #
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE #
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE  #
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR        #
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF       #
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS   #
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN    #
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)    #
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF     #
#  THE POSSIBILITY OF SUCH DAMAGE.                                            #
# ----------------------------------------------------------------------------#

import logging
import os
import ssl
import sys
import time
import can

log = logging.getLogger(__name__)

class Can():
    '''
        CAN implementation for LIOTA. It uses python-can internally.
    '''
    def __init__(self, channel=None, can_filters=None, bus, listeners, timeout=None, enable_authentication=False, timestamp=0.0, is_remote_frame=False, extended_id=True,
                is_error_frame=False, arbitration_id=0,dlc=None, data=None):
        
        self.channel =  channel
        self.bus = bus
        self.can_filters = can_filters
        self.listeners = listeners
        self.timeout = timeout
        self.timestamp = timestamp
        self.id_type = extended_id
        self.is_error_frame = is_error_frame
        self.is_remote_frame = is_remote_frame
        self.arbitration_id = arbitration_id

    def connect(self):
        bus = can.interface.Bus(self.channel) #args inside Bus()?? what abt cls,other,*args??

    def send(self):
        message = can.Message(self.arbitration_id, self.data, self.extended_id=True)
        try:
            self.bus.send(message)
            print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("Message not sent")

        
    def recv(self):
        self.bus.recv(self.timeout)
    
    def set_filters(self):
        self.bus.set_filters(self.can_filters)
    
    def flush_tx_buffer(self):
        self.bus.flush_tx_buffer()

    def shutdown(self):
        self.bus.shutdown()
    
    def stop(self):


    
    
    

                 

    