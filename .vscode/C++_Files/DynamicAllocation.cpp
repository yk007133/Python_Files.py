#include <iostream>
using namespace std;
class Cricketer{
    public:
    string name;
    int runs;
    float average;
    Cricketer(string name,int runs,float average){
        this->name = name;
        this->runs = runs;
        this->average = average;
    }
};
int main(){
    Cricketer c1("Rohit Sharma",18000,47.8);  
    Cricketer* c = &c1;      //It is a Simple way to use Object Pointer.A extra variable is also
    cout<<c->name<<endl;   //created to stored the address of the any variable.


    Cricketer* d = new Cricketer("Virat Kohli",50000,58.7);//It is way to perform Dynamic Allocation.
    cout<<d->name<<endl;     //It is Dynamic Allocation way to use Object Pointer.No need to create 
                             //extra variable to stored the address of any variable.Like an example,
    
    // ----->>>>> Instead of this :-
    
    int a =5;
    int* b = &a;     //Because in which a new variable is also create, so take storage in RAM.
    cout<<*b<<endl;   
 
    //------>>>>> Use this, which is called Dynamic Allocation.

    int* h = new int(6);  //Basically c stores address of 6 in new syntax code.
                          //Here 6 is stored in a virtual variable that has no existence.
    cout<<*h<<endl;       //So, no need to create new variable to store address.
                          //Which results that there is extra space in the RAM.
    
    return 0;                
}















































