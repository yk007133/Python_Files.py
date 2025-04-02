#include<iostream>
using namespace std;
class Vechicle{

    //------->>>>>> public

    public:               //Here public is Access Modifier,under which variable is defined,
        string name;      //can be accessible in within the class and everywhere.
        float millege;
        string fuel;

        Vechicle(string name,float millege,string fuel,bool bootspace,int numberplate){    
        this->name = name;                         //It is noticed that the constructor & functions
        this->millege = millege;                   //must be in public section,Then otherwise                                                                 
        this->fuel = fuel;                         //you do not use it,After making them private.
        this->bootspace = bootspace;                
        this->numberplate = numberplate;           //With the help of Constructor,we can print
        this->numberplate = 4321;                  //and change the private variables.
        cout<<this->numberplate<<endl;
        }                                           
        
        Vechicle(){                                //Default Constructor to tell something.
                                                   //It is defined to avoid complexity for PC.
        }

        void display(){                            //It working like a getter() function.
            cout<<name<<" "<<millege<<" "<<fuel<<" "<<bootspace<<" "<<numberplate<<endl;
        }

        void setvalue(int n,bool y){
            this->numberplate = n;
            this->bootspace = y;
        }

    //------->>>>>> protected

    protected:            //Here protected is Access Modifier,under which variable is defined,
        bool bootspace;   //can be accessible in within the class and only in its derived class.
                          //in the Inheritance.
    
    //------->>>>>> private

    private:              //Here private is Access Modifier,under which variable is defined,
        int numberplate;  //can be accessible only in within the class.
                          
                          //You cannot print and change private variable normally.
                          //But with the help of constructor, it is possible.
    };

int main(){

    //-------->>>>>> With the help of Constructor

    Vechicle v1("Bentely",23.4,"CNG",true,3712);  
    v1.display();                                      
                                            //With the help of Constructor, we are able   
                                            //to initialize protected and private variables too.
    
    //-------->>>>>> With the help of Default Constructor

    Vechicle c2;
    c2.name = "Fortuner";                   //With the help of default construtor,we cannot 
    c2.millege = 34.5;                      //initialize the protected and private variables too.
    c2.fuel = "Diesel";
    c2.display();                           //display function considered value of bootspace
                                            //and numberplate is zero due to not Initializing.
    c2.setvalue(2004,false);
    c2.display();                           //But After use of setter() to assign the value of 
                                            //private and protected variable.


    //------>>>>>> We know that we can print and change the value of protected and private variable
    //via constructor But if make a function in class in public section to make it publicly used to 
    //print the private variable then this function is called getter().
    
    //------>>>>>> We know that we can print and change the value of protected and private variable
    //via constructor But if make a function in class in public section to make it publicly used to 
    //set/change the private variable then this function is called setter().
    
    //getter() and setter() are defined in the public section in the class to make it public.

    return 0;
}










