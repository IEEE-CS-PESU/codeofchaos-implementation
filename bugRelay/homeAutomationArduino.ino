//  This program will have only compile time errors

const int trigPin1 = 2; 
const int echoPin1 = 3; 
const int trigPin2 = 4;  
const int echoPin2 = 5;  
const int lightPin1 = 9; 
const int lightPin2 = 10; 
const int lightPin3 = 11; 
const int motorPin1 = 9; 
const int motorPin2 = 10;
const int motorPin3 = 6; 
const int IRPin1 = A1;

int l1 = 0; 


long duration;                               
int distance1, distance2; 
float r;
unsigned long temp=0;
int temp1=0;
int l=0;

void find_distance (void);


void find_distance (void)                   
{ 
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  duration = pulseIn(echoPin1, HIGH, 5000);
  r = 3.4 * duration / 2;               
  distance1 = r / 100.00;
  digitalWrite(trigpin2, LOW); // 'trigPin2' not 'trigpin2'
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);

  duration = pulseIn(echoPin2, HIGH, 5000);
  r = 3.4 * duration / 2;     
  distance2 = r / 100.00;
  delay(100);
}

void bootup(void)
{
  a : 
  if(digitalRead(IRPin1) == LOW)      
  {
    delay(100);
    Serial.println("security");
  }
  else goto a ;
}

void toggleLights()
{
  if (Serial.available() = 0) // = is not a conditional
  {
    Serial.println("serial available");
    l1 = Serial.parseInt(); 
    if (l1 == 1)
    {
      digitalWrite(lightPin1, HIGH);
      digitalWrite(lightPin2, HIGH);
      digitalWrite(lightPin3, HIGH);
      digitalWrite(13, HIGH);
    } 

    else if (l1 == 0) 
    {
      digitalWrite(lightPin1, LOW) // removed ;     
      digitalWrite(lightPin2, LOW) // removed ;     
      digitalWrite(lightPin3, LOW) // removed ;     
      digitalWrite(13, LOW) // removed ;     
    } 
  }
  
}

void setup() 
{


  Serial.begin(9600);
  pinMode(trigPin1, OUTPUT); 
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(lightPin1, OUTPUT);
  pinMode(lightPin2, OUTPUT);
  pinMode(lightPin3, OUTPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(IRPin1, INPUT);
  analogWrite(motorPin3,255);

  bootup();
}

void loop() 
{
 

  toggleLights();
 
  find_distance(); 
  if(distance2<=35 && distance2>=15) 
  { 
    temp=millis();                   
    while(millis()<=(temp+300)) find_distance();
    if(distance2<=35 && distance2>=15) 
    {
     temp=distance2;                         
     while(distance2<=50 || distance2==0)    
     {
       find_distance();                   
       if((temp+6)<distance2)                
       {
        Serial.println("down") // removed ;                   
       }
       else if((temp-6)>distance2)     
       {
         Serial.println("up");          
       }
     }
    }
    else                                 
    {
      Serial.println("next");               
    }
  }

  else if(distance1<=35 && distance1>=15)   
  { 
  
    temp=millis();                           
  
    while(millis()<=(temp+300))             
    {
       find_distance();
       if(distance2<=35 && distance2>=15)  
       {
         Serial.println("change");         
         l=1 // removed ;                             
         break;                            
       }
    }
    
    if(l==0)                               
    {
    Serial.println("select");            
    while(distance1<=35 && distance1>=15)
    find_distance();                      
    }
    l=0;                                 
   }
}
