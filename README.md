# Demo APP — Frontend & Backend
*(Repositorio de aplicación / CI )*

## Descripción

Este repositorio contiene el **código de la app**, compuesto por:
- un frontend
- un backend

También incluye los **pipelines de CI** responsables de construir y publicar las imágenes de contenedor.

## Responsabilidad del repositorio

- Contener el código fuente
- Construir imágenes Docker
- Publicar imágenes en GitHub Container Registry (GHCR)

**Este repositorio no despliega aplicaciones al cluster.**

## Estructura del repositorio

```
demo-app/
├── dev/
│ ├── front/
│ └── back/
├── test/
│ ├── front/
│ └── back/
└── .github/
└── workflows/
```
- `dev` y `test` representan variantes de build por ambiente
- Los workflows de GitHub Actions se activan al hacer merge a `main`

## CI (GitHub Actions)

Los pipelines:
1. Construyen la imagen Docker
2. Etiquetan la imagen (`*-dev` o `*-test`)
3. Publican la imagen en GHCR

## Despliegue

El despliegue **no ocurre en este repositorio**.

La definición del despliegue y la promoción de versiones se realiza en el repositorio **demo-argo-platform**

## Resumen

Este repositorio se enfoca exclusivamente en **build y publicación de artefactos**.
