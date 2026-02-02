from fastapi import FastAPI, HTTPException, Query, Body

app = FastAPI(title="Task Service API")

@app.get("/")
def home():
    return {"message": "Welcome to the Task Service API"}

#Read all
@app.get("/tasks/")
def get_tasks():
    pass

#Read with Query Params
@app.get("/tasks/search/")
def search_tasks(query: str | None = Query(default=None, description="Search query")):
    pass

#Read with ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass

#Create
@app.post("/tasks/")
def create_task(task: dict = Body(...)):
    pass

#Update
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict = Body(...)):
    pass

#Delete
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass
