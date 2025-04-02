#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(){
    cout<<"\n\n";
    cout<<"************** Stone-Paper-Scissor Game **************";
    cout<<"\n\n\n\n";
    cout<<"Press 1 for wants to Stone "<<endl<<"Press 2 for wants to Paper "<<endl<<"Press 3 for wants to Scissor \n\n";
    cout<<"\n\n";
    string  choice;
    int i=0;
    string arr[] = {"Stone","Paper","Scissor"};
    int ch[] = {1,2,3};
    while(i<1){
        cout<<"Enter your choice :  ";
        cin>>choice;
        cout<<"\n\n";
        
        srand(time(0));  //Sedding the time in srand() to help the rand() for generate new random no. every time.
                // Always define before the rand() function.    
        int chsize = sizeof(ch)/sizeof(ch[0]);   // Here 0 is not index no. , it is a null character.
        int chindex = rand() % chsize;     // It ensures and generate the no. within the range of [0-(chsize-1)] .
        string result = arr[chindex];
        if(choice=="1"){
            cout<<"You        :  Stone"<<endl<<"Computer   :   "<<result<<endl<<endl<<endl;
        }
        if(choice=="2"){
            cout<<"You        :  Paper"<<endl<<"Computer   :   "<<result<<endl<<endl<<endl;
        }
        if(choice=="3"){
            cout<<"You        :  Scissor"<<endl<<"Computer   :   "<<result<<endl<<endl<<endl;
        }
        if(choice=="1" && result=="Stone"){
            cout<<"\n";
            cout<<"Match Draw";
            cout<<"\n\n\n\n";
        }
        else if(choice=="1" && result=="Paper"){
            cout<<"\n";
            cout<<"Computer Win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="1" && result=="Scissor"){
            cout<<"\n";
            cout<<"You win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="2" && result=="Stone"){
            cout<<"\n";
            cout<<"You win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="2" && result=="Paper"){
            cout<<"\n";
            cout<<"Match Draw";
            cout<<"\n\n\n\n";
        }
        else if(choice=="2" && result=="Scissor"){
            cout<<"\n";
            cout<<"Computer win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="3" && result=="Stone"){
            cout<<"\n";
            cout<<"Computer win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="3" && result=="Paper"){
            cout<<"\n";
            cout<<"You win";
            cout<<"\n\n\n\n";
        }
        else if(choice=="3" && result=="Scissor"){
            cout<<"\n";
            cout<<"Match Draw";
            cout<<"\n\n\n\n";
        
        }
        else{
            cout<<"\n";
            cout<<"Invalid Choice";
            cout<<"\n\n\n\n";
        }
                    }
    return 0;
}

































