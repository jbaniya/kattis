#include <iostream>

using namespace std;

int main() {
    
    int i;
    cin >> i;
    while(i){
        int num[2];
        int s, s1, s2;
        int initial_value;
        cin >> num[0] >> num[1];
        
        s = num[1]* (2*1 + (num[1] - 1)) / 2;
        initial_value = num[0];
        num[0] = 1;
        
        
        if((num[0] % 2) == 1) {
            s1 = num[1]* (2*num[0] + 2*(num[1] - 1)) / 2;
            num[0]++;
            s2 = num[1]* (2*num[0] + 2*(num[1] - 1)) / 2;
        }
        else {
            s2 = num[1]* (2*num[0] + 2*(num[1] - 1)) / 2;
            num[0]++;
            s1 = num[1]* (2*num[0] + 2*(num[1] - 1)) / 2;
        }
        cout << initial_value << " " << s << " " << s1 << " " << s2 << endl;
        i--;
    }
    return 0;
}