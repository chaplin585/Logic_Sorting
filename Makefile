Logic-Sorting: main.o
	python main.o



main.o: src\main.py 
	python src\main.py

clean:
	rm Logic-Sorting *o

