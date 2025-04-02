#include <iostream>
using namespace std;
class Cricketer{
    public:
    string name;                  //Where name,runs and average are the attributes of class.
    int runs;
    float average;
    Cricketer(string name,int runs,float average){
        this->name = name;                           //Using "this" keyword to avoid complexity
        this->runs = runs;                           //for the Computer.
        this->average = average;
    }
    void print(int a){                               //Declaration of Function within the class, So no need to pass parameter of attributes
        cout<<name<<" "<<runs<<" "<<average<<endl;   //of class Cricketer.You may pass another parameter rather than attributes of class.
        cout<<a;                                     //Inside the Function.Also, We can achieve attributes without obj Declaration.
    }                                                //Because obj only Declare in the int main.cpp not with the class Declaration.
};
int main(){
    Cricketer c1("Virat Kohli",25000,55.3);
    Cricketer c2("Rohit Sharma",18000,47.8);

    c1.name = "Sachin Tendulkar";         //Updating the Data.

    c1.print(16);              //When we Declare Function within the class then, It is a way to
    c2.print(20);              //call the function, Remember it ! .

    return 0;
}





























