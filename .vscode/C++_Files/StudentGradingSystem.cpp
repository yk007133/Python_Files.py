#include <iostream>
using namespace std;
int main(){
  cout<<"Student grading System";
  cout<<"\n\n";
  cout<<"Enter the marks obtained by student in each subjects :- \n";
  cout<<"\n\n";
  float maths , science, english, hindi, sst, sanskrit;
  cout<<"Enter the marks obtained in the maths : ";
  cin>>maths;
  cout<<"Enter the marks obtained in the science : ";
  cin>>science;
  cout<<"Enter the marks obtained in the english : ";
  cin>>english;
  cout<<"Enter the marks obtained in the hindi : ";
  cin>>hindi;
  cout<<"Enter the marks obtained in the sst : ";
  cin>>sst;
  cout<<"Enter the marks obtained in the sanskrit : ";
  cin>>sanskrit;
  cout<<"\n\n";
  float total;
  total=maths+science+english+hindi+sst+sanskrit;
  if(total>600){
    cout<<"Invalid Marks";}
  else{
    cout<<"The Total marks obtained by the student is : "<<total;
    cout<<"\n\n";
    cout<<"The Percentage obtained by the student is : "<<total/6;
    cout<<"\n\n";
    if(total<=600 && total>=551){
      cout<<"The student has got A+ grade";
    }
    else if(total<=550 && total>=450){
      cout<<"The student has got A grade ";
    }
    else if(total<=449 && total>=350){
      cout<<"The student has got B grade";
    }
    else if(total<=349 && total>=250){
      cout<<"The student has got C grade";
    }
    else if(total<=249 && total>=200){
      cout<<"The student has got D grade";
    }
    else{
      cout<<"The student has got failed!";
    }
  }
  return 0;
}













