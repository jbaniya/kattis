#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    int z;
    int mid, first, last;
    int space = 0;
    while(scanf("%d",&z),z){
       
       int a[z],b[z],temp[z];
       for (int i = 0; i < z ; i++){
           scanf("%d",&a[i]);
           temp[i] = a[i];
           
       }
       
       for (int i = 0; i < z; i++){
           scanf("%d", &b[i]);
           
       }
        std::sort(temp, temp+z);
        std::sort(b, b+z);
        
       
       
        for(int i = 0;i < z; i++){
            first = 0, last = z-1;
            do {
                mid = (first + last) /2;
                if(temp[mid] > a[i])
                    last = mid - 1;
                else if (temp[mid] < a[i])
                    first = mid + 1;
            } while(temp[mid]!=a[i]);
            
            printf("%d",b[mid]); cout << '\n';
            
        }
        cout << endl  ;
    }   
}