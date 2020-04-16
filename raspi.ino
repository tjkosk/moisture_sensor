const int AirValue = 658;   //CALIBRATED WITH 5V USING THE BOTTOM END OF THE CLEAR TAPE
const int WaterValue = 357; //AS TOP WATER LEVEL
int soilMoistureValue = 0;
int soilmoisturepercent=0;
String dataString;

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
  pinMode(11,OUTPUT);

}
void loop() {
  if (Serial.available()>0){
    digitalWrite(11,LOW);
    delay(200);  
    soilMoistureValue = analogRead(3);  //put Sensor insert into soil
    //Serial.println(soilMoistureValue);
    soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
    dataString = String(soilmoisturepercent);
    Serial.println(dataString);
    digitalWrite(11,HIGH);
  }
   delay(200);
}
