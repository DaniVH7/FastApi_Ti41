Create database contactos
use contactos;
Create table  if not exists contactos(
    id_contacto int primary key Autoincrement,
    nombre varchar(250),
    email varchar(250),
    telefono varchar(10)
);