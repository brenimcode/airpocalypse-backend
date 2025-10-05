from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import auth
from core.db import init_db
from routers import insights

description = """
    Backend API para aplicativo web de monitoramento da qualidade do ar.
     \n"
"""

app = FastAPI(
    description=description,
    title="Smart Athlete - Backend",
    version="1.0",
    contact={
        "name": "Breno Oliveira",
        "url": "https://brenooliveira.netlify.app/",
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)

app.include_router(auth.router, tags=["auth"])
app.include_router(insights.router, prefix="/insights", tags=["insights"])


@app.get('/')
def root():
    return RedirectResponse(url='/docs')

if __name__ == '__main__':
    import uvicorn
    port = 8080
    uvicorn.run(app, host="0.0.0.0", port=port) 