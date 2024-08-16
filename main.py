from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import calendar
import datetime

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

registros = {
    "2024-06-27": {
        "exercises": ["Corrida - 5km", "Abdominais - 3 séries de 20"],
        "meals": ["Café da manhã: Aveia com frutas", "Almoço: Salada com frango", "Jantar: Sopa de legumes"]
    },
}

alimentacao = {
    "2024-06-27": {
        "meta_carboidratos": 300,
        "meta_proteinas": 150,
        "meta_gorduras": 70,
        "meta_kcal": 2000
    },
}

@app.get("/")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("index.html", view_model)

@app.get("/planos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("planos.html", view_model)

@app.get("/suporte")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("suporte.html", view_model)

@app.get("/termos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("termos.html", view_model)

@app.get("/politicadeprivacidade")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("politicadeprivacidade.html", view_model)

@app.get("/painelcliente")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("painelcliente.html", view_model)

@app.get("/perfil")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("perfil.html", view_model)

@app.get("/calendario", response_class=HTMLResponse)
async def read_calendario_current(request: Request):
    today = datetime.date.today()
    year = today.year
    month = today.month
    return RedirectResponse(url=f"/calendario/{year}/{month}")

@app.get("/calendario/{year}/{month}", response_class=HTMLResponse)
async def read_calendario(request: Request, year: int, month: int):
    try:
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        view_model = {
            "request": request,
            "year": year,
            "month": month,
            "month_days": month_days,
            "calendar": calendar,
        }
        return templates.TemplateResponse("calendario.html", view_model)
    except calendar.IllegalMonthError:
        raise HTTPException(status_code=400, detail="Month must be in 1..12")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dia/{date}", response_class=HTMLResponse)
async def read_dia(request: Request, date: str):
    details = registros.get(date, {"exercises": [], "meals": []})
    view_model = {
        "request": request,
        "date": date,
        "details": details
    }
    return templates.TemplateResponse("dia_detalhe.html", view_model)

@app.get("/alimentacao", response_class=HTMLResponse)
async def get_alimentacao(request: Request, day: str = None):
    today = datetime.date.today().isoformat()
    if not day:
        day = today
    
    view_model = {
        "request": request,
        "day": day,
        **alimentacao.get(day, {})
    }
    return templates.TemplateResponse("alimentacao.html", view_model)

@app.get("/api/alimentacao", response_class=JSONResponse)
async def get_alimentacao_api(day: str = None):
    today = datetime.date.today().isoformat()
    if not day:
        day = today
    return alimentacao.get(day, {})

@app.get("/exercicios")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("exercicios.html", view_model)

@app.get("/artigos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("artigos.html", view_model)

@app.get("/configuracoes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("configuracoes.html", view_model)

@app.get("/contato")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("contato.html", view_model)

@app.get("/sobre")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("sobre.html", view_model)

@app.get("/professores")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("professores.html", view_model)

@app.get("/perguntasfrequentes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("perguntasfrequentes.html", view_model)

@app.get("/mensagens")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("mensagens.html", view_model)

@app.get("/estatisticas")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("estatisticas.html", view_model)

@app.get("/dieta")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("dieta.html", view_model)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)














