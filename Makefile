Logic-Sorting: thirdparty\main.o thirdparty\Parser.o thirdparty\Sorter.o
	python thirdparty\main.o
	python thirdparty\Parser.o
	python thirdparty\Sorter.o



main.o: src\main.py 
	python src\main.py

Parser.o: src\Parsingfile.py 
	python src\Parsingfile.py

Sorter.o: src\Sorting.py 
	python src\Sorting.py



clean:
	rm Logic-Sorting *o

