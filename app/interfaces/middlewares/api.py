from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware
import logging
import openai

logger = logging.getLogger("uvicorn.error")
class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemy error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Error en la base de datos.", "error": str(e)}
            )
        except HTTPException as http_ex:
            logger.error(f"HTTP error: {str(http_ex.detail)}")
            return JSONResponse(
                status_code=http_ex.status_code,
                content={"detail": http_ex.detail}
            )
        except openai.APIConnectionError as e:
            logger.error("Error de conexión a la API.")
            return JSONResponse(
                status_code=503,
                content={"detail": "Error de conexión a nuestros servicios.", "error": str(e)}
            )
        except openai.APITimeoutError as e:
            logger.error("Tiempo de espera de la API excedido.")
            return JSONResponse(
                status_code=504,
                content={"detail": "La solicitud ha superado el tiempo de espera. Intenta de nuevo más tarde.", "error": str(e)}
            )
        except openai.AuthenticationError as e:
            logger.error("Error de autenticación.")
            return JSONResponse(
                status_code=401,
                content={"detail": "La clave de API o token es inválido, expirado o revocado.", "error": str(e)}
            )
        except openai.BadRequestError as e:
            logger.error(f"Solicitud incorrecta: {str(e)}")
            return JSONResponse(
                status_code=400,
                content={"detail": "La solicitud está mal formada o falta algún parámetro requerido.", "error": str(e)}
            )
        except openai.ConflictError as e:
            logger.error("Conflicto en la actualización del recurso.")
            return JSONResponse(
                status_code=409,
                content={"detail": "El recurso fue actualizado por otra solicitud.", "error": str(e)}
            )
        except openai.InternalServerError as e:
            logger.error("Error interno del servidor.")
            return JSONResponse(
                status_code=500,
                content={"detail": "Error en nuestro lado. Intenta de nuevo más tarde.", "error": str(e)}
            )
        except openai.NotFoundError as e:
            logger.error("Recurso no encontrado.")
            return JSONResponse(
                status_code=404,
                content={"detail": "El recurso solicitado no existe.", "error": str(e)}
            )
        except openai.PermissionDeniedError as e:
            logger.error("Permiso denegado.")
            return JSONResponse(
                status_code=403,
                content={"detail": "No tienes acceso al recurso solicitado.", "error": str(e)}
            )
        except openai.RateLimitError as e:
            logger.error("Límite de tasa alcanzado.")
            return JSONResponse(
                status_code=429,
                content={"detail": "Has alcanzado tu límite de tasa. Espacia tus solicitudes.", "error": str(e)}
            )
        except openai.UnprocessableEntityError as e:
            logger.error("Entidad no procesable.")
            return JSONResponse(
                status_code=422,
                content={"detail": "No se pudo procesar la solicitud a pesar de que el formato es correcto.", "error": str(e)}
            )
        except openai.RateLimitError as e:
                    raise HTTPException(status_code=429, detail="Excediste tu cuota de uso. Por favor verifica tu plan y detalles de facturación.")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Error interno del servidor.", "error": str(e)}
            )