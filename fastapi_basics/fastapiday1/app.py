from fastapi import FastAPI, Response
ap=FastAPI()
@ap.get("/")
def hello():
    return {"message":"welcome to fastapi world"}
# to fiix the 404 error we need to add the favicon route so that the browser can find it
# @ap.get("/favicon.ico")
