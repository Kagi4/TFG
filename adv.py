import re

def extract_adv_info(content, packet_type):
    try:
        if packet_type == "ADV_IND":
            access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
            pdu_type = re.findall(r'PDU Type: (\w+)', content)
            tx_add = "Random" if "Tx Address: Random" in content else "Public"
            chsel = re.search(r'Channel Selection Algorithm: (.+)', content).group(1)
            advertising_address = re.search(r'Advertising Address: ([\w:]+)', content).group(1)
            cust_uuid = re.search(r'Custom UUID: (.+?)\s*\)', content).group(1)
            crc = re.search(r'CRC: (0x[0-9a-fA-F]+)', content).group(1)

            print("-------------------------------------------")
            print("Información capa de enlace o Lin Layer LE:\n")
            print(f"Access Address: {access_address}")
            print(f"PDU Type: {pdu_type}")
            print(f"TxAdd: {tx_add}")
            print(f"Advertising Address: {advertising_address}")
            print(f"Seleccion de algortimo para el salto de canal: #{chsel}")
            print(f"Personalizado UUID de 128 bits: {cust_uuid}")
            print(f"CRC: {crc}")
            print("-------------------------------------------")


        elif packet_type == "ADV_NONCONN_IND":
            access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
            pdu_type = re.findall(r'PDU Type: (\w+)', content)
            tx_add = "Random" if "Tx Address: Random" in content else "Public"
            advertising_address = re.search(r'Advertising Address: ([\w:]+)', content).group(1)
            company = re.search(r'Company ID: (\w+)', content).group(1)
            data = re.search(r'Data: (\w+)', content).group(1)
            
            print("-------------------------------------------")
            print("Información capa de enlace o Lin Layer LE:\n")
            print(f"Access Address: {access_address}")
            print(f"PDU Type: {pdu_type}")
            print(f"TxAdd: {tx_add}")
            print(f"Advertising Address: {advertising_address}")
            print(f"Compañia: {company}")
            print(f"Datos cifrados: {data}")
            print("-------------------------------------------")

    except AttributeError as e:
        print(f"No se pudo encontrar la información adicional para el paquete {packet_type}.")
 