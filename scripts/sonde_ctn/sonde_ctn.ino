// Mesure de la tension aux bornes d'une résistance CTN
const int sonde=A0;  // Branchement de la sonde
unsigned long deltat = 1000;            // Intervalle de temps entre deux mesures en ms
unsigned long myTime; // Temps de la dernière mesure

int U;            // Tension CTN
unsigned long t_inst;        // Temps depuis la dernière mesure


void setup() {
   Serial.begin(115200);  // Paramétrage du port série
   t_inst = 0; //
   myTime = millis();
}

void loop() {
  t_inst = millis() - myTime;
  while(t_inst < deltat){t_inst = millis() - myTime;}
  U = analogRead(sonde);      // Lecture tension en V
  myTime = millis();
  Serial.print(t_inst);
  Serial.print(",");
  Serial.println(U);
}
