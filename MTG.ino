#include <WiFi.h>
#include <HTTPClient.h>

// WiFi Configuration
const char* ssid = "Pondok Putra";
const char* password = "11223344";

// Sensor configuration
const int sensorPin = 35;
const String sensorName = "Asapmaksum";

// RestAPI Configuration
const char* baseRoute = "http://192.168.1.225:5000/sensor/";
const int requestDelay = 1000;

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi network");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(requestDelay);
  int gas = analogRead(sensorPin);

  Serial.println(analogRead(sensorPin));

  if(WiFi.status()== WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;

    http.begin(client, baseRoute+sensorName);
    int statusCode = http.POST(String(gas));

    http.end();
  }else{
    Serial.println("WiFi Disconnected");
  }
}