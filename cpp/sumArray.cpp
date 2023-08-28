#include <iostream>
using namespace std; 

int main(){
	long long n;
	long long a[n]; 
	long long sum = 0;
	cin >> n; 
	for(int i = 0; i < n; i++){
		cin >> a[i];
	}
	for(int i = 0; i < n; i++){
		sum += a[i];
	}
	cout << sum;
	return 0;
}
