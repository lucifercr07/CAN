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
from liota.lib.transports.Can import Can, CanMessagingAttributes 
import random

log = logging.getLogger(__name__)


class CanDeviceComms(DeviceComms):
	"""
	DeviceComms for Can bus protocol
	"""

	def __init__(self, can_msg_attr, channel=None, can_filters=None, bustype=None, listeners=None):
		"""
		:param channel: The can interface identifier. Expected type is backend dependent.
		:param can_filters:A list of dictionaries each containing a "can_id" and a "can_mask".
			>>> [{"can_id": 0x11, "can_mask": 0x21}]
			A filter matches, when ``<received_can_id> & can_mask == can_id & can_mask``
		:param bustype: The ref:`bus` to listen too.
		:param listeners: An iterable of class:`can.Listeners`
		:param userdata: userdata is used to store messages coming from the receive channel.
		"""
		self.channel = channel
		if bustype is None:
			log.error("Bus Type can't be None")
			raise TypeError("Bus Type can't be none")
		else:
			self.bustype=bustype  
		self.bustype = bustype
		self.can_filters=can_filters
		self.listeners = listeners
		#self.userdata = Queue.Queue()
		if can_msg_attr is None:
			log.info("arbitration_id will be auto-generated and extended_id will be true by default")
			self.msg_attr = CanMessagingAttributes(arbitration_id=random.randint(0,2**29-1),extended_id=True)
		elif isinstance(can_msg_attr, CanMessagingAttributes):
			log.info("User configured arbitration_id and extended_id")
			self.msg_attr = can_msg_attr
		else:
			log.error("can_msg_attr should either be None or of type CanMessagingAttributes")
			raise TypeError("can_msg_attr should either be None or of type CanMessagingAttributes")
		self._connect()

	def _connect(self):
		self.client = Can(self.channel, self.can_filters, self.bustype, self.listeners)
		self.client.connect()

	def _disconnect(self):
		raise NotImplementedError

	def send(self, data, msg_attr=None):
		'''
		:param data(bytearray): data sent to can bus
		:param msg_attr : CanMessaging attribute instance
		 Messages can use extended identifiers, be remote or error frames, and contain data.
		'''
		if data is None:
			raise TypeError("Data can't be none")

		if msg_attr:
			self.client.send(msg_attr.arbitration_id, data, msg_attr.extended_id)
		else:
			self.client.send(self.msg_attr.arbitration_id, data, self.msg_attr.extended_id)

	def receive(self, timeout=0):
		'''
		:param timeout(float): Seconds to wait for a message
		'''
		msg = self.client.recv(timeout)  
		if msg is not None:
			return msg
		else:
			print("No message received")
			log.error("No message received")

	def set_filters(self):
		self.client.set_filters(self.can_filters)

	def flush_tx_buffer(self):
		self.client.flush_tx_buffer()

	def send_periodic(self, data, msg_attr=None, period=0.0, duration=None):
		task = self.client.send_periodic(data, msg_attr.arbitration_id, msg_attr.extended_id, period, duration)
		#To-Do how the task will be used

	def shutdown():
		self.client.shutdown()