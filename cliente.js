function cargarMascotas(){

fetch("http://localhost:8000/api/mascotas")

.then(res => res.json())

.then(data => {

document.getElementById("resultado").textContent =
JSON.stringify(data, null, 2)

})

.catch(error => console.log(error))

}