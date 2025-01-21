import os
import subprocess
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "templates")), name="static")

output_dir = "csvs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process/")
def process_csv(request: Request, start_row: int = Form(...), end_row: int = Form(...), input_file: UploadFile = File(...), output_file: str = Form(...)):
    try:

        temp_input_path = f"csvs/{input_file.filename}"
        with open(temp_input_path, "wb") as f:
            f.write(input_file.file.read())

        # Comando PowerShell para cortar el CSV
        output_filepath = os.path.join(output_dir, f"{output_file}.csv")
        ps_command = f"Get-Content {temp_input_path} | Select-Object -Skip {start_row} | Select-Object -First {end_row-start_row} | Set-Content {output_filepath}"

        subprocess.run(["powershell", "-Command", ps_command], check=True)

        return templates.TemplateResponse("index.html", {"request": request, "output_path": output_filepath})
    
    except Exception as e:
        return {"error": str(e)}
