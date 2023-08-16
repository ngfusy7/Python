#include <iostream>
using namespace std; 

void swap(int &a, int &b){
	int temp = a; 
	a = b; 
	b = temp; 
}

int main(){
	int first = 5; 
	int second = 7; 
	cout << "First and Second: " << first << second;
	swap(first, second);
	cout << "First and Second: " << first << second;
	return 0;
}
