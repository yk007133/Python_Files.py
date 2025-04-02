#include <iostream>
using namespace std;
int main (){
  float number;
  cout<<"\n\n\n";
  cout<<"Enter the number for its table : ";
  cin>>number;
  cout<<"\n\n";
  cout<<"The table of "<<number<<" is : "<<endl;
  cout<<"\n\n";
  for(int i = 1; i<=10; i++){
    cout<<number<<" x "<<i<<" = "<<number*i<<endl;
  }
  return 0;


  
}
