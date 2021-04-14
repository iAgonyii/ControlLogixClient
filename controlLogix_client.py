# Roy Teneij
from pycomm3 import LogixDriver, CIPDriver, Services

def getPlc():
	with LogixDriver('10.0.111.5') as plc:
		return(plc)
def getPlcInfo():
	with LogixDriver('10.0.111.5') as plc:
		return(plc.info)

def getTags():
	with LogixDriver('10.0.111.5') as plc:
		return plc.get_tag_list()

def readTag(tagName):
	with LogixDriver('10.0.111.5') as plc:
		return plc.read(tagName)

def readTagInfo(tagName):
	with LogixDriver('10.0.111.5') as plc:
		return plc.get_tag_info(tagName)

def writeTag(tagName, value):
	with LogixDriver('10.0.111.5') as plc:
		return plc.write((tagName, value))

def writeSimulationTag(bool):
	with LogixDriver('10.0.111.5') as plc:
		data = {'tag_name': 'System_In_Simulation', 'dim': 0, 'instance_id': 448, 'symbol_address': 1879793412, 'symbol_object_address': 1947314424, 'software_control': 1140916492, 'alias': bool, 'external_access': 'Read/Write', 'dimensions': [0, 0, 0], 'tag_type': 'atomic', 'data_type': 'BOOL', 'data_type_name': 'BOOL', 'bit_position': 0}
		return plc.write(('System_In_Simulation', data))

def getIPConfig():
    message_path = '10.0.111.5'

    with CIPDriver(message_path) as plc:  # L85
        data = plc.generic_message(
            service=b'\x0e',
            class_code=b'\xf5',
            instance=1,
            attribute=3,
            connected=False,
            unconnected_send=True,
            route_path=True,
            name='IP_config'
        )

        statuses = {
            0b_0000: 'static',
            0b_0001: 'BOOTP',
            0b_0010: 'DHCP'
        }
        print(data.value)
       #ip_status = data.value & 0b_1111  # only need the first 4 bits
       # print(statuses.get(ip_status, 'unknown'))

def stopPlc():
	with CIPDriver('10.0.111.5') as plc:
		data = plc.generic_message(
			service=b'\x07',
			class_code=b'\x24',
			instance=1,
			connected=False,
			unconnected_send=True,
			route_path=True,
			name='STOP_plc' 
		)
		print(data.value)
