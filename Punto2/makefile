#si se quiere cambiar el tiempo hay que modificar el 0.1 en la 8 linea y los nombres de los archivos
all: sod_test.x estado_0.100000.dat estado_0.100000.pdf

sod_test.x: Punto2.c
	cc Punto2.c -lm -o sod_test.x

estado_0.100000.dat: sod_test.x
	./sod_test.x 0.1

estado_0.100000.pdf: estado_0.100000.dat graficas.py
	python graficas.py estado_0.100000.dat