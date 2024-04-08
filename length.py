import re

def extract_ll_length_req_info(content):
    try:
        access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
        master_address = re.search(r'Master Address: ([\w:]+)', content).group(1)
        slave_address = re.search(r'Slave Address: ([\w:]+)', content).group(1)
        llid = re.search(r'LLID: (\w+)', content).group(1)
        control_opcode = re.search(r'Control Opcode: ([\w\s]+) \(0x(\w+)\)', content).group(2)
        max_rx_octets = re.search(r'Max RX octets: (\d+)', content).group(1)
        max_rx_time = re.search(r'Max RX time: (\d+) microseconds', content).group(1)
        max_tx_octets = re.search(r'Max TX octets: (\d+)', content).group(1)
        max_tx_time = re.search(r'Max TX time: (\d+) microseconds', content).group(1)
        
        print("-------------------------------------------")
        print("Información de la capa de enlace o Link Layer LE")
        print(f"Access Address: {access_address}")
        print(f"Master Address: {master_address}")
        print(f"Slave Address: {slave_address}")
        print(f"LLID: {llid}")
        print(f"Control Opcode: {control_opcode}")
        print(f"Max RX octetos: {max_rx_octets}")
        print(f"Max RX time: {max_rx_time} microsegundos")
        print(f"Max TX octetos: {max_tx_octets}")
        print(f"Max TX time: {max_tx_time} microsegundos")
        print("-------------------------------------------")

    except AttributeError as e:
        print(f"No se pudo encontrar la información adicional para el paquete LL_LENGTH_REQ.")
