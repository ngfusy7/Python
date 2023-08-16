#include <iostream>
using namespace std; 

int n, a[10];

int isPrime(int a[10]){
	int flag = 1; 
	if(n <= 1){
		return 0; 
	}
	for(int i = 2; i < n; i++){
		if(n % i == 0){
			flag = 0;
			break;
		}
	}
	return flag;
}
int main(){
	cout << "Enter N: ";
	cin >> n; 
	cout << "\n";
	for(int i = 0; i < n; i++){
		cin >> a[i];
	}
	if(isPrime(a)){
		cout << "Is Prime";
	} else {
		cout << "Not Prime";
	}
}
