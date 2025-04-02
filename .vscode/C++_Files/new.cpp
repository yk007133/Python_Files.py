#include<iostream>
using namespace std;
class Yash{
    public:
    string name;
    int income;
    void display(){
        cout<<name<<"  "<<income<<endl;
    }
};
int main(){
    cout<<"Hello World"<<endl;
    Yash y1;
    y1.name = "Yash Khandelwal";
    y1.income = 100000;
    y1.display();
    return 0;
}



