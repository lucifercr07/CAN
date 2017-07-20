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

import unittest
import mock
from liota.device_comms.canbus_device_comms import CanBusDeviceComms
from liota.device_comms.device_comms import DeviceComms
from liota.lib.transports.CanBus import CanBusMessagingAttributes

bus_type = "virtual"

class TestCanBusDeviceComms(unittest.TestCase):

	
	def test_CanBusDeviceComms_fail_without_bustype(self):
		with self.assertRaises(Exception):
			deviceComms = CanBusDeviceComms("asd")
			assertNotIsInstance(deviceComms, CanBusDeviceComms)

		with self.assertRaises(Exception):
			deviceComms = CanBusDeviceComms()
			assertNotIsInstance(deviceComms, CanBusDeviceComms)

	def test_CanBusDeviceComms_takes_bustype(self):
		
		deviceComms = CanBusDeviceComms(bustype = bus_type, can_msg_attr=None)
		assert isinstance(deviceComms, CanBusDeviceComms)

	def test_CanBusDeviceComms_fail_with_invalidArg_msg_attr(self):
		with self.assertRaises(Exception):
			deviceComms = CanBusDeviceComms(bustype = bus_type, can_msg_attr="asd")
			assertNotIsInstance(deviceComms, CanBusDeviceComms)

	def test_CanBusDeviceComms_pass_with_validArg_msg_attr(self):
		mock_can_msg_attr = mock.create_autospec(CanBusMessagingAttributes)
		deviceComms = CanBusDeviceComms(bustype = bus_type, can_msg_attr=mock_can_msg_attr)
		assert isinstance(deviceComms, CanBusDeviceComms)


if __name__ == '__main__':
	unittest.main()
