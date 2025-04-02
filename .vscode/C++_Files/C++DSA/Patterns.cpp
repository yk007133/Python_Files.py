#include<iostream>
using namespace std;

//Declarartion of the Function.

void simplepyramid(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<i;j++){
            cout<<"* ";
        }
        cout<<endl;   //You think about that why we use it and what its importance in this place. 
    }
}
void usingwhile(int n){
    int i = 0,j = 0;
    while(i<n){
        while(j<=i){
            cout<<"* ";
            j++;
        }
        j = 0;  //##### Important #####
                // we have to reset j value because its aukaat remains in (i-while) also ,
                // due to it is declare startingly with i,
                // so as it can start from beginning and print * equal to i.
        cout<<endl;
        i++;
            }
}
void yash(int n){

for (int i = n; i > 0; i--) {
    for (int j = 1; j <= n; j++) 
    {
        if (j >= i) {
            cout << "* ";
        }
        else {
            cout << "  ";
        }
    }
    cout << endl;
    } 
}

void fliptriangle(int n){
    for(int i = n;i > 0;i--){
        for(int j = 0;j < i;j++){
            cout<<"* ";
        }
        cout<<endl;
    }

}

void equilateraltriangle(){
    for(int i = n;)
}

//Main function for calling the function.
int main(){
    int choice;
    choice = 10;
    simplepyramid(choice);
    cout<<"\n\n";
    usingwhile(choice);
    cout<<"\n\n";
    yash(choice);
    cout<<"\n\n";
    fliptriangle(choice);
    cout<<"\n\n";


    return 0;

}





