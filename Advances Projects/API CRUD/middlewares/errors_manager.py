from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse


class ErrorManager(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except ValueError as e:
            return JSONResponse(status_code=400, content={"error": "Bad request: " + str(e)})
        except KeyError as e:
            return JSONResponse(status_code=400, content={"error": "Bad request: " + str(e)})
        except TypeError as e:
            return JSONResponse(status_code=400, content={"error": "Bad request: " + str(e)})
        except IndexError as e:
            return JSONResponse(status_code=400, content={"error": "Bad request: " + str(e)})
        except FileNotFoundError as e:
            return JSONResponse(status_code=404, content={"error": "File not found: " + str(e)})
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": "An internal error occurred: " + str(e)})