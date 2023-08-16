#include <iostream>
#include <math.h>
using namespace std; 

int n = 5; 
float S(int n){
	if(n == 0) 
		return 0;
	else 
		return sqrt(2+S(n-1));
}

int main(){
	cout << S(n);
	return 0;
}
