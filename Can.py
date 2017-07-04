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
import sys
import time
import can
from random import randint

log = logging.getLogger(__name__)

class Can:
    '''
        CAN implementation for LIOTA. It uses python-can internally.
    '''
    def __init__(self, channel=None, can_filters=None, bustype, listeners, enable_authentication=True, data=None, timeout=None):
        
        self.channel =  channel
        self.bustype = bustype
        self.can_filters = can_filters
        self.listeners = listeners
        self.enable_authentication = enable_authentication
        self.data = data
        self.timeout=timeout


    def connect(self):
        bus = can.interface.Bus(bustype=self.bustype, channel=self.channel) 
        log.info("Connected to Can Bus")

    def send(self, arbitration_id, data, extended_id):
        message = can.Message(arbitration_id=arbitration_id, data=data, extended_id=extended_id)  
        try:
            self.bus.send(message)
            print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("Message not sent")
            log.error("Message not sent over channel")

        
    def recv(self, timeout):
        return self.bus.recv(self.timeout)
    
    def set_filters(self):
        self.bus.set_filters(self.can_filters)
    
    def flush_tx_buffer(self):
        self.bus.flush_tx_buffer()

    def send_periodic(self, data, arbitration_id, extended_id, period, duration=None):
        '''
        :param float period:
            Period in seconds between each message
        :param float duration:
            The duration to keep sending this message at given rate. If
            no duration is provided, the task will continue indefinitely.

        :return: A started task instance
        :rtype: can.CyclicSendTaskABC
        '''
        message = can.Message(arbitration_id=arbitration_id, data=data, extended_id=extended_id)
        task = can.send_periodic(message, period, duration)
        assert isinstance(task, can.CyclicSendTaskABC)
        return task

    def shutdown(self):
        self.bus.shutdown()
    
    def stop(self):
        #To-Do: Add using Notifier

class CanMessagingAttributes:

    def __init__(self, edge_system_name=None, pub_timestamp=0.0, arbitration_id=0, extended_id=True, is_remote_frame=False,
                is_error_frame=False, dlc=None):

        if edge_system_name:
            
            self.extended_id = True
            self.arbitration_id = randint(0,2**29-1) #If extended _id is true arbitration_id can be 29-bits else 11-bits
            
        else:
            #  When edge_system_name is None, arbitration_id and extended_id must be provided
            self.arbitration_id = arbitration_id
            self.extended_id = extended_id

        self.pub_timestamp = pub_timestamp
        self.arbitration_id = arbitration_id
        self.id_type = extended_id
        self.is_remote_frame = is_remote_frame
        self.is_error_frame = is_error_frame
    
        if dlc is None:
            self.dlc = len(self.data)
        else:
            self.dlc = dlc

        assert self.dlc <= 8, "data link count was {} but it must be less than or equal to 8".format(self.dlc)
  
    
    

                 

    