#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    string name,number,key;
    cin>>n;
    map<string,string>phonebook;
    for(int i=0;i<n;i++)
    {
        cin>>name>>number;
        phonebook[name]=number;
    }
    while(cin>>key)
    {
        if(phonebook.find(key)!= phonebook.end())
        {
            cout<<key<<"="<<phonebook.find(key)->second<<endl;
        }
        else
        {
            cout<<"Not found"<<endl;
        }
    }

    return 0;
}
