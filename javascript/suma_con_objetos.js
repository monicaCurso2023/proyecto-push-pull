/* 
  Similar a **kwargs en Python

  En JS se utiliza el operador de propagación "..."
*/

function sumarConObjeto(valores) {
  let suma = 0;
  for (let key in valores) {
      suma += valores[key];
  }
  return suma;
}

let valores = {
  numero1: 5,
  numero2: 10,
  numero3: 15,
  numero4: 20
};

let resultado = sumarConObjeto(valores);
console.log("La suma de los números es:", resultado);
