#include <iostream>
using namespace std;
class Car{
    public:
    string name;
    int average;

    Car(){    //---------->>>>>>  It is called Default Constructor.When we not create constructor,
                                 //Then it always present but didn't see.It is created because of we
    }                            //create s1 which is operated by constuctor and s2 which is operated by Default constructor.
                                 //Actually there is telling the computer that constructor for s1 & default constructor for s2.
                                 
                                 
                //  ----->>>>     We can create Multiple Constructor also.


    Car(string s,int i){         //Declaration of Constructor.
        name = s;                //Here name,average define without its datatype,It is Define already with Dataype one time.                        
        average = i;             //It already define within the class. 
    }
    Car(string w){               //It is also a Constructor , which take only name .
        name = w;                //It is only for the s3 Object.
    }
    Car(int a){                  //It is also a Constructor , which take only name .
        average = a;             //It is only for the s4 Object.
    }
};
class Truck{                     //It is also a kind of Class/Userdefined Datatype.
    public:
    string name,color;
    int average,seat;
    float rpm;

    Truck(string c,string y,int z,int k ,float l){       //It is constructor of class Truck.
        name = c;
        color = y;
        average = z;
        seat = k;
        rpm = l;
    }
    Truck(){           //It is Default Constructor.Used for Traditionally Initializing Method.

    }
    Truck(string c,int z,float l){
        name = c;
        average = z;
        rpm = l;
    }

};
void funprint(string d,int g){
    cout<<"Name - "<<d<<" and "<<"Average - "<<g<<endl<<endl;
}

void funtruck(string c ,string d,int a, int b ,float s){
    cout<<"Name - "<<c<<" and "<<"Average - "<<a<<" and "<<"Color - "<<d<<" and "<<"Seat - "<<b<<" and "<<"RPM - "<<s<<endl<<endl;
}
int main(){
    Car s1("Fortuner",3400);     //It is called at time of Declaration of an object , only  need to pass the parameter.
    cout<<"\n\n";
    funprint("Fortuner",3400);

    Car s2;
    s2.name = "lamborghini";     //It is tradition way to declare an object so for running this ,
    s2.average = 7900;           //so create Default constructor so computer doesn't get confused.
    funprint(s2.name,s2.average);

    Car s3("MiniCooper");        //In which One is for constructor which only taken name. 
    s3.average = 30000;          //One is for traditionally way.
    funprint(s3.name,s3.average);

    Car s4(7000);
    s4.name = "Mazretti";
    funprint(s4.name,s4.average);

    Truck t1;
    t1.name = "EnglishTruck";
    t1.color = "Black";
    t1.average = 400;
    t1.seat = 2;
    t1.rpm = 343.47;
    funtruck(t1.name,t1.color,t1.average,t1.seat,t1.rpm);


    Truck t2("DesiTruck",5000,234.45);
    t2.color = "Black";
    t2.seat = 4;
    funtruck(t2.name,t2.color,t2.average,t2.seat,t2.rpm);

    //    ----------->>>>>>     Under Below , Both are type of Copy Constructor of Different ways.      

    Truck t3 = t2;                   //It is also method of initializing of obj. value.
    t3.name = "MarathiTruck";           
    funtruck(t3.name,t3.color,t3.average,t3.seat,t3.rpm);

    Truck t4(t1);                   //By passing t1,all values like name,
                                    //Color of t1 are passed as an argument for its specific constructor.
    funtruck(t4.name,t4.color,t4.average,t4.seat,t4.rpm);


    return 0;
}






























