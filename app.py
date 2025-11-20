from flask import Flask,render_template,request,jsonify,redirect,url_for
from datetime import datetime
app = Flask(__name__)


tasks=[]
@app.route("/",methods=["GET","POST"])
def to_do():
    return render_template("index.html",tasks=tasks,today=datetime.now().strftime('%Y-%m-%d'))


@app.route("/add",methods=["POST"])
def add_task():
    if request.method=="POST":
        task=request.form.get("task")
        datet=request.form.get("date")
        done=False
        if task  :
            id=len(tasks)+1
            tasks.append({"id":id,"task":task,"date":datet,"done":done})
    return redirect(url_for("to_do"))
    
    
@app.route("/action",methods=["POST","GET"])
def action():
    if request.method=="POST":
        action=request.form.get("action")
        id=int(request.form.get("task_id"))
        if action=="delete":
            tasks.pop(tasks.index(next(item for item in tasks if item["id"]==id)))
        if action=="complete":
            tasks[tasks.index(next(item for item in tasks if item["id"]==id))]["done"]=True    
    return redirect(url_for("to_do"))



if __name__ == '__main__' :
    app.run(debug=True)