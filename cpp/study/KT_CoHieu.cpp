#include <iostream>
using namespace std; 

int n, a[100];

int check(int a[100]){
	int flag = 0;
	for(int i = 0; i < n; i++){
		if(a[i] % 2 == 0){
			flag = 1;
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
	if(check(a) == 1 ){
		cout << "YES";
	} else {
		cout << "NO";
	}
	return 0;
}
