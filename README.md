Proyecto 100% funcional y utilizable.
(Ver Pending.txt para extras que agregaré en un futuro .)

*Se utlizó el modelo de IA "Cursor" para diseño de pantallas y ordenamiento de objetos creados.*

-------------------------------------------------------------------------------------------------------------------------------

Este es el proyecto elegido para el trabajo integrador de la materia "Programación Orientada a Objetos" de la Institución de Formacion Técnica Superior N°18

El objetivo es lograr desarrollar un sistema similar a los tableros de trello/jira, pero un poco mas simple.

-------------------------------------------------------------------------------------------------------------------------------

```
Sistema tipo Trello{

    Descripción:Gestión de tareas mediante tableros, listas y tarjetas.

    Stack{
        Backend: Python
        DB: SQL Server
        Frontend: NodeJS / FrameWork React
    }

    Clases principales{
        Base
        Usuario
        Tablero
        Estado
        Tarea
        Comentario
    }

    Relaciones{
        Un usuario tiene un o mas tablero/s
        Un tablero contiene un o mas estado/s
        Una lista contiene una o mas tarea/s
        Una tarea tiene un o mas comentario/s
    }

    Funcionalidades base{
        Login/Register funcional
        Datos persistentes en una DB
        Manejo de sesión WEB
        Crear tableros
        Crear estados
        Crear/mover tareas
        Cambiar estado de tareas
    }

    Funcionalidades Descartadas (por ahora){
        Password Hashing  
    }
}

```
-------------------------------------------------------------------------------------------------------------------------------