# Actividad de Entrega — Moodle (Unidad IV · Semana 10)

## Parte A — Conceptual

### P1: ¿Qué significa JWT y cuáles son sus tres partes?
**JWT** significa *JSON Web Token*. Es un estándar abierto utilizado para transmitir información de forma segura entre partes como un objeto JSON. Consta de 3 partes separadas por puntos (`.`):
1. **Header:** Tipo de token (`JWT`) y el algoritmo de firma (`HS256`).
2. **Payload:** Contiene los datos del usuario y la sesión (`sub`, `role`, `exp`).
3. **Signature:** Firma digital creada con el Header, Payload y una `SECRET_KEY` para garantizar la integridad.

### P2: ¿Por qué el payload NO es seguro para guardar contraseñas?
El payload está codificado en **Base64Url**, por lo que **no está encriptado**. Cualquier usuario puede decodificarlo e inspeccionar su contenido en texto plano.

### P3: ¿Qué sucede si alguien modifica el payload sin conocer el SECRET_KEY?
La firma digital deja de coincidir al ser verificada por el servidor, ya que el servidor recalcula la firma con su `SECRET_KEY`. La petición es automáticamente rechazada por falta de integridad.

### P4: Diferencia entre 401 Unauthorized y 403 Forbidden. ¿Cuándo usa cada uno FastAPI?
* **401 Unauthorized:** Ocurre cuando falta la autenticación o el token es inválido/expirado. FastAPI lo lanza en la dependencia `get_current_user` o credenciales erróneas en `/login`.
* **403 Forbidden:** Ocurre cuando el usuario está autenticado pero no tiene permisos o el rol necesario. FastAPI lo lanza al intentar acceder a rutas restringidas sin el rol apropiado (ej. un usuario `estudiante` accediendo a `/admin`).

---

## Parte B — Práctica

### Capturas Swagger

#### 1. POST /login → 200 con token
![Login 200](capturas/1_login_200.png)

#### 2. GET /privado → 200 (Autenticado)
![Privado 200](capturas/2_privado_200.png)

#### 3. GET /admin → 403 (Rol estudiante)
![Admin 403](capturas/3_admin_403.png)
