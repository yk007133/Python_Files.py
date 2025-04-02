#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> yash = {4,6,2,4,5,6,4,3,2,3};
    cout<<yash[9]<<endl;
    yash.push_back(4);
    cout<<yash.size()<<endl;
    yash.pop_back();
    cout<<yash.size()<<endl;
    yash.insert(yash.begin(),7);   //In Insert, It only except standard position like start & end.
    cout<<yash[0]<<endl;
    yash.erase(yash.end());        //In Insert, It only except standard position like start & end.
    cout<<yash[10]<<endl;
    yash.clear();
    cout<<yash[8]<<endl;
    


    
    
    
    
    
    return 0;
}