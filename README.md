# Desarrollo de una API REST para gestión de usuarios

El equipo de desarrollo de una fintech necesita una API REST para gestionar usuarios. La API debe permitir el registro, autenticación y consulta de usuarios. Los usuarios se almacenarán en una base de datos relacional. La autenticación se realizará mediante JWT. Los actores involucrados son: 'usuario', 'administrador', 'base de datos'. Las propiedades operativas incluyen:'registro de usuario idempotente', 'autenticación segura', 'consulta de usuario eficiente'. Los umbrales numéricos son: '1 000 solicitudes/segundo en hora pico'. La razón de negocio es: 'facilitar la gestión de usuarios para mejorar la experiencia del cliente'.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python FastAPI |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Registro de usuarios

**Objetivo:** Implementar la funcionalidad de registro de usuarios de manera idempotente.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Diseñar la estructura de datos para los usuarios.
- Implementar la funcionalidad de registro de usuarios asegurándote de que sea idempotente.
- Definir los criterios de aceptación para el registro de usuarios.

**Entregable:** Servicio que permite el registro idempotente de usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejarías dos solicitudes de registro con los mismos datos.
- Piensa en cómo validarías la unicidad del nombre de usuario.

</details>

### Fase 2: Autenticación de usuarios

**Objetivo:** Implementar la autenticación de usuarios mediante JWT.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Diseñar la estructura de datos para los tokens JWT.
- Implementar la funcionalidad de autenticación de usuarios utilizando JWT.
- Definir los criterios de aceptación para la autenticación de usuarios.

**Entregable:** Servicio que permite la autenticación de usuarios mediante JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejarías la expiración de los tokens JWT.
- Piensa en cómo protegerías la información sensible en los tokens.

</details>

### Fase 3: Consulta de usuarios

**Objetivo:** Implementar la funcionalidad de consulta de usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Diseñar la estructura de datos para la consulta de usuarios.
- Implementar la funcionalidad de consulta de usuarios.
- Definir los criterios de aceptación para la consulta de usuarios.

**Entregable:** Servicio que permite la consulta eficiente de usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo optimizarías la consulta para manejar un alto volumen de solicitudes.
- Piensa en cómo manejarías los errores de consulta.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un registro idempotente de usuarios y por qué es importante en este contexto?
- **paraQueSirve**: ¿Para qué sirve la autenticación mediante JWT en la gestión de usuarios?
- **comoSeUsa**: ¿Cómo se usa la consulta de usuarios en la API REST?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir durante el registro, autenticación y consulta de usuarios?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de una API REST para gestión de usuarios?

## Criterios de Evaluacion

- Implementar el registro idempotente de usuarios.
- Implementar la autenticación de usuarios mediante JWT.
- Implementar la consulta eficiente de usuarios.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
