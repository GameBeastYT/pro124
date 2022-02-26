from asyncio import tasks
from flask import Flask, jsonify, request

app = Flask(__name__)
contactlist = [{"id":1, "Contact":"3924784895", "Name":"Charles", "done": False},
{"id":2, "Contact":"8450931065", "Name":"John", "done": False}]

@app.route("/add_data", methods = ["POST"])

def AddTask():
    if not request.json:
        return(jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 404))

    contact = {"id":contactlist[-1]["id"]+1, "Name":request.json["Name"], "Contact":request.json.get("Contact",""), "done": False}
    contactlist.append(contact)
    return(jsonify({
        "status": "success",
        "message": "Contact added successfully"
    }))

@app.route("/get_data")

def gettask():
    return(jsonify({
        "data": contactlist
    }))

if __name__ == "__main__":
    app.run()

