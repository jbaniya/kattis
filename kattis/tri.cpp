#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    
   int num[3];
   cin >> num[0] >> num[1] >> num[2];
   
    if((num[0] + num[1]) == num[2] )
       cout << num[0] << "+" << num[1] << "=" << num[2];
    else if((num[0] * num[1]) == num[2] )
       cout << num[0] << "*" << num[1] << "=" << num[2];
    else if((num[0] - num[1]) == num[2] )
       cout << num[0] << "-" << num[1] << "=" << num[2];
    else if((num[0]/num[1]) == num[2] )
       cout << num[0] << "/" << num[1] << "=" << num[2];
    else if((num[1] + num[2]) == num[0] )
       cout << num[0] << "=" << num[1] << "+" << num[2];
    else if((num[1] * num[2]) == num[0] )
       cout << num[0] << "=" << num[1] << "*" << num[2];
    else if((num[1] - num[2]) == num[0] )
       cout << num[0] << "=" << num[1] << "-" << num[2];
    else if((num[1]/num[2]) == num[0] )
       cout << num[0] << "=" << num[1] << "/" << num[2];
   
    return 0;
   }