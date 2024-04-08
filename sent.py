import re

def extract_sent_info(content, menu):
    if menu == "2":
        try:
            access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
            master_address = re.search(r'Master Address: ([\w:]+)', content).group(1)
            slave_address = re.search(r'Slave Address: ([\w:]+)', content).group(1)
            llid = re.search(r'LLID: (.+)', content).group(1)

            print("-------------------------------------------")
            print("Información de la capa de enlace o Link Layer LE")
            print(f"Access Address: {access_address}")
            print(f"Master Address: {master_address}")
            print(f"Slave Address: {slave_address}")
            print(f"LLID: {llid}")
            print("-------------------------------------------")

        except AttributeError as e:
            print("No se pudo encontrar la información para la opción 2.")

    elif menu == "3":
        try:
            cid = re.search(r'CID: (.+)', content).group(1)
            opcode = re.search(r'Opcode: (.+)', content).group(1)
            uuids = re.findall(r'UUID: (.+)', content)
            value_hex = re.search(r'Value: (.+)', content).group(1)
            value = re.search(r'Value: (.+)', content).group(1)
            service_uuid = re.search(r'Service UUID: (.+)', content).group(1)

            value_text = bytearray.fromhex(value).decode()
            unique_uuids = set(uuids)
            
            print("-------------------------------------------")
            print("Información de los protocolos L2CAP y ATT")
            print(f"L2CAP -> CID: {cid}")
            print(f"ATT -> Opcode: {opcode}")
            print(f"ATT -> Service UUID: {service_uuid}")
            print("ATT -> UUIDs:")
            for uuid in unique_uuids:
                print(f"  - {uuid}")
            print(f"Valor (hex): {value_hex}")
            print(f"Valor (texto): '{value_text}' ")
            print("-------------------------------------------")

        except AttributeError as e:
            print("No se pudo encontrar la información para la opción 3.")
    else:
        print("Opción no válida.")
