from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, RedirectResponse
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")


# define a lifespan method for fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

   


DEBUG = True


app = FastAPI(
    title="Langfuse", 
    version="0.0.1",
    description="Test Langfuse", 

    debug=DEBUG,
    openapi_url="/api/openapi.json" if DEBUG else None,
    docs_url="/api/docs" if DEBUG else None,
    redoc_url="/api/redoc" if DEBUG else None,
    swagger_ui_oauth2_redirect_url="/api/docs/oauth2-redirect" if DEBUG else None,

    contact={"name": "Qutaiba Olayyan", "url": "https://www.linkedin.com/in/qutaiba-olayyan/", 'email': "qutaibaolayyan@gmail.com"}, 
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},

    # important: this will make the endpoint to accept the path with or without "/"
    # ignore_trailing_slash=True, # not supported yet, now use core/router.py
    lifespan=lifespan, 
    dependencies=[],
    default_response_class=ORJSONResponse,
)






# CORS settings.FRONTEND_URLS,
origins = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/api/docs")

@app.get("/api", include_in_schema=False)
async def api_root():
    return RedirectResponse(url="/api/docs")




from langfuse.callback import CallbackHandler
from langchain_openai import ChatOpenAI


langfuse_handler = CallbackHandler(
    public_key=LANGFUSE_PUBLIC_KEY,
    secret_key=LANGFUSE_SECRET_KEY,
    host=LANGFUSE_HOST,
    session_id="test_session",
    user_id="test_user",
    metadata={"test_field": "test_data"},
    trace_name="test_trace_name",
    tags=["test", "langfuse"],


)
 

def test():
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model="gpt-4o-mini"
    )
    # Add Langfuse handler as callback (classic and LCEL) 
    return llm.invoke("I want to test you", config={"callbacks": [langfuse_handler]})
 

@app.get("/api/test")
async def test_api():
    return test()
    