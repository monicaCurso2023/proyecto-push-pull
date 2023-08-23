// Similar a args en Python

function sumarConArguments() {
  let suma = 0;
  for (let i = 0; i < arguments.length; i++) {
      suma += arguments[i];
  }
  return suma;
}

let resultado = sumarConArguments(5, 10, 15, 20);
console.log("La suma de los números es:", resultado);
