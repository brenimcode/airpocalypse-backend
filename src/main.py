from fastapi import FastAPI


api = FastAPI()

@api.get('/')
def home():
    return {'message': 'HELLO WORLD!!'}

if __name__ == '__main__':
    import uvicorn
    port = 8080
    uvicorn.run(api, host="0.0.0.0", port=port) 