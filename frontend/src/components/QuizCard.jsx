const cleanText = (text) => text?.replace(/\\n/g, "").trim();

export default function QuizCard({ question }) {
  return (
    <div className="mcq-card">
      <h3 className="mcq-question">
        {cleanText(question.question)}
      </h3>

      <div className="mcq-options">
        {question.options.map((opt, i) => (
          <label key={i} className="mcq-option">
            <input type="radio" name={`q-${question.id}`} disabled />
            <span>{cleanText(opt)}</span>
          </label>
        ))}
      </div>

      <div className="mcq-meta">
        <p>
          <b>Correct Answer:</b>{" "}
          {cleanText(question.correct_answer)}
        </p>
        <p>
          <b>Difficulty:</b>{" "}
          {cleanText(question.difficulty)}
        </p>
      </div>

      <details className="mcq-explanation">
        <summary>View Explanation</summary>
        <p>{cleanText(question.explanation)}</p>
        <p>
          <b>Related Topics:</b>{" "}
          {question.related_topics
            ?.map(cleanText)
            .join(", ")}
        </p>
      </details>
    </div>
  );
}
