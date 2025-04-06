#include<iostream>
using namespace std;
class A{
    public:
    int a;
    float b;
    string c;

    A(int a , float b , string c){
        this->a = a;
        this->b = b;
        this->c = c;   
    }
    void display(){
        cout<<a<<endl;
        cout<<b<<endl;
        cout<<c<<endl;
    }  
};
int main(){
    A obj1(1 , 2.5, "YashKhandelwal");
    obj1.display();
    return 0;
}
