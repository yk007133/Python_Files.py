#include <iostream>
using namespace std;
int main (){
  cout<<"Basic Calculator";
  cout<<"\n\n";
  cout<<"+ for Addition\n- for Substratction\n* for Multiplication\n/ for Division";
  cout<<"\n\n";
  float num1 , num2;
  cout<<"Enter the first Number : ";
  cin>>num1;
  cout<<"\n";
  cout<<"Enter the second Number : ";
  cin>>num2;
  cout<<"\n";
  char optr;
  cout<<"Enter the operator : ";
  cin>>optr;
  cout<<"\n";
  switch (optr){
    case '+' :
      cout<<"The sum of "<<num1<<" and "<<num2<<" is "<<num1+num2;
      break;
    case '-' :
      cout<<"The differnce of "<<num1<<" and "<<num2<<" is "<<num1-num2;
      break;
    case '*' :
      cout<<"The multiplication of "<<num1<<" and "<<num2<<" is "<<num1*num2;
      break;
    case '/' :
      if(num2!=0){
        cout<<"The division of "<<num1<<" and "<<num2<<" is "<<num1/num2;
      }
      else{
        cout<<"The division of "<<num1<<" and "<<num2<<" is not possible";
      }
      break;
    default :
      cout<<"Invalid operator";
  }
  return 0;
}















  
