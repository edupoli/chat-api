from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.userController import router

app = FastAPI(
    title="API chatbot",
    version="1.0",
    description="API para chatbots com Inteligencia Artificial",
    openapi_url="/api/v1/openapi.json",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)