import { useState } from "react";

import api from "./services/api";

import SearchBar from "./components/SearchBar";
import Loading from "./components/Loading";
import ScoreCards from "./components/ScoreCards";
import ReportSection from "./components/ReportSection";

import { FaReact } from "react-icons/fa";
import { SiFastapi, SiSqlalchemy } from "react-icons/si";

function App() {
  const [loading, setLoading] = useState(false);

  const [report, setReport] = useState(null);

  const analyzeWebsite = async (url) => {
    try {
      setLoading(true);

      setReport(null);

      const response = await api.post("/api/analyze", {
        url,
      });

      const jobId = response.data.job_id;

      const poll = setInterval(async () => {
        const result = await api.get(`/api/results/${jobId}`);

        if (result.data.status === "completed") {
          clearInterval(poll);

          setReport(result.data.result);

          setLoading(false);
        }
      }, 2000);
    } catch (error) {
      console.error(error);

      alert("Analysis Failed");

      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="max-w-7xl mx-auto p-8">
        <h1 className="text-5xl font-bold text-center mb-8">SEO Analyzer</h1>

        <SearchBar onAnalyze={analyzeWebsite} loading={loading} />

        {loading && <Loading />}

        {report && (
          <>
            <ScoreCards scores={report.scores} />

            <ReportSection report={report} />
          </>
        )}

        <footer className="mt-16 border-t border-gray-300 pt-8 pb-6 text-center">
          <h3 className="text-xl font-semibold text-gray-800">SEO Analyzer</h3>

          <div className="flex justify-center items-center gap-6 mt-4 text-blue-600">
            <div className="flex items-center gap-2">
              <FaReact size={22} />
              <span className="text-gray-700">React</span>
            </div>

            <div className="flex items-center gap-2">
              <SiFastapi size={22} />
              <span className="text-gray-700">FastAPI</span>
            </div>

            <div className="flex items-center gap-2">
              <SiSqlalchemy size={22} />
              <span className="text-gray-700">SQLAlchemy</span>
            </div>
          </div>

          <p className="text-sm text-gray-500 mt-3">
            Performs Technical SEO, On-Page SEO, Content Analysis and SEO
            Scoring.
          </p>

          <p className="text-sm text-gray-400 mt-5">© 2026 Sourav Pandey</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
