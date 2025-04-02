#include <iostream>
using namespace std;

class Car{
    public:
    int model;
    string name;
    int seater;
};

void funcar(Car& c){         //Call by Refrence.
    c.model = 2016;
    c.name = "Fortuner";
    c.seater = 8;  
}

int main(){
    Car abc;
    abc.model = 2017;
    abc.name = "Honda City";
    abc.seater = 5;

    cout<<abc.model<<" "<<abc.name<<" "<<abc.seater<<endl;
    funcar(abc);
    cout<<abc.model<<" "<<abc.name<<" "<<abc.seater<<endl;   //Different Output due to reference of variable of main.cpp in the function.

    return 0;
}













