
#include <Servo.h> // Incluimos la biblioteca Servo

Servo servo_1;   // Definimos los servos que vamos a utilizar
Servo servo_2;
Servo servo_3;   
Servo servo_4;

int potenciometro_1 = A0;  // Pin usado para conectar el potenciómetro
int valor_potenciometro_1;    // Esta variable definirá la posición del servo
int potenciometro_2 = A1;  
int valor_potenciometro_2;
int potenciometro_3 = A2; 
int valor_potenciometro_3;    
int potenciometro_4 = A3;  
int valor_potenciometro_4;


void setup() {
servo_1.attach(5); // Definimos los pines de señal para el servo
servo_2.attach(6); 
servo_3.attach(10); 
servo_4.attach(11); 
}

void loop() {
  
valor_potenciometro_1 = analogRead(potenciometro_1);
// leemos el valor del potenciometro (valor entre 0 y 1023)
valor_potenciometro_1 = map(valor_potenciometro_1, 0, 1023, 0, 180);
// valor proporcional a la escala del servomotor (valor entre 0 y 180)
servo_1.write(valor_potenciometro_1);
delay(10);
// Esperamos para reiniciar el bucle


valor_potenciometro_2 = analogRead(potenciometro_2);
valor_potenciometro_2 = map(valor_potenciometro_2, 0, 1023, 0, 180);
servo_2.write(valor_potenciometro_2);
delay(10);



valor_potenciometro_3 = analogRead(potenciometro_3);
valor_potenciometro_3 = map(valor_potenciometro_3, 0, 1023, 0, 180);
servo_3.write(valor_potenciometro_3);
delay(10);



valor_potenciometro_4 = analogRead(potenciometro_4);
valor_potenciometro_4 = map(valor_potenciometro_4, 0, 1023, 0, 180);
servo_4.write(valor_potenciometro_4);
delay(10);

}
