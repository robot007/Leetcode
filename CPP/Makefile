all: RemoveDuplicates_class.exe RemoveDuplicates_func.exe TestCompiler.exe

# all: $(patsubst %.c, %.exe, $(wildcard *.c))
%.exe: %.cpp Makefile
	g++ $< -o $@ -Wall -O2
