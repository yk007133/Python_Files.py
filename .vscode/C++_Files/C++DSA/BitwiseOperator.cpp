#include<iostream>
using namespace std;
int main(){  

//### Important Information :- 
//Firstly know the number 1 to 10 in binary for 4/8 places digits and 1s and 2s complement.
//Then and(&),or(|),xor(^) are follow according to their logic tables & convert into decimal no.
//For not(~), then find the 2s complement of that variable then add 1 in it then convert in decimal no.

    int a = 5;    //in binary , 0101
    int b = 6;    // binary , 0110 Then sum of the both binary number acc. to their logic gates.
    cout<<(a&b)<<endl;
    cout<<(a|b)<<endl;
    cout<<(a^b)<<endl;
    cout<<(~a)<<endl;
    

    return 0;
}




