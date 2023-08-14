# mobilERG

## ¿Qué es y qué puedo hacer con mobilERG?

Antes de explicar la tecnología que existe detrás de este prototipo vamos a ver diferentes usos que podríamos darle, creo que de esta forma se entiende mucho mejor. A partir de ahora cuando nombre a mobilERG estaré haciendo referencia a todo el prototipo funcionando.

Con pequeños conocimientos de electrónica y una base mínima de programación podemos llegar a darle usos infinitos. Lo primero que debemos diferenciar de mobilERG son 2 modos de uso muy diferentes:

- Modo 1: mobilERG nos avisa a nosotros indicándonos que se produjo algún evento en la distancia mediante una llamada o SMS.
- Modo 2: Nosotros realizamos una llamada o enviamos un SMS para avisar a mobilERG y que comience a realizar una acción previamente definida.

<hr>

## Modo 1

**Listaré algunos usos para verlo con claridad y que podamos apreciar el potencial del Modo 1** (el sistema es quién me avisa de que ocurrió algún evento):
- El precio de Ergo sube y me llega un SMS a mi teléfono personal indicando que Ergo está camino de la luna.
- Mi cartera Ergo pasó de tener 100 ERG a tener 103 ERG.
- Se detectan movimientos en casa mediante un sensor y mobilERG me envía un SMS indicándome que hay movimientos en casa.
- Todo lo que se nos ocurra…

<hr>

### Modo 2

**Listaré algunos usos para verlo con claridad y que podamos apreciar el potencial del Modo 2** (nosotros avisamos al sistema para que se realice alguna acción en la distancia):
- Hacer un envío de ERG a una cartera determinada.
- Crea un token.
- Instalar el nodo.
- Última voluntad.
- Apagar la luz de casa.
- Formateo del ordenador.
- Todo lo que se nos ocurra…

<hr>

**Modo 1**: mobilERG nos avisa de que ocurrió algo.

**Modo 2**: Avisamos a mobilERG para que realice una acción.

(Los avisos del **Modo 1** y **Modo 2** pueden ser mediante llamada de teléfono o envío-recepción de SMS). 

<hr>

### Desarrollo del ejemplo
Nos centraremos para este ejemplo en el **Modo 2.**

### ¿Puedo enviar 0.01 ERG a la cartera de un amigo con solo hacer una llamada o enviando un SMS?   
Por supuesto que sí, puedes realizar este tipo de envíos y muchas acciones más.

### Vamos a ver cómo realizar el envío de 0.01 ERG a un amigo realizando una llamada.

Este ejemplo podría desarrollarse de forma íntegra con una Raspberry Pi Zero, ya que ésta dispone de GPIO para el módulo SIM800L y a que las versiones del nodo de Ergo son increíblemente ligeras y rápidas de sincronizar. Aunque de esta forma lo dejaremos para el siguiente ejemplo.

Ahora vamos a ver cómo realizarlo usando estos componentes: 
- Ordenador.
- Arduino UNO.
- SIM800L.
- Tarjeta SIM (aunque no es obligatorio eliminar el PIN de seguridad, sí que es más fácil).
- La librería ergpy con la que interactuaremos con el blockchain de Ergo (nodo público).

<hr>

### Un breve resumen del funcionamiento de mobilERG:
Por un lado tengo un Arduino con un módulo SIM800L conectado (este módulo permite enviar llamadas, SMS y recibirlos). Este Arduino mediante comandos AT analiza lo que ocurre en el módulo SIM800L y en base a los valores (SMS o llamadas que envía o recibe) envía por el puerto serial la información que yo le indique.

Por otro lado tengo ejecutándose una mini aplicación escrita en Python leyendo el puerto serial de mi equipo. En base a los valores que recibe (valores que envío desde Arduino) puedo enviar ERG, crear un token, o lo que me apetezca.

<hr>

## Conexión para el módulo SIM800L a nuestro Arduino UNO

**Diodo 1N4007** 
Este diodo nos servirá para alimentar de forma correcta el módulo SIM800L (restamos 0,7 voltios), ya que lo estamos alimentando con 5 voltios y únicamente necesita 4,3 voltios.

<img src="https://ergonfts.org/other_images/sim800L-connection.png" alt="Esquema de conexión para Arduino y SIM800L">