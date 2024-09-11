from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import calendar
import datetime
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Depends, HTTPException

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

app.add_middleware(SessionMiddleware, secret_key="supersecretkey")


user_data = {
    "email": "usuario@exemplo.com",
    "senha": "senha_antiga",
    "codigo_verificacao": "123456"
}

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

def common_view_params(request: Request, show_header=True, show_footer=True, show_sidebar=True):
    return {
        "request": request,
        "show_header": show_header,
        "show_footer": show_footer,
        "show_sidebar": show_sidebar
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
    return templates.TemplateResponse("planos.html", common_view_params(request))

@app.get("/suporte")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("suporte.html", common_view_params(request))

@app.get("/termos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("termos.html", common_view_params(request))

@app.get("/politicadeprivacidade")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("politicadeprivacidade.html", common_view_params(request))

@app.get("/painelcliente")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("painelcliente.html", common_view_params(request))

@app.get("/perfil")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("perfil.html", common_view_params(request))

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
        return templates.TemplateResponse("calendario.html", common_view_params(request))
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
    return templates.TemplateResponse("dia_detalhe.html", common_view_params(request))

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
    return templates.TemplateResponse("alimentacao.html", common_view_params(request))

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
    return templates.TemplateResponse("exercicios.html", common_view_params(request))

@app.get("/artigos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("artigos.html", common_view_params(request))

@app.get("/configuracoes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("configuracoes.html", common_view_params(request))

@app.get("/contato")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("contato.html", common_view_params(request))

@app.get("/sobre")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("sobre.html", common_view_params(request))

@app.get("/professores")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("professores.html", common_view_params(request))

@app.get("/perguntasfrequentes")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("perguntasfrequentes.html", common_view_params(request))

@app.get("/mensagens")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("mensagens.html", common_view_params(request))

@app.get("/estatisticas")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("estatisticas.html", common_view_params(request))

@app.get("/receitas")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("receitas.html", common_view_params(request))

@app.get("/sair")
def get_root(request: Request):
    # Redireciona para a página inicial (index.html)
    return RedirectResponse(url="/")

@app.get("/login")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("login.html", view_model)

@app.get("/inscrever")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("inscrever.html", view_model)

@app.get("/recuperar_senha", response_class=HTMLResponse)
async def get_recuperar_senha(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("esqueceu_sua_senha.html", view_model)

# Processar o envio do email para recuperação de senha (POST)
@app.post("/recuperar_senha", response_class=RedirectResponse)
async def post_recuperar_senha(request: Request, email: str = Form(...)):
    if email == user_data["email"]:
        request.session['email'] = email  # Salva o email na sessão
        return RedirectResponse(url="/verificar_codigo", status_code=302)
    else:
        raise HTTPException(status_code=404, detail="Email não encontrado")
    
@app.post("/enviar_codigo", response_class=RedirectResponse)
async def enviar_codigo(request: Request, email: str = Form(...)):
    if email == user_data["email"]:
        request.session['email'] = email  # Salva o email na sessão
        return RedirectResponse(url="/verificar_codigo", status_code=302)
    else:
        raise HTTPException(status_code=404, detail="Email não encontrado")

@app.get("/verificar_codigo", response_class=HTMLResponse)
async def get_verificar_codigo(request: Request):
    if 'email' not in request.session:
        return RedirectResponse(url="/recuperar_senha")
    
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("verificar_codigo.html", view_model)

@app.post("/verificar_codigo", response_class=RedirectResponse)
async def verificar_codigo(request: Request, codigo: str = Form(...)):
    if 'email' not in request.session:
        return RedirectResponse(url="/recuperar_senha")

    if codigo == user_data["codigo_verificacao"]:
        return RedirectResponse(url="/redefinir_senha", status_code=302)
    else:
        raise HTTPException(status_code=400, detail="Código incorreto")

@app.get("/redefinir_senha", response_class=HTMLResponse)
async def get_redefinir_senha(request: Request):
    if 'email' not in request.session:
        return RedirectResponse(url="/recuperar_senha")
    
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("redefinir_senha.html", view_model)

@app.post("/redefinir_senha", response_class=RedirectResponse)
async def redefinir_senha(request: Request, senha: str = Form(...)):
    if 'email' not in request.session:
        return RedirectResponse(url="/recuperar_senha")

    user_data['senha'] = senha  # Redefine a senha (simulação)
    del request.session['email']  # Remove o email da sessão
    return RedirectResponse(url="/login", status_code=302)

# Supondo que você tem uma função de autenticação
def authenticate_user(email: str, password: str):
    # Aqui iria sua lógica de autenticação
    return True  # Suponha que retorne True se autenticado corretamente

@app.post("/login")
async def post_login(request: Request, email: str = Form(...), senha: str = Form(...)):
    user_authenticated = authenticate_user(email, senha)
    if user_authenticated:
        return RedirectResponse(url="/perfil", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.post("/inscrever")
async def post_inscrever(request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...), profissao: str = Form(...)):
    # Aqui você adicionaria o usuário ao seu sistema
    return RedirectResponse(url="/perfil", status_code=303)

@app.get("/rotina")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("rotina.html", common_view_params(request))

@app.get("/explorarrotina")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("explorar_rotina.html", common_view_params(request))

@app.get("/treinamentovazio")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("treinamento_vazio.html", common_view_params(request))

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)














