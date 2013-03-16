#include<stdio.h>

int main(void){
	extern "C"{
		Foo* foo_new(){ return new Foo(); }
		void foo_bar( Foo* foo ){ foo->bar(); }
	}
	return 0;
}
