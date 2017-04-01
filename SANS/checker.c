char scode[] = "";

int main(int argc, char **argv){
	int (*one)();
	one = (int(*)())scode;
	(int)(*one)();
}

//compile this using gcc checker.c -o checker
//
