
//------->>>>>> ### Important ###
//Firstly , please understand access modifier in AccessModifier.cpp file, then come on this.
//Otherwise go gonna waste your time because without that you can understand it.


#include <iostream>
using namespace std;
class Vehicle{
    public:
        string name;
        float millege;
        bool bootspace;
        int price;
        Vehicle(string name,float millege,bool bootspace, int price,int numberplate){
            this->name = name;
            this->millege = millege;               //With the help of Constructor, we can change 
            this->price = price;                   //and print the private variable.
            this->bootspace = bootspace;           //But not with the Default Constructor.
            this->numberplate = numberplate;
            this->numberplate = 10001;
            cout<<this->numberplate<<endl;
        }
        Vehicle(){

        }

        void setter(int n){                //With the help of setter, we can set the numberplate.
            this->numberplate = n;         //In place setter, you can write any name of function.
        }                                  //It is only defined in public section in the class.

    

        void getter(){                     //With the help of getter, we can print the numberplate.
            cout<<this->numberplate<<endl; //In place getter, you can write any name of function.
        }                                  //It is only defined in public section in the class.

        

    private:
        int numberplate;

};

int main (){
    Vehicle v2("RangeOver Velor",45.67,true,18000000,50000);
    v2.setter(1);
    v2.getter();

    return 0;
}





