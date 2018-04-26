#include <iostream>
#include <string>

using namespace std;

int main(){
    int i;
    
    cin >> i;

    int a_old;
    int a = 1;
    int b = 0;
    while(i--){
       a_old = a;
       a = b;
       b += a_old;
        
    }
    
    cout << a << " " << b;
    return 0;
}