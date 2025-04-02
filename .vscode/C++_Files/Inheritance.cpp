
//--------->>>>>>> What is Inheritance ?

// Inheritance in programming allows a new class to inherit properties and behaviors from an 
//existing class.This means the child class can use and extend functionalities of the parent class.

//------->>>>>> Types of Inheritance :-

// 1. Single Inheritance     : A class inherits from one parent class.
// 2. Multiple Inheritance   : A class inherits from more than one parent class.
// 3. Multilevel Inheritance : A class is derived from a parent class that is also derived
//                             from another parent class.

// All doubt are cleared after understand this example :-

//cpp

#include <iostream>
using namespace std;
class Cricketer{                               //It is a Parent Class.
    public:
    int runs;
    float average;
    int wickets;
};
class IPL : public Cricketer{                  //It is a Single Inheritance.
    public:
    string teamname;
    int tropies;
};
class Player : public IPL{                     //It is a Single Inheritance.But from Cricketer
    public:                                    //to player, It is a Multilevel Inheritance.
    string playername;
};
class Jadeja : public Cricketer,public IPL{    //It is a Multiple Inheritance.
    public:
    string category;
    void display(){
        cout<<runs<<" "<<average<<" "<<wickets<<" "<<teamname<<" "<<tropies<<endl;
    }
};

int main(){
    Jadeja j1;
    j1.runs = 1000;
    j1.average = 45.34;
    j1.wickets = 500;
    j1.teamname = "Chennai Superkings";
    j1.tropies  = 7;
    j1.display();

    return 0;
}




