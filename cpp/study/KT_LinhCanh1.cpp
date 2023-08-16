#include <iostream>
using namespace std; 

int LSearch(int a[], int n, int x){
	int i = 0; 
	while(i < n && a[i] != x){
		i++;
		if(i < n){
			return i;
		}
	}
	return -1;
}

bool ktSoAm(int a[], int n){
	a[n] = -1;
	int i = 0; 
	while(a[i] >= 0){
		i++;
	}
	return (i<n);
}


int main(){
	
}
