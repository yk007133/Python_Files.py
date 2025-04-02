#include<iostream>
#include<string.h>
using namespace std;
int main(){
  string c,d;
  cout<<"Enter the your name : ";
  cin>>d;
  for(char& c : d){
    c = tolower(c);
    cout<<c;
  }
  return 0;
}



