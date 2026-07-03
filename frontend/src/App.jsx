import { useState } from "react";

import api from "./services/api";

import SearchBar from "./components/SearchBar";
import Loading from "./components/Loading";
import ScoreCards from "./components/ScoreCards";
import ReportSection from "./components/ReportSection";

function App() {

  const [loading, setLoading] = useState(false);

  const [report, setReport] = useState(null);

  const analyzeWebsite = async (url) => {

    try {

      setLoading(true);

      setReport(null);

      const response = await api.post("/api/analyze", {
        url
      });

      const jobId = response.data.job_id;

      const poll = setInterval(async () => {

        const result = await api.get(
          `/api/results/${jobId}`
        );

        if (result.data.status === "completed") {

          clearInterval(poll);

          setReport(result.data.result);

          setLoading(false);

        }

      }, 2000);

    }

    catch (error) {

      console.error(error);

      alert("Analysis Failed");

      setLoading(false);

    }

  };

  return (

    <div className="min-h-screen bg-gray-100">

      <div className="max-w-7xl mx-auto p-8">

        <h1 className="text-5xl font-bold text-center mb-8">

          SEO Analyzer

        </h1>

        <SearchBar

          onAnalyze={analyzeWebsite}

          loading={loading}

        />

        {loading && <Loading />}

        {report && (

          <>

            <ScoreCards

              scores={report.scores}

            />

            <ReportSection

              report={report}

            />

          </>

        )}

      </div>

    </div>

  );

}

export default App;