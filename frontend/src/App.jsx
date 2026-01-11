import { useState } from "react";
import Tabs from "./components/Tabs";
import GenerateQuiz from "./components/GenerateQuiz";
import PastQuizzes from "./components/PastQuizzes";
import "./styles/app.css";

export default function App() {
  const [activeTab, setActiveTab] = useState("generate");

  return (
    <div className="app-container">
      <h1>AI Wiki Quiz Generator</h1>

      <Tabs activeTab={activeTab} setActiveTab={setActiveTab} />

      {activeTab === "generate" && <GenerateQuiz />}
      {activeTab === "history" && <PastQuizzes />}
    </div>
  );
}
