#include<iostream>

using namespace std;

long long dequy(int a, int b){
    if (b == 0) return 1;
    if ( b > 0 ) return a * dequy(a, b-1);
    else return 1.0;
}
int main(){
    int a, b;
    cin >> a >> b;
    cout << dequy(a, b);
    return 0;
}
