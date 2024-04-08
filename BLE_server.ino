#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
//definir UUID
#define SERVICE_UUID        "620A05F8-2287-40B8-98A8-50B53AFCF37B"
#define CHARACTERISTIC_UUID "24D7D47A-6883-48BE-BB2D-74DDBB479177"
//crear SERVICIO Y CARACTERISTICA
void setup() {
  Serial.begin(115200);
  Serial.println("CREANDO SERVIDOR BLE...");
  BLEDevice::init("ble_Server");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );
  //definir valor caracterítica
  pCharacteristic->setValue("Hola desde BLE! este es el valor");
  //comenzar el servicio + configuración
  pService->start();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(true);
  pAdvertising->setMinPreferred(0x06);
  pAdvertising->setMinPreferred(0x12);
  BLEDevice::startAdvertising();
  Serial.println("SERVIDOR ANUNCIANDOSE...");
}
void loop() {
  delay(2000);
}