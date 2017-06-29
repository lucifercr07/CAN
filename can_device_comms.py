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

from liota.device_comms.device_comms import DeviceComms
from liota.lib.transports.can import Can

log = logging.getLogger(__name__)


class CanDeviceComms(DeviceComms):
    """
    DeviceComms for Can bus protocol
    """

    def __init__(self, channel=None, can_filters=None, bus, listeners, timeout=None, enable_authentication=False, timestamp=0.0, is_remote_frame=False, extended_id=True,
                is_error_frame=False, arbitration_id=0,dlc=None, data=None):
        """
        :param channel: The can interface identifier. Expected type is backend dependent.
        :param can_filters:A list of dictionaries each containing a "can_id" and a "can_mask".
            >>> [{"can_id": 0x11, "can_mask": 0x21}]
            A filter matches, when ``<received_can_id> & can_mask == can_id & can_mask``
        ::param bus: The ref:`bus` to listen too.
        :param listeners: An iterable of class:`can.Listeners`
        :param timeout: An optional maximum number of seconds to wait for any message.
         Messages can use extended identifiers, be remote or error frames, and contain data.
        """
        self.channel = channel  
        self.bus = bus
        self.can_filters=can_filters
        self.listeners = listeners
        self.timeout = timeout
        self.enable_authentication=enable_authentication
        self.timestamp = timestamp
        self.is_remote_frame = is_remote_frame
        self.extended_id = extended_id
        self.is_error_frame = is_error_frame
        self.arbitration_id = arbitration_id
        self.dlc = dlc
        self.data = data
        

    def _connect(self):
        
        self.client = Can(self.channel, self.can_filters=can_filters, self.bus=bus, self.listeners=listeners,self.timeout = timeout,
                        self.timestamp = timestamp, self.id_type = extended_id,self.is_error_frame = is_error_frame,self.is_remote_frame = is_remote_frame,
                        self.arbitration_id = arbitration_id)


    def _disconnect(self):
        #how to stop (can.Notifier has stop method)

    def send(self):
        self.client.send()

    def receive(self):
        self.client.recv()

    def set_filters(self):
        self.client.set_filters()

    def flush_tx_buffer(self):
        self.client.flush_tx_buffer()

    def shutdown():
        self.client.shutdown()