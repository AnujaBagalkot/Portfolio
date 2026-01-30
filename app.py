from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.assessment import get_questions, calculate_score

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# HOME PAGE
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ✅ TEST SELECTION PAGE
@app.get("/skill-assessment", response_class=HTMLResponse)
async def select_test(request: Request):
    return templates.TemplateResponse("select_test.html", {"request": request})


# ✅ QUIZ PAGE BY DOMAIN
@app.get("/skill-assessment/{domain}", response_class=HTMLResponse)
async def skill_assessment(request: Request, domain: str):

    questions = get_questions(domain)

    return templates.TemplateResponse(
        "skill_assessment.html",
        {"request": request, "questions": questions, "domain": domain}
    )


# ✅ SUBMIT QUIZ
@app.post("/submit-quiz/{domain}", response_class=HTMLResponse)
async def submit_quiz(request: Request, domain: str):

    questions = get_questions(domain)

    form = await request.form()

    user_answers = []
    for i in range(len(questions)):
        ans = form.get(f"q{i}")
        user_answers.append(ans)

    score = calculate_score(questions, user_answers)

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "score": score, "total": len(questions)}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
