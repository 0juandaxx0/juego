El codigo es un juego estilo galaga creado con pygame, donde el jugador con su nave debe esquivar los disparos enemigos y disparar para eliminarlos, asi alcanzar el mayor puntaje posible antes de perder las 3 vidas. 

Una vez iniciado el juego tendra un menu principal con funciones basicas en el cual podra iniciar el juego, una guia de los controles y el objetivo del juego. estos diran con que teclas acceder a las diferentes funciones ya que esta diseñado para ser jugado unicamente con el teclado.
- Pulsando la tecla ENTER iniciara el juego
- Pulsando la tecla C abrira una nueva ventana para conocer los controles
- Pulsando la tecla O abrita una ventana la cual menciona el objetivo del juego

El juego funciona usando las teclas de movimiento de izquierda y derecha, haciendo que la nave se mueva en un unico eje, y podra disparar usando la tecla de ESPACIO para eliminar los ovnis, estos apareceran en grupos de 8 en posiciones aleatorias por la pantalla, sin superar la mitad de esta para evitar problemas con la nave del jugador. Estos ovnis son el objetivo del jugador los cuales tambien podran disparar con el fin de eliminar la nave, cada vez que terminemos con los 8 ovnis iniciales, automaticamente aparecera otro grupo para continuar el juego, esto se repetira hasta que se terminen las 3 vidas.

En la pantalla del juego podremos ver el contador de puntaje y de vidas, ambos se actualizan con las acciones que ocurran en el juego de la sigueinte forma:
- El contador del puntaje aumentara cuando eliminemos un ovni, este iniciara en 0 y una eliminacion da 10 puntos.
- El contador de vidas dismiye cuando un proyectil de un ovni alcance la nave, este iniciara en 3 vidas y cada proyectil que reciba sera una vida menos hasta llegar a 0.

Cuando el contador de vidas llega a 0, el juego terminara y mostrara una pantalla de Game Over indicando que ha perdido, esta pantalla muestra 3 opciones, para volver a jugar, volver al menu principal o cerrar el juego.
- Para volver a jugar prisionar la tecla R, esto iniciara el juego nuveamente reiniciando el contador de puntaje y de vidas.
- Para volver al menu debe presionar la tecla M, esto abrira nuevamente el menu principal que abre al iniciar el programa.
- Para cerrar el jeugo presiona la tecla ESC, esto cerrara definitivamente el programa, usando la libreria sys se logra esto.

Para diseñar este juego se usaron 3 imagenes de internet para el fondo, la nave y los enemigos, el resto de diseño esta creado usando unicamente la libreria de pygame.

Se utilizaron unas funciones adicionales para poner en pantalla la nave y los enemigos de forma aleatoria, usando la libreria de random y convinandola con pygame se logro dibujar en pantalla. 

Para la estructura principal del juego se declara la funcion game(), en la cual se da la posicion del jugador, listas para los poyectiles, cantidad de enemigos, el puntaje y las vidas.
Para el movimiento del jugador se usaron condicionales que validan primero la entrada del teclado y luego valida el movimiento o disparo del jugador, como restriccion el jugador podra disparar 5 proyectiles estando quieto.
Para las colisiones del proyectil de la nave con los ovnis valida si estan en el mismo espacio del enemigo, luego incrementa el puntaje y llama una funcion para quitar el ovni de pantalla.
Para las colisiones de los proyectiles enemigos y la nave es similar validando si estan en el mismo espacio que la nave, si es asi el contador de vidas le resta 1, valida si este contador llega a 0 y termina el juego en este caso.

El flujo del juego al iniciar lo primero que veremos es el menu principal, luego el juego y finalmente una pantalla de Game Over el cual puede reciniciar el ciclo volvienco al menu o el juego, o cerrando el programa definitivamente.