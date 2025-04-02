#include <iostream>
using namespace std;
class Yash{
    public:                   
    string name;                      //This is an Arguments.
    int age;
    Yash(string name,int age){        //When this kind situation comes when argument's and attribute's name are got same 
                                      //then use "this" keyword which relate the correct thing to correct thing.
        this->name = name;            //And Avoid Complexity for the Computer.
        this->age = age;
    }   
};
void function(Yash f){
        cout<<f.name<<" "<<f.age<<endl;
    }
int main(){
    Yash y1("Dhruv",20);
    function(y1);
    return 0;
}


































