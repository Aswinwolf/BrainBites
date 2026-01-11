import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const generateQuiz = async (url, numQuestions) => {
  const res = await axios.post(`${BASE_URL}/generate-quiz`, {
    url,
    num_questions: numQuestions,
  });
  return res.data;
};

export const fetchHistory = async () => {
  const res = await axios.get(`${BASE_URL}/history`);
  return res.data;
};

export const fetchQuizById = async (id) => {
  const res = await axios.get(`${BASE_URL}/quiz/${id}`);
  return res.data;
};
