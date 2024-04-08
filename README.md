# TFG
# Guillermo Carrasco
El siguiente repositorio recoge el firmware propio de un cliente y servidor del protocolo Bluetooth Low Energy para un SoC ESP32 y la herramienta BLERECON diseñada para el TFG de Ingeniería de Software de la U-Tad.

El firmware para estos dispositivos está programado en Arduino y emplea su propio lenguaje con extensión .ino. El firmware incluido ofrece una configuración de un servidor que anuncia un servicio con características propias, y un cliente que escanea dispositivos buscando este servicio para establecer una conexión.

La herramienta está programada usando Python 3.10.10, está compuesta por un código principal ble.py, y unas librerías que ofrecen diferentes funciones. El objetivo es ofrecer una herramienta de filtrado de información de paquetes del protocolo Bluetooth Low Energy. La herramienta filtra toda la información del paquete mostrando los datos más relevantes para cada tipo de paquete.

El funcionamiento de la herramienta es simple, se debe ejecutar el archivo ble.py en el mismo directorio que las librerías y se deberá agregar un documento de texto .txt que contenga el volcado de un paquete capturado de Bluetooth Low Energy. Se van a adjuntar una serie de paquetes de prueba en caso de que no se tenga acceso a un laboratorio que permita la captura de paquetes.

Ejemplo de uso: python ble.py paquete.txt
