from fastapi import FastAPI, Request, responses

app = FastAPI()

fake_db = {
    "data":
    [{
        "name": "",
        "phone": "902346829",
        "activity": "",
        "joined": 897643289,
        "history": [
            {
                "date": 6781982376,
                "complain": "",
            }
        ]
    },
        {
            "name": "",
            "activity": "",
            "joined": 897643289,
            "history": [
                {
                    "date": 6781982376,
                    "complain": "",
                }
            ]
        }, {
        "name": "",
        "activity": "",
        "joined": 897643289,
        "history": [
            {
                "date": 6781982376,
                "complain": "",
            }
        ]
    }

    ]
}


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

    user = {}

    for i in fake_db.get("data"):
        if i.get("phone") == str(phone_number):
            user = i
            print(i)
            break



    # # if phone_number in fake_db.get("data"):
    # for i in fake_db.get("data"):
    #     if i["phone"] == str(phone_number):
    #         user = i
    #         break

    # if user:
    if text == "":
        return str("CON welcome\n please send 1")
    elif text == "1":
        return "END welldone you can read english"
    else:
        return "END dimwit"
    # else:
    #     return str("CON welcome\n what is your name")


# a = 0
# b = ""
# c = []
# d = {}
# e = ()