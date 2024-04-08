#include "BLEDevice.h"

//definir UUID que nos interesan
static BLEUUID serviceUUID("620A05F8-2287-40B8-98A8-50B53AFCF37B");
static BLEUUID    charUUID("24D7D47A-6883-48BE-BB2D-74DDBB479177");
//variables de conexion y scaneo
static boolean doConnect = false;
static boolean connected = false;
static boolean doScan = false;
static BLERemoteCharacteristic* pRemoteCharacteristic;
static BLEAdvertisedDevice* myDevice;

//evento de conexion conectado y desconectado
class MyClientCallback : public BLEClientCallbacks {
  void onConnect(BLEClient* pclient) {
  } //no muestra nada
  void onDisconnect(BLEClient* pclient) {
    connected = false;
    Serial.println("DESCONECTADO"); //se muestra al desconectar
  }
};

//ESCANEO DE DISPSOITIVOS
class MyAdvertisedDeviceCallbacks: public BLEAdvertisedDeviceCallbacks {

  void onResult(BLEAdvertisedDevice advertisedDevice) {
    Serial.print("DISPOTIVO BLE DETECTADO: ");
    Serial.println(advertisedDevice.toString().c_str());
    //SE COMPRANA LOS UUID DEL SERVICIO
    if (advertisedDevice.haveServiceUUID() && advertisedDevice.isAdvertisingService(serviceUUID)) {
      //SE PARA EL ESCANEO SI COINCIDEN
      BLEDevice::getScan()->stop();
      myDevice = new BLEAdvertisedDevice(advertisedDevice);
      doConnect = true;
      doScan = true;

    } 
  } 
};

//ESTABELCER CONEXION CON EL SERVIDOR
bool connectToServer() {
    Serial.print(" EMPEZANDO UNA CONEXION CON EL DISPOSITIVO ->");
    Serial.println(myDevice->getAddress().toString().c_str());
    
    //crea cliente
    BLEClient*  pClient  = BLEDevice::createClient();
    Serial.println(" | CLIENTE CREADO |");
    pClient->setClientCallbacks(new MyClientCallback());

    //conexion cliente con servidor
    pClient->connect(myDevice); 
    Serial.println(" | CONECTADO AL SERVIDOR |");
    pClient->setMTU(517); 
  
    //COMPARAMOS EL UUID DEL SERVICIO AL QUE NOS HEMOS CONECTADO
    BLERemoteService* pRemoteService = pClient->getService(serviceUUID);
    if (pRemoteService == nullptr) {
      Serial.print("Buscando el UUID del servicio sin exito...");
      Serial.println(serviceUUID.toString().c_str());
      pClient->disconnect();
      return false;
    }
    Serial.println(" | SERVICIO ENCONTRADO |");


    //COMPARAMOS EL UUID DE LA CARACTERISTICA AL QUE NOS HEMOS CONECTADO
    pRemoteCharacteristic = pRemoteService->getCharacteristic(charUUID);
    if (pRemoteCharacteristic == nullptr) {
      Serial.print("Buscando el UUID de la característica sin exito...");
      Serial.println(charUUID.toString().c_str());
      pClient->disconnect();
      return false;
    }
    Serial.println(" | CARACTERISTICA ENCONTRADA |");

    //LEER VALOR DE LA CARACTERÍSTICA
    if(pRemoteCharacteristic->canRead()) {
      std::string value = pRemoteCharacteristic->readValue();
      Serial.print("VALOR DE LA CARACTERISTICA LEIDA --> ");
      Serial.println(value.c_str());
    }

    connected = true;
    return true;
}

void setup() {
  Serial.begin(115200);
  // SE INICIA EL CLIENTE
  Serial.println("CREANDO CLIENTE BLE...");
  BLEDevice::init("ble_Client");

  //establecemos el escaneo durante 5 segundos
  BLEScan* pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setInterval(1349);
  pBLEScan->setWindow(449);
  pBLEScan->setActiveScan(true);
  pBLEScan->start(5, false);
} 
void loop() {

  // SI LA CONEXIÓN ES CORRECTA COMIENZA EL INTERCAMBIO DE DATOS
  if (doConnect == true) {
    if (connectToServer()) {
      Serial.println("COMENZANDO ENVIO Y RECEPCIÓN DE DATOS");
    } else {
      Serial.println("FALLO DE CONEXION...");
    }
    doConnect = false;
  }

  //ESTABLECEMOS EL NUEVO VALOR PARA LA CARACTERISTICA
  if (connected) {
    String newValue = String(millis()/1000) + " segundos";
    Serial.println("NUEVO VALOR CARACTERÍSTICA: \"" + newValue + "\"");

    pRemoteCharacteristic->writeValue(newValue.c_str(), newValue.length());
  //SI NO CONECTA ESCANEAMOS DE NUEVO
  }else if(doScan){
    BLEDevice::getScan()->start(0); 
  }
  
  delay(1000); 
} 
