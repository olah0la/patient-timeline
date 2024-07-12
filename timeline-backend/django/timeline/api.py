from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/timeline")
def timeline(request):
    return {"message": "Hello, world!"}

@api.get("/appointments")
def appointments(request):
    return {"message": "Hello, world!"}