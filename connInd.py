import re

def extract_connect_ind_info(content):
    try:
        access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
        pdu_type = re.search(r'PDU Type: (\w+)', content).group(1)
        ch_sel = re.search(r'Channel Selection Algorithm: #(\d+)', content).group(1)
        tx_add = "Random" if "Tx Address: Random" in content else "Public"
        rx_add = "Random" if "Rx Address: Random" in content else "Public"
        initiator_address = re.search(r'Initiator Address: ([\w:]+)', content).group(1)
        advertising_address = re.search(r'Advertising Address: ([\w:]+)', content).group(1)
        access_address_2 = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
        ch_map = re.search(r'Channel Map: ([0-9a-fA-F]+)', content).group(1)
        hop = re.search(r'Hop: (\d+)', content).group(1)
        crc = re.search(r'CRC: (0x[0-9a-fA-F]+)', content).group(1)
        
        print("-------------------------------------------")
        print("Información de la capa de enlace o Link Layer LE")
        print(f"Access Address: {access_address}")
        print(f"PDU Type: {pdu_type}")
        print(f"Seleccion de algortimo para el salto de canal: #{ch_sel}")
        print(f"Tx Address: {tx_add}")
        print(f"Rx Address: {rx_add}")
        print(f"Dirección del dispositivo que inicia: {initiator_address}")
        print(f"Advertising Address: {advertising_address}")
        print(f"Access Address 2: {access_address_2}")
        print(f"Mapa de canales: {ch_map}")
        print(f"Hop (incremento de salto entre canales): {hop}")
        print(f"CRC: {crc}")
        print("-------------------------------------------")

    except AttributeError as e:
        print(f"No se pudo encontrar la información adicional para el paquete CONNECT_IND.")
