// Mesure de la tension aux bornes d'une résistance CTN
const int sonde=A0;  // PIN de branchement de la sonde
unsigned long deltat = 10;            // Intervalle de temps entre deux mesures en ms
unsigned long myTime; // Temps de la dernière mesure

int U;            // Tension CTN (R1 plus précisément)
unsigned long t_inst;        // Temps depuis la dernière mesure


void setup() { // Initialisation de la carte
   Serial.begin(115200);  // Paramétrage du port série
   t_inst = 0;
   myTime = millis();
}

void loop() {  //Actions réalisées en boucle
  t_inst = millis() - myTime;
  while(t_inst < deltat){t_inst = millis() - myTime;}  // Attente d'un intervalle de temps de 1s
  U = analogRead(sonde);      // Lecture tension en V
  myTime = millis();  //On réinitialise le temps de mesure
  Serial.print(t_inst);  // On envoie le temps entre deux mesures et non le temps de mesure
  Serial.print(",");
  Serial.println(U);  // On envoie la tension
}
