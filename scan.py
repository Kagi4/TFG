import re

def extract_scan_info(content, packet_type):
    try:
        if packet_type == "SCAN_REQ":
            scanning_address = re.search(r'Scanning Address: ([\w:]+)', content).group(1)
            access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
            pdu_type = re.search(r'PDU Type: (\w+)', content).group(1)
            tx_add = "Random" if "Tx Address: Random" in content else "Public"
            rx_add = "Random" if "Rx Address: Random" in content else "Public"
            advertising_address = re.search(r'Advertising Address: ([\w:]+)', content).group(1)
            crc = re.search(r'CRC: (0x[0-9a-fA-F]+)', content).group(1)

            print("-------------------------------------------")
            print("Información de la capa de enlace o Link Layer LE")
            print(f"Scanning Address: {scanning_address}")
            print(f"Access Address: {access_address}")
            print(f"PDU Type: {pdu_type}")
            print(f"TxAdd: {tx_add}")
            print(f"RxAdd: {rx_add}")
            print(f"Advertising Address: {advertising_address}")
            print(f"CRC: {crc}")
            print("-------------------------------------------")

        elif packet_type == "SCAN_RSP":
            advertising_address = re.search(r'Advertising Address: ([\w:]+)', content).group(1)
            scan_response_data = re.search(r'Scan Response Data: ([0-9a-fA-F]+)', content).group(1)
            crc = re.search(r'CRC: (0x[0-9a-fA-F]+)', content).group(1)

            print("-------------------------------------------")
            print("Información de la capa de enlace o Link Layer LE")
            print(f"Advertising Address: {advertising_address}")
            print(f"Scan Response Data: {scan_response_data}")
            print(f"CRC: {crc}")
            print("-------------------------------------------")

    except AttributeError as e:
        print(f"No se pudo encontrar la información adicional para el paquete {packet_type}.")
