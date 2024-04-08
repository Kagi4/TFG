import re

def extract_ll_feature_req_info(content):
    try:
        access_address = re.search(r'Access Address: (0x[0-9a-fA-F]+)', content).group(1)
        master_address = re.search(r'Master Address: ([\w:]+)', content).group(1)
        slave_address = re.search(r'Slave Address: ([\w:]+)', content).group(1)
        llid = re.search(r'LLID: (\w+)', content).group(1)
        control_opcode = re.search(r'Control Opcode: ([\w\s]+) \(0x(\w+)\)', content).group(2)
        feature_set = re.search(r'Feature Set: (0x[0-9a-fA-F]+)', content).group(1)

        print("-------------------------------------------")
        print("Información de la capa de enlace o Link Layer LE")
        print(f"Access Address: {access_address}")
        print(f"Master Address: {master_address}")
        print(f"Slave Address: {slave_address}")
        print(f"LLID: {llid}")
        print(f"Control Opcode (tipo de operación): {control_opcode}")
        print(f"Set de caracterísitcas: {feature_set}")
        print("-------------------------------------------")

    except AttributeError as e:
        print(f"No se pudo encontrar la información adicional para el paquete LL_FEATURE_REQ.")
