import java.util.ArrayList;
import java.util.Scanner;

public class VentasMensuales {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> meses = new ArrayList<>();
        ArrayList<Double> ropa = new ArrayList<>();
        ArrayList<Double> deportes = new ArrayList<>();
        ArrayList<Double> jugueteria = new ArrayList<>();

        mostrarMenu(scanner, meses, ropa, deportes, jugueteria);
    }

    public static void ingresarDatos(Scanner scanner, ArrayList<String> meses, ArrayList<Double> ropa, ArrayList<Double> deportes, ArrayList<Double> jugueteria) {
        while (true) {
            System.out.print("Ingrese el nombre del mes (o 'fin' para terminar): ");
            String mes = scanner.nextLine();
            if (mes.equalsIgnoreCase("fin")) {
                break;
            }

            double ventaRopa = validarEntrada(scanner, "Venta de ropa en " + mes + ": ");
            double ventaDeportes = validarEntrada(scanner, "Venta de deportes en " + mes + ": ");
            double ventaJugueteria = validarEntrada(scanner, "Venta de jugueteria en " + mes + ": ");

            meses.add(mes);
            ropa.add(ventaRopa);
            deportes.add(ventaDeportes);
            jugueteria.add(ventaJugueteria);
        }
    }

    public static double validarEntrada(Scanner scanner, String mensaje) {
        while (true) {
            try {
                System.out.print(mensaje);
                return Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Error: Ingrese un número válido.");
            }
        }
    }

    public static void buscarElemento(Scanner scanner, ArrayList<String> meses, ArrayList<Double> ropa, ArrayList<Double> deportes, ArrayList<Double> jugueteria) {
        System.out.print("Ingrese el mes a buscar: ");
        String mesBuscar = scanner.nextLine();
        int indice = meses.indexOf(mesBuscar);
        if (indice != -1) {
            System.out.println("Ventas en " + mesBuscar + ":");
            System.out.println("  Ropa: $" + ropa.get(indice));
            System.out.println("  Deportes: $" + deportes.get(indice));
            System.out.println("  Jugueteria: $" + jugueteria.get(indice));
        } else {
            System.out.println("Mes no encontrado.");
        }
    }

    public static void eliminarVenta(Scanner scanner, ArrayList<String> meses, ArrayList<Double> ropa, ArrayList<Double> deportes, ArrayList<Double> jugueteria) {
        System.out.print("Ingrese el mes a eliminar: ");
        String mesEliminar = scanner.nextLine();
        int indice = meses.indexOf(mesEliminar);
        if (indice != -1) {
            meses.remove(indice);
            ropa.remove(indice);
            deportes.remove(indice);
            jugueteria.remove(indice);
            System.out.println("Ventas de " + mesEliminar + " eliminadas.");
        } else {
            System.out.println("Mes no encontrado.");
        }
    }

    public static void mostrarMenu(Scanner scanner, ArrayList<String> meses, ArrayList<Double> ropa, ArrayList<Double> deportes, ArrayList<Double> jugueteria) {
        while (true) {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Ingresar datos de ventas");
            System.out.println("2. Buscar ventas por mes");
            System.out.println("3. Eliminar ventas de un mes");
            System.out.println("4. Salir");

            System.out.print("Seleccione una opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "1":
                    ingresarDatos(scanner, meses, ropa, deportes, jugueteria);
                    break;
                case "2":
                    buscarElemento(scanner, meses, ropa, deportes, jugueteria);
                    break;
                case "3":
                    eliminarVenta(scanner, meses, ropa, deportes, jugueteria);
                    break;
                case "4":
                    System.out.println("¡Hasta luego!");
                    return;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        }
    }
}
