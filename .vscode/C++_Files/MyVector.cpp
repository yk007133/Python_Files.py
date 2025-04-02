//A Vector in programming is a Dynamic Array. 
//A Vector can dynamically adjust its size to accommodate elements, unlike standard arrays which have a fixed size.

//##### Important #####

//At Declare time, The vector has considered that have a size 0 and have a capacity of 1 element. 
//After that as the size and capacity got same, capacity increase itself by doubling its capacity.


//------->>>>> Here are some key points about Vector:

//Dynamic Resizing : Vectors can grow or shrink in size automatically as elements are added or removed.
//Random Access    : Just like arrays, vectors provide constant-time access to elements using an index.
//Efficiency       : Vectors manage their own storage and resizing, ensuring efficient memory allocation and deallocation.
//Member Functions : Vectors come with several useful member functions like push_back, pop_back, insert, erase, and more, making them highly versatile.


//In C++ programming, a vector is a part of the Standard Template Library (STL) and is used to store elements in a dynamic array.
//It provides flexibility and a host of useful functionalities over traditional arrays.

//----->>>>>>> What is a Vector?

//Dynamic Array    : Unlike static/normal arrays, vectors can grow and shrink in size dynamically.
//Random Access    : Elements can be accessed directly using an index.
//Automatic Memory Management : Vectors handle their own memory allocation and deallocation.
//Member Functions : Vectors come with functions like push_back, pop_back, insert, and erase which make manipulation easy.


//----->>>>>  Common Operations and Member Functions :-

//Adding Elements    : push_back(value) adds an element to the end.
//Removing Elements  : pop_back() removes the last element.
//Accessing Elements : Use at(index) or the subscript operator [].
//Size of Vector     : size() returns the number of elements.
//Inserting Elements : insert(position, value) inserts an element at the specified position.
//Erasing Elements   : erase(position) removes the element at the specified position.
//Clearing the Vector: clear() removes all elements from the vector.
//Starting Element   : begin() start the array with our choice number.


//cpp

#include <vector>  
#include <iostream>
using namespace std;

int main() {
    // Declaring a vector of integers datatype.
    vector<int> numbers;

    // Adding elements to the vector
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);

    // Accessing elements
    cout << "First element: " << numbers[0] << endl;

    // Looping through the vector
    for (int i = 0; i < numbers.size(); i++) {
        cout << "Element at index " << i << ": " << numbers[i] << endl;
    }

    // Adding elements
    numbers.push_back(50);

    // Accessing elements
    cout << "Element at index 2: " << numbers[2] << endl;

    // Inserting element at the beginning
    numbers.insert(numbers.begin(), 5);

    // Removing the last element
    numbers.pop_back();

    // Erasing the second element
    numbers.erase(numbers.begin() + 1);

    //Printing the Vector
    cout<<"Vector Starting number is :- "<<numbers[0]<<endl;

    // Clearing the vector
    numbers.clear();

    cout << "Size of vector after clearing: " << numbers.size() <<endl;


    return 0;
}





















