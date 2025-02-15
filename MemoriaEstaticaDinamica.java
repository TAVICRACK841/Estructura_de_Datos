import java.util.ArrayList;
public class MemoriaEstaticaDinamica {

    public static void main(String[] args) {
        // **Memoria Estática:**
        // El tamaño del array 'calificaciones' se define en tiempo de compilación (5 elementos).
        int[] calificaciones = new int[5];
        calificaciones[0] = 90;
        calificaciones[1] = 85;
        // ... (se deben asignar valores a todas las posiciones)

        System.out.println("Memoria Estática - Calificaciones:");
        for (int calificacion : calificaciones) {
            System.out.println(calificacion);
        }

        // **Memoria Dinámica:**
        // Usamos ArrayList para un tamaño que puede cambiar en tiempo de ejecución.
        ArrayList<Integer> listaCalificaciones = new ArrayList<>();
        listaCalificaciones.add(95);
        listaCalificaciones.add(88);
        listaCalificaciones.add(92);

        System.out.println("\nMemoria Dinámica - Lista de Calificaciones:");
        for (int calificacion : listaCalificaciones) {
            System.out.println(calificacion);
        }

        // Podemos agregar más elementos dinámicamente
        listaCalificaciones.add(76);
        System.out.println("\nMemoria Dinámica - Lista de Calificaciones (después de agregar un elemento):");
        for (int calificacion : listaCalificaciones) {
            System.out.println(calificacion);
        }
    }
}
