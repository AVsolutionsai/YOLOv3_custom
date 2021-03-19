
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--<a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h3 align="center">YOLOv3-CustomTraining-Template</h3>

  <p align="center">
    Entrenamiento customizado para entrenamiento de YOLOv3 y YOLOv3-tiny
    <br />
    <a href="https://github.com/AVsolutionsai/YOLOv3_custom"><strong>Explorar Documentos»</strong></a>
    <br />
    <br />
    <!--<a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>-->
    ·
    <a href="https://github.com/AVsolutionsai/YOLOv3_custom/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/AVsolutionsai/YOLOv3_custom/issues">Pedir una Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Contenido</summary>
  <ol>
    <li>
      <a href="#Proyecto">Proyecto</a>
      <ul>
        <li><a href="#Construir">Construcción</a></li>
      </ul>
    </li>
    <li>
      <a href="#Empezar">Empezar</a>
      <ul>
        <!--<li><a href="#Pre-requisitos">Pre-requisitos</a></li>-->
        <li><a href="#Requisitos">Requisitos</a></li>
      </ul>
    </li>
    <li>
      <a href="#Ejecución">Ejecución</a>
      <ul>
        <!--<li><a href="#Pre-requisitos">Pre-requisitos</a></li>-->
        <li><a href="#base-de-datos">Base de Datos</a></li>
        <li><a href="#entrenamiento-de-YOLOv3">Entrenamiento de YOLOv3</a></li>
        <li><a href="#Visualización-de-Detección">Visualización de Detección</a></li>
      </ul>
    </li>
    <!--<li><a href="#Ejemplos">Ejemplos</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>-->
    <li><a href="#Contacto">Contacto</a></li>
    <!--<li><a href="#Reconocimientos">Reconocimientos</a></li>-->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Proyecto

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

En este proyecto se llevan a cabo 3 principales acciones:
- Creación de base de datos para el entrenamiento de YOLOv3 o YOLOv3-tiny.
- Entrenamiento de la red YOLOv3.
- Visualización de detecciones con la red entrenada.

### Construir

Este proyecto fue testeado con las siguientes dependencias.
* [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
* [Tensorflow 2.1.2](https://www.tensorflow.org/install/pip?hl=es-419)


<!-- GETTING STARTED -->
## Empezar
Para comenzar este proyecto, es necesario clonarlo seguir los siguientes pasos:

### Requisitos

1. Clonar el repositorio en un ambiente virtual
   ```sh
   git clone https://github.com/AVsolutionsai/YOLOv3_custom.git
   ```
2. Instalar requerimientos en ambiente virtual
   ```sh
   pip install -r requirements-gpu.txt
   ```
3. Descargar los pesos para crear la Base de Datos para entrenar YOLOv3 del siguiente link, una vez descargado el modelo, pasarlo a la carpeta *create_dataset* del proyecto:
* [Pesos VGG16](https://drive.google.com/drive/folders/1JvGF7UOImLokG-cmV5yiOcz3ZgEqN1px)

4. Descargar los archivos *yolov3_custom.cfg* y *obj.names* para la visualización con *dnn* del siguiente link, una vez descargados, pasarlos a la carpeta *dnn*:
* [Archivos de configuración YOLOv3](https://drive.google.com/drive/u/1/folders/13jZwASuPZuLl_3i4vyrlan-HV0Q9itWp)


<!-- USAGE EXAMPLES -->
## Ejecución
### Base de Datos
Comenzaremos en la carpeta *create_database*, en donde tendremos 3 archivos:
- get_data_yolo.py
- main_get_data_yolo.py
- modelo-280.. (previamente descargado)

Una vez abierto el archivo *main_get_data_yolo.py* es necesario cambiar el *nombre_de_archivo.mp4* que debe encontrarse en la carpeta *data/video*.
Después, podemos ejecutar este archivo.
Nos creará una carpeta dentro de este mismo *path* llamada *Obj*, en donde encontraremos todos los archivos *.jpg* y *.txt* necesarios para entrenar YOLOv3.

### Entrenamiento de YOLOv3
Entrar al siguiente Google Colab para comenzar el entrenamiento de YOLOv3, seguir los pasos indicados:
* [Entrenamiento de YOLOv3](https://drive.google.com/file/d/1XNp6KhcoY7-lsk891Slj7wn-J7tLyq3m/view?usp=sharing)

### Visualización de Detección
Se cuentan con dos opciones para visualizar la detección de la red YOLOv3:
- Utilizando OpenCv: 
  - Abrir el archivo ***test_yolo.py*** que se encuentra en la carpeta *dnn* y cambiar los *paths* al modelo entrenado de YOLOv3, que debe encontrarse en la carpeta *weights* 
  y haber descargado los archivos *yolov3_custom.cfg* y *obj.names*, deben encontrarse en este folder.
  - Cambiar el *path* del video a evaluar, debe encontrarse en la carpeta *data/video*.
 - Utilizando Tensorflow-gpu:
    - Es necesario convertir los pesos antes de utilizarlos, para ello, escribimos en consola lo siguiente:
    ```sh
      python load_weights.py --weights ./weights/yolov3_custom_last.weights --output ./weights/yolov3.tf
    ```
    Es necesario que se encuentre el archivo a convertir dentro de la carpeta *weights*, como resultado obtendremos el modelo convertido a *.tf* dentro de esta misma carpeta.
    - Una vez obtenido el modelo en *.TF*, escribir en consola:
    ```sh
      python detect_video.py --video data/video/<nombre_de_archivo>.mp4 --weights ./weights/yolov3.tf
    ```
    Se puede utilizar la bandera *--output ./detections/output.avi* para guardar el video con la detección dentro de la carpeta *detections*

<!--
_For more examples, please refer to the [Documentation](https://example.com)_
-->


<!-- ROADMAP 
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).
-->


<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
-->


<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE` for more information.-->



<!-- CONTACT -->
## Contacto

Isaac R. Aguilar Figueroa - [Isaac Aguilar](https://www.linkedin.com/in/isaac-rene-aguilar-figueroa-b5b2438b/) - isaac.aguilar@alumnos.udg.mx

J. Vladimir Martínez Nuño - [Vladimir Martínez](www.linkedin.com/in/vladimir-martinez-nuno) - vladimir.martinez@alumnos.udg.mx

Project Link: [YOLOv3_custom](https://github.com/AVsolutionsai/YOLOv3_custom)



<!-- ACKNOWLEDGEMENTS 
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)-->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!--
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->
