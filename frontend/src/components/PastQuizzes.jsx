import { useEffect, useState } from "react";
import { fetchHistory, fetchQuizById } from "../api/quizApi";
import QuizModal from "./QuizModal";

// 🔹 Clean text helper
const cleanText = (text) => {
  if (!text) return "";
  return text.replace(/\n/g, " ").replace(/\s+/g, " ").trim();
};

export default function PastQuizzes() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [selectedQuiz, setSelectedQuiz] = useState(null);

  useEffect(() => {
    const loadHistory = async () => {
      try {
        setLoading(true);
        const data = await fetchHistory();
        setHistory(data);
      } catch (err) {
        setError("Failed to load history");
      } finally {
        setLoading(false);
      }
    };

    loadHistory();
  }, []);

  const handleView = async (id) => {
    try {
      const data = await fetchQuizById(id);
      setSelectedQuiz(data);
    } catch (err) {
      alert("Failed to load quiz");
    }
  };

  return (
    <div>
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>S.No</th>
            <th>ID</th>
            <th>Quiz Title</th>
            <th>Article</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {history.length === 0 && !loading && (
            <tr>
              <td colSpan="5" style={{ textAlign: "center" }}>
                No past quizzes found
              </td>
            </tr>
          )}

          {history.map((q, index) => (
            <tr key={q.quiz_id}>
              {/* 🔢 Serial Number */}
              <td>{index + 1}</td>

              <td>{q.quiz_id}</td>

              {/* 🧹 Cleaned text */}
              <td>{cleanText(q.quiz_title)}</td>
              <td>{cleanText(q.article_title)}</td>

              <td>
                <button onClick={() => handleView(q.quiz_id)}>
                  View
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedQuiz && (
        <QuizModal
          quiz={selectedQuiz}
          onClose={() => setSelectedQuiz(null)}
        />
      )}
    </div>
  );
}
