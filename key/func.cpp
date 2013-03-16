#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>

using namespace std;

bool isPrimer(unsigned long n){
	if( n==1 || n==0 ){
		return false;
	}
	if( n==2 ){
		return true;
	}
	
	for( int sub=2; sub<n; sub++ ){
		if( n%sub==0 ){
			cout<<"  "<<sub<<endl;
			return false;
		}
	}

	return true;
}

int main(int argc, char* argv[]){
	unsigned long test[] = {
		0xffff
	 };
	int length = sizeof(test)/sizeof(unsigned long);
	
	for(int index=0; index<length; index++){
		if( isPrimer(test[index]) ){
			cout<<test[index]<<" is primer"<<endl;
		}else{
			cout<<test[index]<<" is not primer"<<endl;
		}
	}

	return 0;
}
