-------------------------------------------------------------------------------------------------------------------------------

Este es el proyecto elegido para el trabajo integrador de la materia "Programación Orientada a Objetos" de la Institución de Formacion Técnica Superior N°18
El objetivo es lograr desarrollar un sistema similar a los tableros de trello/jira, pero un poco mas simple.

-------------------------------------------------------------------------------------------------------------------------------

```
Sistema tipo Trello{

    Descripción:Gestión de tareas mediante tableros, listas y tarjetas.

    Stack{
        Backend: Python
        DB: MySQL
        Frontend: React
    }

    Clases principales{
        Usuario
        Tablero
        Lista
        Tarea
    }

    Relaciones{
        Un usuario tiene múltiples tableros
        Un tablero contiene listas
        Una lista contiene tareas
    }

    POO aplicada{
        Composición fuerte (estructura jerárquica)
        Encapsulación en estados de tareas
        Posible uso de enums (estado/prioridad)
    }

    Funcionalidades base{
        Crear tableros
        Crear listas
        Crear/mover tareas
        Cambiar estado (ToDo / Doing / Done)
    }

    Extras{
        Prioridades
        Comentarios en tareas
        Usuarios compartidos
    }
}

```
-------------------------------------------------------------------------------------------------------------------------------

TAREAS 
1) Hacer el diagrama de clases
2) Crear las clases y objetos funcionales
3) Probar funcionalidad sin Frontend
4) Frontend/Visualizar objetos

-------------------------------------------------------------------------------------------------------------------------------
