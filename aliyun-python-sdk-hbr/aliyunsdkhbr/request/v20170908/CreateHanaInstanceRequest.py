# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkhbr.endpoint import endpoint_data

class CreateHanaInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateHanaInstance','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HanaName(self):
		return self.get_query_params().get('HanaName')

	def set_HanaName(self,HanaName):
		self.add_query_param('HanaName',HanaName)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_UseSsl(self):
		return self.get_query_params().get('UseSsl')

	def set_UseSsl(self,UseSsl):
		self.add_query_param('UseSsl',UseSsl)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)

	def get_AlertSetting(self):
		return self.get_query_params().get('AlertSetting')

	def set_AlertSetting(self,AlertSetting):
		self.add_query_param('AlertSetting',AlertSetting)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_Host(self):
		return self.get_query_params().get('Host')

	def set_Host(self,Host):
		self.add_query_param('Host',Host)

	def get_ValidateCertificate(self):
		return self.get_query_params().get('ValidateCertificate')

	def set_ValidateCertificate(self,ValidateCertificate):
		self.add_query_param('ValidateCertificate',ValidateCertificate)

	def get_EcsInstanceId(self):
		return self.get_query_params().get('EcsInstanceId')

	def set_EcsInstanceId(self,EcsInstanceId):
		self.add_query_param('EcsInstanceId',EcsInstanceId)

	def get_InstanceNumber(self):
		return self.get_query_params().get('InstanceNumber')

	def set_InstanceNumber(self,InstanceNumber):
		self.add_query_param('InstanceNumber',InstanceNumber)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)