


int soundDetectedPin = 0;
int LEDDetectedPin = 13;
int soundDetectedVal = 0;
int buttomDetectedPin = 2;
int echoDetectedPin = 6;
int trigDetectedPin = 7;
int led = 0;
int estate = 0;
int modo = 0;
int alerta = 0;
unsigned int tiempo, distancia;

void setup ()
{
  Serial.begin(9600);  
  pinMode (soundDetectedPin, INPUT) ; // input from the Sound Detection Module
  pinMode (buttomDetectedPin, INPUT) ;
  pinMode (echoDetectedPin, INPUT) ;
  pinMode (trigDetectedPin, OUTPUT) ;
  pinMode (LEDDetectedPin, OUTPUT) ;
}
void loop ()
{
  soundDetectedVal = analogRead (soundDetectedPin) ; // read the sound alarm time
  estate = digitalRead (buttomDetectedPin) ;
  if(estate == 1)
  {
    delay(1000);
    if (modo == 0)
    {
      modo = 1;
    }else
    {
      modo = 0;
    }
  }
  if (modo == 1)
  {
    led = 0;
    digitalWrite(trigDetectedPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigDetectedPin, HIGH);
    // EL PULSO DURA AL MENOS 10 uS EN ESTADO ALTO
    delayMicroseconds(10);
    digitalWrite(trigDetectedPin, LOW);
 
    // MEDIR EL TIEMPO EN ESTADO ALTO DEL PIN "ECHO" EL PULSO ES PROPORCIONAL A LA DISTANCIA MEDIDA
    tiempo = pulseIn(echoDetectedPin, HIGH);
 
    // LA VELOCIDAD DEL SONIDO ES DE 340 M/S O 29 MICROSEGUNDOS POR CENTIMETRO
    // DIVIDIMOS EL TIEMPO DEL PULSO ENTRE 58, TIEMPO QUE TARDA RECORRER IDA Y VUELTA UN CENTIMETRO LA ONDA SONORA
    distancia = tiempo / 58;
 
    // ENVIAR EL RESULTADO AL MONITOR SERIAL
    delay(200);
 
    // ENCENDER EL LED CUANDO SE CUMPLA CON CIERTA DISTANCIA
    if (distancia <= 15) {
      digitalWrite(13, LOW);
      alerta = 1;
    } 
    if (alerta == 0 )
    {
      digitalWrite(13, HIGH);
    }else
    {
      digitalWrite(13, LOW);
      Serial.print(led);
      Serial.println(alerta);
      delay(2000);
      alerta = 0;
    }
  }else
  {
    alerta = 0;
    if (soundDetectedVal == 1023)
    {
      if (led == 1 )
      {
        digitalWrite(13, LOW);
        led = 0;
        delay(100);
        Serial.print(led) ;
        Serial.println(alerta);
      }
      else
      {
        digitalWrite(13, HIGH);
        led = 1;
        delay(100);
        Serial.print(led) ;
        Serial.println(alerta);
      }
    }
    delay(10);
  }
   
  }
