//Declaration of the Header Files.
#include <iostream>
#include <string.h>
using namespace std;

// Declaration of a Function.
void poster(){
    cout<<"\n\n\n\n************ Hunny-Bunny Restaurant *************\n\n\n\n";
    cout<<"Hello Sir/Madam !\n\n\nHere is the Menu Card  : - \n\n\n";
}

void billing(){
    cout<<"Billing Options Available  :-  \n\n"<<endl<<"1. Net Banking"<<endl<<"2. UPI"<<endl<<"3. Credit/Debit Card"<<endl<<"4. Cash on Delivery"<<endl;
    cout<<"\n\n";
    int payment,pin;
    cout<<"What kind of payment mode would you prefer : ";
    cin>>payment;
    cout<<"\n\n";
    int s=0;
    while(s<1){
        if(payment>=1 && payment<=4){
            cout<<"Enter the pin :  ";
            cin>>pin;
            cout<<"Thankyou!"<<endl<<"Our Delivery Boy will Deliver your order soon !\n\n";
        }
        else{
            cout<<"Invalid Input, please try again !\n\n";
        }
    }


}

int main(){
    poster();      // Calling of a Function.

    //Declaration of the Arrays.

    string extra,item[10] = {"burger","pizza","fries","coke","icecream","pasta","noddles","sandwich","hotdog","paties"};
    int choice,price[10] = {100,200,60,50,80,150,100,70,90,65};
    float total = 0;       //Total price of items stored in this variables.

    //We use Do-while loop for complex programming.
    do{
        //Using For loop for presenting the menu card.
        for(int i=0;i<10;i++){
            cout<<i+1<<". "<<item[i]<<" - "<<price[i]<<" Rs."<<endl;
        }
        cout<<"\n\n";
        cout<<"Enter the name of item according to your choice(1-10)  :  ";
        cin>>choice;        //choice already define beacuse avoid the problem of scope of variable within the loop .
        cout<<"\n";         //Because if we define choice in do loop then it is undefined for while loop so define main.cpp.

        //Applying the Condition.
        if(choice>=1 && choice<=10){
            total = total+price[choice-1];
            cout<<"The Total price of your item is "<<total<<" Rs.\n\n";
        }
        else{
            cout<<"Invalid Input , Please Try Again ! \n\n";
        }  
        
        // Asking for another item.
        cout<<"Do you want to order the item(y/n)  :  ";
        cin>>extra;
        cout<<"\n\n";
    }
    while(extra=="y" || extra=="Y");    //extra already define beacuse avoid the problem of scope of variable within the loop .
    
    // Showing final total price of items.
    cout<<"\n\n";
    cout<<"Your Total price of items is "<<total<<" Rs."<<endl;
    cout<<"Thankyou for your Ordering !"<<endl<<endl;

    //Programming for the Billing/Payment of the order .
    billing();





    





    




    









    return 0;
}