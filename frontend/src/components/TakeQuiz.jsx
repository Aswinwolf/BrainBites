import { useState, useRef, useEffect } from "react";

/* ---------- Helpers ---------- */
const cleanText = (text) => {
  if (!text) return "";
  return text.replace(/\\n/g, "").trim();
};

const normalize = (text) =>
  cleanText(text)
    .toLowerCase()
    .replace(/[^\w\s]/g, "")
    .trim();

/* ---------- Component ---------- */
export default function TakeQuiz({ quiz }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const resultRef = useRef(null);

  /* ---------- Reset when new quiz comes ---------- */
  useEffect(() => {
    setAnswers({});
    setSubmitted(false);
  }, [quiz]);

  /* ---------- Handlers ---------- */
  const handleSelect = (qid, option) => {
    setAnswers((prev) => ({ ...prev, [qid]: option }));
  };

  const handleSubmit = () => {
    setSubmitted(true);

    // Auto scroll to result section
    setTimeout(() => {
      resultRef.current?.scrollIntoView({ behavior: "smooth" });
    }, 100);
  };

  /* ---------- SCORING (ROBUST) ---------- */
  const score = quiz.questions.reduce((acc, q) => {
    const userAns = normalize(answers[q.id] || "");
    const correctAns = normalize(q.correct_answer || "");

    if (userAns && userAns === correctAns) acc++;
    return acc;
  }, 0);

  /* ---------- RESULT VIEW ---------- */
  if (submitted) {
    return (
      <div className="result-box" ref={resultRef}>
        <h2>Quiz Result</h2>
        <p>
          You scored <b>{score}</b> out of{" "}
          <b>{quiz.questions.length}</b>
        </p>

        <div className="result-list">
          {quiz.questions.map((q, index) => {
            const userAns = answers[q.id] || "Not answered";

            // Detect AI inconsistency
            const isMismatch = !q.options.some(
              (opt) =>
                normalize(opt) === normalize(q.correct_answer)
            );

            return (
              <div key={q.id} className="result-item">
                <p>
                  <b>
                    Q{index + 1}. {cleanText(q.question)}
                  </b>
                </p>

                <p>
                  Your answer:{" "}
                  {cleanText(userAns)}
                </p>

                <p>
                  Correct answer:{" "}
                  {isMismatch ? (
                    <span style={{ color: "orange" }}>
                      {cleanText(q.correct_answer)} (AI mismatch)
                    </span>
                  ) : (
                    cleanText(q.correct_answer)
                  )}
                </p>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  /* ---------- QUIZ VIEW ---------- */
  return (
    <div>
      <h2>{quiz.quiz_title}</h2>

      {quiz.questions.map((q, index) => (
        <div key={q.id} className="mcq-card">
          <h3 className="mcq-question">
            Q{index + 1}. {cleanText(q.question)}
          </h3>

          <div className="mcq-options">
            {q.options.map((opt, i) => (
              <label key={i} className="mcq-option">
                <input
                  type="radio"
                  name={`q-${q.id}`}
                  value={opt}
                  checked={answers[q.id] === opt}
                  onChange={() =>
                    handleSelect(q.id, opt)
                  }
                />
                <span>{cleanText(opt)}</span>
              </label>
            ))}
          </div>
        </div>
      ))}

      <button
        className="submit-btn"
        onClick={handleSubmit}
      >
        Submit Quiz
      </button>
    </div>
  );
}
