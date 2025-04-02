#include<iostream>
using namespace std;
class Student{
    public:
    string name;
    int age;
    float income;
    string car;
};
int main(){
    Student s1;
    s1.name="Rohit Sharma";
    s1.age=37;
    s1.income=564534;
    s1.car="Lamborghini";
    cout<<s1.name<<" "<<s1.age<<" "<<s1.income<<" "<<s1.car<<endl<<endl;


    return 0;
}