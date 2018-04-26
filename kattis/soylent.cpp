#include <iostream>

using namespace std;

int main(){
    int test;
    cin >> test;
    
    while(test--){
        int i, bottles;
        cin >> i;

        if((i % 400) == 0){
            bottles = (i/400);
        }
        else {
            bottles = (i/400) + 1;
        }
        
        cout << bottles << endl;
    }
    return 0;
}