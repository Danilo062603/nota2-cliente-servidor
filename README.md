# Proyecto Cliente-Servidor – Programación Web

## Descripción

Este proyecto implementa una **arquitectura cliente-servidor** usando Python para el servidor y HTML + JavaScript para el cliente.
El sistema permite obtener datos desde un servidor mediante una API y mostrarlos en el navegador.

El servidor maneja solicitudes HTTP y responde con información en formato **JSON**, que luego es procesada por el cliente.

---

## Tecnologías utilizadas

* Python
* HTTPServer
* HTML
* JavaScript
* JSON
* Git y GitHub

---

## Estructura del proyecto

```
nota2-cliente-servidor
│
├── servidor.py        # Servidor HTTP en Python
├── index.html         # Interfaz del cliente
├── cliente.js         # Lógica del cliente
├── README.md          # Documentación del proyecto
│
└── docs
    └── arquitectura.png   # Diagrama del sistema
```

---

## Arquitectura del sistema

El proyecto sigue el modelo **Cliente → Servidor → API → Respuesta JSON**

```
Navegador (Cliente)
        │
        │ HTTP Request
        ▼
Servidor Python
        │
        │ API /datos
        ▼
Respuesta JSON
        │
        ▼
Cliente muestra la información
```

### Diagrama

![Arquitectura](docs/arquitectura.png)

---

## Cómo ejecutar el proyecto

### 1 Clonar el repositorio

```
git clone https://github.com/Danilo062603/nota2-cliente-servidor.git
```

### 2 Entrar al proyecto

```
cd nota2-cliente-servidor
```

### 3 Ejecutar el servidor

```
python servidor.py
```

### 4 Abrir en el navegador

```
http://localhost:8000
```

---

## Funcionamiento

1. El cliente abre la página web.
2. JavaScript realiza una solicitud al servidor.
3. El servidor procesa la solicitud.
4. Se envía una respuesta en formato JSON.
5. El cliente muestra la información en la página.

---

## Autores

Danilo ramirez perez
Luis David correa riofrio
Julian Ramirez velez
carlos andres arroyave herrera
Proyecto académico – Programación Web
