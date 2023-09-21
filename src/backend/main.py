from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from authorization.router import router as auth_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=[
            "GET",
            "PUT",
            "POST",
            "PATCH",
            "DELETE",
            "OPTIONS"
        ],
        allow_headers=[
            "Set-Cookie",
            "Content-Type",
            "Authorization"
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin"
        ]
    )
    # application.add_middleware(
    #     middleware.ContextMiddleware,
    #     plugins=(plugins.ForwardedPlugin())
    # )
    application.include_router(auth_router)
    return application


app = get_application()
