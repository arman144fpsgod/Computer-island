g++ gen.cpp -std=c++20 -O2 -o gen.out
g++ code.cpp -std=c++20 -O2 -o code.out
g++ test.cpp -std=c++20 -O2 -o test.out

for(( i = 1; i <= 1000; i++ ))
do
	./gen.out > input.txt

	./code.out < input.txt > o1.txt

	./test.out < input.txt > o2.txt

	diff -bBq o1.txt o2.txt

	#if [ $? == 0 ]
	#then
	#	echo Accepted on test $i
	#else
	#	echo Wrong on test $i
	#	cat input.txt
	#	exit
	#fi

	if [ $? != 0 ]
	then
		echo Wrong on test $i
		echo Test:
		cat input.txt
		echo
		echo Output:
		cat o1.txt
		echo
		echo Answer:
		cat o2.txt
		exit
	fi

done

echo Accepted on All Tests