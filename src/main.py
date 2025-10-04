from fastapi import FastAPI


api = FastAPI()


@api.get('/')
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    import uvicorn
    port = 8000
    uvicorn.run(api, host="0.0.0.0", port=port)