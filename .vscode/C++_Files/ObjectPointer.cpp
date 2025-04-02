#include <iostream>                      //Where <iostream> is the required Header-file.
using namespace std;
class Cricketer{
    public:
    string name;                         //Where name,runs and average are attributes of class.
    int runs;
    float average;
    Cricketer(string name,int runs,float average){
        this->name = name;               // Use of this keyword to avoid complexity for computer.
        this->runs = runs;
        this->average = average;
    }
    void function(string c){             //Function Declare within the Classes.
        cout<<name<<" "<<runs<<" "<<average<<endl;
        cout<<c<<endl;
        }
};

//-------->>>>> It is a call by value so not permanent changes in (*c3) means c1.

void print(Cricketer c){
    Cricketer* j = &c;         
    (*j).name = "Mahendra Singh Dhoni";
}

//-------->>>>> There are 2 diff. kind of call by refrence so got permanent changes in (*c3).

//------>>>>> Type-1. Basic Terminology[&].

void refrence(Cricketer& c){        
    Cricketer* j = &c;
    j->name = "Mahendra Singh Dhoni";
}

//------>>>>> Type-2. With help of Object-Pointer.

void type2(Cricketer* d){          //It is necessary to take such kind of Datatype in parameter of 
    d->name = "SuryaKumar Yadav";  //a function otherwise call by refrence by pointer not happen.
}

int main (){             // ------>>> Object Pointer as a Simple in main.cpp.
    int a =5;
    cout<<&a<<endl;      //It always gives the address of that variable in which we put "&". 
                         //Every next running the code , it will give you diff. address of a.
    int* b = &a;         //&a = Address of a .
    cout<<*b<<endl<<b<<endl; //&a is address of diff. kind ,so also need Datatype of diff. kind like 'int*'.
                         //If variable f has floattype then use float* to store the &f(address of f).
                         //Where *b is called Pointer.
                         //Here *b = a [Means b ke ander jo address he us pr jao or us address mein
                         //jo value he vo lao thst its]. 
    
    Cricketer c1("Virat Kohli",25000,57.8);
    c1.function("Hello");
    Cricketer c2("Rohit Sharma",18000,48.3);
    c2.function("Namaste");

                                //-------->>> Object Pointer as in the Classes and Onjects. 
   
    cout<<&c1<<endl;            //It gives address of thing which is stored in object c1.
    Cricketer* c3 = &c1;        //It stores address of variable c1 in variable c3.
   
    (*c3).name = "Sachin Tendulkar";  //------->>>>> All same for the object c2.

    cout<<c3<<endl<<(*c3).runs<<endl; //Here c3 called Pointer.It is also a variable that holds 
                                      //memory address of another variable.
    cout<<(*c3).name<<endl;           //We can't use *c3 as a single as *b , because *c3 has lot of varieties.
                                //So, [(*c3).runs = c1.runs] and Here bracket of *c3 is compulsory,
                                //Which is not necessary in *b due to have a single type of variety.
    
    // ------->>>>>Instead of using (*c3) in (*c3).name, we can also use this:- 'c3->' [That is not okward as much (*c3)].
    // ------->>>>>We cannot use 'c3->' as a Single like (*c3), If you want to use as a single please go for (*c3).Like, 
    
    c3->runs = 50000;
    cout<<c3->runs<<endl;

                      
    print((*c3));               //It is output of call by value.
    cout<<c1.name<<endl;
    
    
    refrence((*c3));            //It is output of call by refrence by Type-1.
    cout<<c1.name<<endl;

    type2(c3);                  //It is output of call by refrence by Type-2.
    cout<<c1.name<<endl;

    //so pointer stores the address of any variable but its also have an address, which is stored
    //is store with the help of the double pointer.

    Cricketer** dptr = &c3;
    cout<<dptr<<endl<<*dptr<<endl<<(**dptr).name<<endl<<(**dptr).average<<endl;

                       //It is return-type of int Datatype used in running the main.cpp.

    //### Pointer Arthmetic : - 

    //All operators are illegal expect to :-

    //Increment/decrement,Addition of integer of a point,
    //Substracting of integer of a point,Substracting of 2 pointers of same type and comparison of pointers.

    //### Pointers always increse its address by an order of 4/8 units.
    //formula :-  [new address = current address + (number*sizeof(datatype))]   

    //Above valid operator also work if both pointer have of same datatype.
    //Comparison of point :-
    // <,>=,>,<=,==,!=,etc.

    //#code

    
















    return 0;










    }



























