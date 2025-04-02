#include <iostream>      
#include <cstdlib>          //Must Headerfile for generate random number.
#include <ctime>
using namespace std;

int main() {
    // Seed the random number generator with the current time
    srand(time(0));

    // Define an array
    int myArray[] = {10, 20, 30, 40, 50,60,70,80,90,100};
    int arraySize = sizeof(myArray) / sizeof(myArray[0]);
    cout<<"\n\n";
    // Generate a random index between 0 and arraySize - 1
    int randomIndex = rand() % arraySize;

    // Access the value at the random index
    int randomValue = myArray[randomIndex];
    

    cout << "Random value from array: " << randomValue << endl<<endl<<endl;

    return 0;
}






























