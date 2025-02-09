# Estructura_de_Datos
Repositorio que servirá para la materia de Estructura de Datos 


Explicación del Código Python:

1. ingresar_datos():
 •Permite al usuario ingresar el nombre del mes y las ventas de ropa, deportes y juguetería para ese mes.
 •Utiliza un bucle while para asegurarse de que las entradas de ventas sean números válidos.
 •Almacena los datos en listas separadas (meses, ropa, deportes, jugueteria).

2. buscar_elemento():
 •Pide al usuario que ingrese el mes que desea buscar.
 •Si el mes se encuentra en la lista meses, muestra las ventas correspondientes de ropa, deportes y juguetería.

3. eliminar_venta():
 •Pide al usuario que ingrese el mes cuyas ventas desea eliminar.
 •Si el mes se encuentra, elimina los datos correspondientes de las cuatro listas.

4. mostrar_menu():
 •Muestra un menú con las opciones disponibles.
 •Utiliza input() para obtener la opción del usuario.
 •Llama a las funciones correspondientes según la opción seleccionada.


Explicación del Código Java:

1. main():
 •Crea un objeto Scanner para leer la entrada del usuario.
 •Inicializa cuatro ArrayList para almacenar los meses y las ventas de cada categoría.
 •Llama a la función mostrarMenu() para iniciar la interacción con el usuario.

2. ingresarDatos():
 •Similar a la función en Python, permite al usuario ingresar los datos de ventas mensuales.
 •Utiliza un bucle while para permitir la entrada de múltiples meses.
 •Llama a la función validarEntrada para asegurarse de que las entradas de ventas sean números válidos.

3. validarEntrada():
 •Muestra un mensaje al usuario y espera a que ingrese un número.
 •Utiliza un bloque try-catch para manejar la excepción         NumberFormatException que ocurre si el usuario ingresa un valor no numérico.
 •Continúa pidiendo la entrada hasta que se ingrese un número válido.

4. buscarElemento():
 •Pide al usuario que ingrese el mes que desea buscar.
 •Utiliza el método indexOf() de ArrayList para encontrar el índice del mes.
 •Si el mes se encuentra, muestra las ventas correspondientes.

5. eliminarVenta():
 •Pide al usuario que ingrese el mes cuyas ventas desea eliminar.
 •Utiliza el método indexOf() para encontrar el índice del mes.
 •Si el mes se encuentra, elimina los datos correspondientes de las cuatro listas utilizando el método remove().

6. mostrarMenu():
 •Muestra un menú con las opciones disponibles.
 •Utiliza scanner.nextLine() para obtener la opción del usuario.
 •Utiliza una estructura switch para llamar a las funciones correspondientes según la opción seleccionada.