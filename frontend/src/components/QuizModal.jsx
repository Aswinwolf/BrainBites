export default function QuizModal({ quiz, onClose }) {
  return (
    <div className="modal-backdrop">
      <div className="modal">
        <h2>{quiz.quiz_title}</h2>

        {quiz.questions.map((q, index) => (
  <div key={q.id} className="question-card">
    <h3>
      {index + 1}. {q.question}
    </h3>

    <ul>
      {q.options.map((opt, i) => (
        <li key={i}>{opt}</li>
      ))}
    </ul>
  </div>
))}


        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}
