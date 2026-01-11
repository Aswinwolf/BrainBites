import os
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from prompts.quiz_prompt import QUIZ_PROMPT_TEMPLATE


def clean_text(text: str) -> str:
    if not text:
        return ""
    # remove newlines + extra spaces
    return " ".join(text.replace("\n", " ").split()).strip()


def sanitize_quiz_output(quiz_data: dict) -> dict:
    for q in quiz_data["questions"]:

        # clean main fields
        q["question"] = clean_text(q.get("question"))
        q["difficulty"] = clean_text(q.get("difficulty"))
        q["explanation"] = clean_text(q.get("explanation"))

        # clean options
        q["options"] = [clean_text(o) for o in q.get("options", [])]

        # clean topics + remove garbage
        clean_topics = []
        for t in q.get("related_topics", []):
            t = clean_text(t)
            # ignore metadata / junk
            if t and not t.lower().startswith(("extras", "{", "[")):
                clean_topics.append(t)
        q["related_topics"] = clean_topics

        # fix missing correct answer
        if not q.get("correct_answer"):
            # fallback: first option
            q["correct_answer"] = q["options"][0] if q["options"] else ""

        else:
            q["correct_answer"] = clean_text(q["correct_answer"])

    return quiz_data


def generate_quiz(article_data: dict, num_questions: int = 5):

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = PromptTemplate(
        template=QUIZ_PROMPT_TEMPLATE,
        input_variables=["num_questions", "title", "summary", "sections"]
    )

    final_prompt = prompt.format(
        num_questions=num_questions,
        title=article_data["title"],
        summary=article_data["summary"],
        sections=article_data["sections"]
    )

    # ---- CALL GEMINI ----
    response = llm.invoke(final_prompt)

    # ---- get text safely ----
    if isinstance(response.content, list):
        text = " ".join(str(p) for p in response.content)
    else:
        text = str(response.content)

    text = text.strip()

    # ---- keep only from first QUESTION ----
    idx = text.find("QUESTION:")
    if idx != -1:
        text = text[idx:]

    # -------- PARSER USING REGEX --------
    question_blocks = re.split(r"QUESTION:\s*", text)[1:]
    questions = []

    for i, block in enumerate(question_blocks, start=1):

        # Question text = everything before first A:
        q_match = re.search(r"^(.*?)(?=A:)", block, re.S)
        question_text = q_match.group(1).strip() if q_match else block.strip()

        def grab(pattern):
            m = re.search(pattern, block, re.S)
            return m.group(1).strip() if m else ""

        option_a = grab(r"A:\s*(.*?)(?=B:)")
        option_b = grab(r"B:\s*(.*?)(?=C:)")
        option_c = grab(r"C:\s*(.*?)(?=D:)")
        option_d = grab(r"D:\s*(.*?)(?=ANSWER:)")

        correct_letter = grab(r"ANSWER:\s*(.*?)(?=DIFFICULTY:)")
        difficulty = grab(r"DIFFICULTY:\s*(.*?)(?=EXPLANATION:)")
        explanation = grab(r"EXPLANATION:\s*(.*?)(?=TOPICS:)")
        topics_raw = grab(r"TOPICS:\s*(.*)")

        options = [option_a, option_b, option_c, option_d]

        if correct_letter.upper() in ["A", "B", "C", "D"]:
            correct_answer = options[ord(correct_letter.upper()) - 65]
        else:
            correct_answer = ""

        questions.append({
            "id": i,
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "difficulty": difficulty,
            "explanation": explanation,
            "related_topics": [t.strip() for t in topics_raw.split(",") if t.strip()]
        })

    raw_quiz = {
        "quiz_title": f"{article_data['title']} Quiz",
        "questions": questions
    }

    clean_quiz = sanitize_quiz_output(raw_quiz)

    return clean_quiz
