/*
 *  This sketch run on NodeMCU (ESP8266),
 *  demonstrates how to set up a simple HTTP-like server.
 *  The server will set a GPIO pins depending on the request,
 *  to control the brightness of RGB LED connected to:
 *    D0 : BLUE
 *    D1 : GREEN
 *    D2 : RED
 *    
 *    http://server_ip/rgb/rrggbb/
 *    where rr is the value set RED
 *    where gg is the value set GREEN
 *    where bb is the value set BLUE
 *    then terminate with '/'
 *  server_ip is the IP address of the NodeMCU, will be 
 *  printed to Serial when the module is connected.
 */

#include <ESP8266WiFi.h>

const char* ssid = "SSID";
const char* password = "password";

int ledB = D0;
int ledG = D1;
int ledR = D2;

// Create an instance of the server
// specify the port to listen on as an argument
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  delay(10);

  // prepare GPIOs for RGB LED
 
  
  
  // Connect to WiFi network

  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
   
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
  
  // Read the first line of the request
  String req = client.readStringUntil('\r');
  Serial.println(req);
  client.flush();
  
  // Match the request
  int valX, valY,indexX,indexY;
  String subStringX, subStringY;
  indexX=req.indexOf("/x");
  indexY=req.indexOf("/y");
  if(indexX!= -1 &&  indexY!=-1 ){
    if(req.charAt(indexX+6)=='/'){
      subStringX = req.substring(indexX+2);
      subStringY = req.substring(indexY+2);
      valX = subStringX.toInt();
      valY = subStringY.toInt();
      switch (valX+ 3*valY){
        case 4: /*x=1  y=1    ambos negativos*/  break;
        case 5: /*x=2  y=1    x quieto    y negativo*/  break;
        case 6: /*x=3  y=1    x positivo  y negativo*/  break;
        case 7: /*x=1  y=2    x negativos y quieto*/  break;
        case 8: /*x=2  y=2    x quieto    y quieto*/  break;
        case 9: /*x=3  y=2    x positivo  y quieto*/  break;
        case 10: /*x=1  y=3   x negativos y positivo*/  break;
        case 11: /*x=2  y=3   x quieto    y positivo*/  break;
        case 12: /*x=3  y=3   x positivo  y positivo*/  break;
        
        }
      Serial.println("valX: " + String(valX));
      Serial.println("valY: " + String(valY));    
    }
    else{
      Serial.println("Not terminated with /");
      client.stop();
      return;
    }
  }
  else {
    Serial.println("No /x and /y found");
    client.stop();
    return;
  }

  // Set GPIOs according to the request
  // No check valid of the requested setting 
  
  client.flush();

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html";  

  // Send the response to the client
  client.print(s);
  delay(1);
  Serial.println("Client disonnected");

  // The client will actually be disconnected 
  // when the function returns and 'client' object is detroyed
}
