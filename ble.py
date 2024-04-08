import sys
import os
import re
import time
from connInd import extract_connect_ind_info
from feature import extract_ll_feature_req_info
from length import extract_ll_length_req_info
from rcvd import extract_rcvd_info
from sent import extract_sent_info
from scan import extract_scan_info
from version import extract_ll_version_req_info
from adv import extract_adv_info

#leer el fichero pasado por argumento
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("El archivo especificado no fue encontrado")
        sys.exit(1)

#extraccion datos capa fisica
def extract_common_info(content):
    try:
        length_of_payload = re.search(r'Length of payload: (\d+)', content).group(1)
        channel_index = re.search(r'Channel Index: (\d+)', content).group(1)
        rssi = re.search(r'RSSI: (-?\d+) dBm', content).group(1)
        crc = re.search(r'CRC: (0x[0-9a-fA-F]+)', content).group(1)

        print("-------------------------------------------")
        print("Información capa física:\n")
        print(f"Longitud del payload: {length_of_payload}")
        print(f"Canal de transmisión: {channel_index}")
        print(f"RSSI: {rssi} dBm (intensidad de señal)")
        print(f"CRC: {crc}")
        print("-------------------------------------------")

    except AttributeError as e:
        print(f"Error al extraer información de la capa de enlace: {e}")


#buscar y mostrar el tipo de PDU
def read_pdu_type(file_path):
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no fue encontrado")
        return None

    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("El archivo especificado no fue encontrado")
        return None

    pdu_type_pattern = r'PDU Type: (\w+)'
    opcode_pattern = r'Opcode: (.+?)\s*\('

    pdu_type_match = re.search(pdu_type_pattern, content)
    if pdu_type_match:
        pdu_type = pdu_type_match.group(1)
        return pdu_type

    opcode_match = re.search(opcode_pattern, content)
    if opcode_match:
        opcode = opcode_match.group(1)
        return opcode

    return None


#funcion principal
def main():
    #verificar si hay argumento
    if len(sys.argv) != 2:
        print("Por favor, proporcione el nombre del archivo como argumento...")
        sys.exit(1)

    file_path = sys.argv[1]

    #leer fichero
    content = read_file(file_path)

    #obtener tipo de PDU
    pdu_type = read_pdu_type(file_path)

    #print("\nPDU Type: " + pdu_type)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    print("------HERRAMIENTA DE ANÁLISIS DE PAQUETES BLE------")
    print("---------------------------------------------------")
    print("------------------BLERECON-------------------------")
    print("---------------------------------------------------")
    print("\nEsta herramienta esta diseñada para el filtrado de paquetes BLE.\nEl código espera recibir un documento de texto por argumento para analizarlo.\nExisten distintas opciones de filtrado en función del tipo de paquete...")
    #menu de inicio

    print("\nPDU Type: " + pdu_type)
    while True:
        print("\nMenú:")
        print("1. Información capa física o PHY Layer ")
        print("2. Información de la capa de enlace o Link Layer LE")
        print("3. Información de los protocolos L2CAP y ATT")
        print("4. Salir")

        opcion = input("")
        #opcion 1 leer la info comun a todos
        if opcion== "1":
            print("\nLeyendo...\n")
            time.sleep(0.5)
            extract_common_info(content)
        #en funcion del tipo de paquete
        elif opcion == "2":
            if pdu_type == 'CONNECT_IND':
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_connect_ind_info(content)
            elif pdu_type in ['LL_FEATURE_REQ', 'LL_FEATURE_RSP']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_ll_feature_req_info(content)
            elif pdu_type in ['LL_LENGTH_REQ', 'LL_LENGTH_RSP']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_ll_length_req_info(content)
            elif pdu_type == 'Read By Group Type Response':
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_rcvd_info(content, opcion)
            elif pdu_type == 'Write Request':
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_sent_info(content, opcion)
            elif pdu_type in ['SCAN_REQ', 'SCAN_RSP']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_scan_info(content, pdu_type)
            elif pdu_type == 'LL_VERSION_IND':
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_ll_version_req_info(content)
            elif pdu_type in ['ADV_IND', 'ADV_NONCONN_IND']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_adv_info(content,pdu_type)
            else:
                print("¡Tipo de PDU no reconocido!")
                sys.exit(1)
         #para los paquetes con protocolo ATT y L2CAP   
        elif opcion == "3":
            if pdu_type in ['Read By Group Type Response', 'Write Response']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_rcvd_info(content, opcion)
            elif pdu_type in ['Read By Group Type Request' , 'Write Request']:
                print("\nLeyendo...\n")
                time.sleep(0.5)
                extract_sent_info(content, opcion)
            else:
                print("Este paquete no tiene esa informacion...")

        elif opcion == "4":
            break

if __name__ == "__main__":
    main()
