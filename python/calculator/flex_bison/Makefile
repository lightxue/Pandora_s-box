default:
	bison -d calc.y
	flex calc.l
	g++ -o calc calc.tab.c lex.yy.c
clean:
	rm calc calc.tab.c calc.tab.h lex.yy.c
