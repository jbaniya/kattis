#include <iostream>
#include <string>

using namespace std;

int main() {
    std::string number_one, number_two;
    
    cin >> number_one >> number_two;
      
    std::string result1 = "";
    std::string result2 = "";
    
   
    while(number_one.length() < number_two.length()){
        number_one = "0" + number_one;
    }
    
    while(number_one.length() > number_two.length()){
        number_two = "0" + number_two;
    }
    
    for(int i = 0; i < number_one.length(); i++) {
        if(number_one[i] >= number_two[i]){
            result1+= number_one[i];
        }
        
        if(number_one[i] <= number_two[i]) {
            result2+= number_two[i];
        }
    }
    
    
    while(result1[0] == '0' && result1.length() > 1){
        result1 = result1.substr(1, result1.length()-1);
    }
    
    while(result2[0] == '0' && result2.length() > 1){
        result2 = result2.substr(1, result2.length()-1);
    }
    
    
    if(result1 == "") result1 = "YODA";
    if(result2 == "") result2 = "YODA";
    

    cout << result1 << " " << result2;
    return 0;
}