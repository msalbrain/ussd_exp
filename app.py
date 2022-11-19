from fastapi import FastAPI, Request, responses

app = FastAPI()


@app.get("/test")
def check():
    return {"msg": "hello there bro"}


@app.post("/app", response_class=responses.PlainTextResponse)
async def index(request: Request):
    form = await request.form()
    session_id = form["sessionId"]
    serviceCode = form["serviceCode"]
    phone_number = form["phoneNumber"]
    text = form["text"]

    if text == "":
        return str("CON welcome\n please send 1")
    elif text == "1":
        return "END welldone you can read english"
    else:
        return "END dimwit"



