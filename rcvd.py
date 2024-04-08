import re

def extract_rcvd_info(content, menu):
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
            uuids = re.findall(r'UUID: (.+?)\s*\)', content)

            unique_uuids = set(uuids)
            for uuid in uuids:
                match = re.search(r'(\(0x[0-9a-fA-F]+\))', uuid)  # Ajuste aquí
                if match:
                    unique_uuids.add(uuid[:match.start() + len(match.group())])
            
            print("-------------------------------------------")
            print("Información de los protocolos L2CAP y ATT")
            print(f"L2CAP -> CID: {cid}")
            print(f"ATT -> Opcode: {opcode}")
            print("ATT -> UUIDs:")
            for uuid in unique_uuids:
                print(f"  - {uuid}")
            print("-------------------------------------------")

        except AttributeError as e:
            print("No se pudo encontrar la información para la opción 3.")
    
    else:
        print("Opción no válida.")
