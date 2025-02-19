
# Python - Examen
Desarrollo de examen asignado por el profesor pedro relacionado a compañia de movistar....

## Tabla de contenidos
| Indice | Titulo  |Descripcion|
|--|--|--|
| 1 |  [MenuPrincipal.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/MenuPrincipal.py "MenuPrincipal.py")| Script en Python que gestiona el menú principal del sistema, permitiendo la navegación entre los diferentes módulos.
| 2 | [ModuloAd.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/ModuloAd.py "ModuloAd.py") |Módulo en Python que maneja las funciones administrativas, como la gestión de usuarios, permisos y configuraciones del sistema.
| 3 | [ModuloBonificacion.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/ModuloBonificacion.py "ModuloBonificacion.py")|Módulo en Python encargado de gestionar las bonificaciones, descuentos o incentivos aplicados a los clientes o usuarios.
| 4 | [ModuloCliente.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/ModuloCliente.py "ModuloCliente.py") |Módulo en Python que maneja la información de los clientes, incluyendo su registro, consulta y actualización de datos.
| 5 | [Moduloservicio.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/Moduloservicio.py "Moduloservicio.py") |Módulo en Python que gestiona los servicios ofrecidos, permitiendo su administración y asignación a los clientes.
| 6 | [Usuarios.json](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/Usuarios.json "Usuarios.json") |Archivo JSON que almacena la información de los usuarios del sistema, incluyendo credenciales y roles.
| 7 |  [clientes.json](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/clientes.json "clientes.json") |Archivo JSON que almacena los datos de los clientes, como nombres, contactos y servicios adquiridos.
| 8 |  [menu.py](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/menu.py "menu.py")| Script en Python que maneja un menú dentro del sistema, posiblemente complementario al menú principal.
| 9 | [reportes.json](https://github.com/AuraCamilaPicoAraque/Examen_Python_PicoAura/blob/master/reportes.json "reportes.json")  |Archivo JSON donde se almacenan los reportes generados, incluyendo estadísticas, análisis y datos relevantes sobre clientes y servicios.


### Instalaciones 

Deberás ejecutar este comando para descargar el repositorio:

```bash
git clone <repositorio>

```


## Y para poder ejecutarlo en el visual studio se debe colocar :

```bash
python3 <nombre>.py
```

en caso de que quieras ejecutar un .json , no se podra ya que no saldra nada para ejecutar 




## Errores

Si da la casualidad de que estas en windows y no te deja ejecutar los archivos .py  puede ser porque no tienes instalado el python.org 



## Explicación github.

Para poder subir a la nube este repositorio:

`Terminal :  Ctrl + Alt + T `

* 1-  Debemos iniciar con el  ` git init `  = ¿Porque? __ pues iniciamos un git vaco para que podamos subirlo al local.

* 2- Partiendo de ahí pondremos nuestros datos para subir a la nube   ` git config --global user.email "(gmail)"` para colocar nuestro gmail vinculado al github y seguido también nuestro nombre  ` git config --global user.name "(nombre)"`

* 3- Ingresado nuestro gmail y nombre proseguimos a poner nuestro repositorio que seria de la siguiente manera : ` git remote add origin (link del repositorio)`

* Un ejemplo seria: ` git remote add origin https://github.com/AuraCamilaPicoAraque/Python_S1_PicoAura`
* listo ahora tenemos que confirmar si tenemos nuestros archivos en la carpeta ..   ` git status `
* teniendo esos archivos los agregaremos con  ` git add . `
* Y le ponemos  ` git commit -m "(descripcion que quieras)" `  esto para tener un registro de el proceso que llevamos con los commits
* Ahora si todo va bien tendrías que mandarlo a la nube estando en  local , lo haremos de la siguiente manera :    ` git push origin master `
* Ahora saldrá un menú para que pongas tu usuario de nombre de github ... tendrás que ponerlo 
* Y ahora viene una parte fundamental ... te va a salir otro menú que te dirá que pongas tu contraseña esa sera la que tendrás en github.
* Para sacarla tendrías que meterte  [aqui~](https://github.com/settings/apps) y darle en  ` personal access tokens `  al terminar de darle click le das a `tokens(classic)` 
* Ahora estará vació , aquí le tienes que dar en `generate new token` y le tienes que dar en `Generate new token (classic)`.
* Y listo le pones las opciones que quieres la mas recomendada es `repo`  y ahí te sale un código el cual copias y pegas en lo que te pide en la termina.
* Listo ahora ya estaría subido al repositorio , debes actualizar la pestaña para que te salga

ÉXITOSSSSSSSSSS...


## Repositorio...

Este repositorio fue hecho y desarrollado por [ AuraCamilaPicoAraque ](https://github.com/AuraCamilaPicoAraque)
