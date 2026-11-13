# b) Consumo con React

Para mostrar en React la lista de animales que devuelve el método GET, se crea un
componente funcional que guarda los datos en un estado, los pide al servidor cuando
el componente aparece en pantalla y luego los recorre para dibujar cada elemento.

**useState.** `const [animales, setAnimales] = useState([])` crea una variable de
estado que guardará el arreglo recibido de la API. Se inicia como arreglo vacío para
que, antes de que llegue la respuesta, el componente pueda dibujarse sin errores.
Cada vez que se llama a `setAnimales` con datos nuevos, React vuelve a renderizar el
componente y la lista se actualiza en pantalla.

**useEffect.** La petición a la API es un efecto secundario, por eso se coloca
dentro de `useEffect`. El segundo argumento es un arreglo de dependencias vacío
(`[]`), lo que indica que el efecto se ejecuta una sola vez, cuando el componente se
monta. Sin ese arreglo, la petición se repetiría en cada renderizado y se generaría
un ciclo infinito, porque actualizar el estado provoca un nuevo renderizado.

**fetch.** Dentro del efecto, `fetch("http://127.0.0.1:8001/api/animales/")` envía
una solicitud GET al endpoint de listar. Como es asíncrona, devuelve una promesa: el
primer `.then` convierte la respuesta a objeto JavaScript con `res.json()` y el
segundo guarda ese arreglo en el estado con `setAnimales(data)`. Para que el
navegador permita la petición desde la aplicación de React (otro puerto), el backend
de Django tiene configurado `django-cors-headers`.

**map con key.** En el `return`, `animales.map(...)` recorre el arreglo y convierte
cada objeto en un elemento `<li>` que muestra su nombre, especie y edad. A cada
elemento se le asigna la propiedad `key={a.id}`; el id es único porque viene de la
llave primaria en MySQL. React usa esa `key` para identificar cada elemento de la
lista y, cuando los datos cambian, saber cuál se agregó, modificó o eliminó, en lugar
de volver a dibujar toda la lista.

```jsx
import { useState, useEffect } from "react";

export default function ListaAnimales() {
  const [animales, setAnimales] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8001/api/animales/")
      .then((res) => res.json())
      .then((data) => setAnimales(data));
  }, []);
  return (
    <ul>
      {animales.map((a) => <li key={a.id}>{a.nombre} - {a.especie} ({a.edad} años)</li>)}
    </ul>
  );
}
```
