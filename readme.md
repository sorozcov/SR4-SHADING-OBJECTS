# Silvio Orozco 18282
## Shading Objects

El objetivo de la siguiente fase del renderizador por software es que pueda cargar modelos 3D y colorearlos en tonalidades de gris de acuerdo a una fuente de luz. 

Parte del objetivo de ésta tarea es que demuestren su implementación del zbuffer. El zbuffer resulta ser del exacto tamaño que su framebuffer. Creen un método para renderizar su zbuffer a un bmp en tonalidades de gris. El valor de Z más alto debe ser blanco, y el valor de Z más bajo debe ser negro.

Para obtener la nota completa de ésta tarea deben entregar lo siguiente:

Código fuente capaz de cargar un archivo .obj al software renderer
Archivo obj de su elección 
Código fuente capaz de renderizar el zbuffer de su archivo obj
El modelo debe ser cargado en el centro de la pantalla y debe ser completamente visible. Recuerden incluir instrucciones sobre como renderizar su modelo y sobre cómo renderizar su zbuffer.



La nota máxima es 100.

Los puntos se darán así: Si rellenan el 100% del polígono 1 tienen 30 puntos, si rellenan el 90% tienen el 90% de los 30 puntos. Si se salen de las lineas, pierden puntos de la misma manera.

Envíen su código fuente renderizando todos los polígonos en un solo render, los puntos ya están puestos para que no se traslapen. Copia resultara en una nota inmediata de cero puntos.