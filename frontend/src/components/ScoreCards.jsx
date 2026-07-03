import {
  FaChartLine,
  FaServer,
  FaSearch,
  FaFileAlt,
  FaBolt,
} from "react-icons/fa";

const cards = [
  {
    key: "overall",
    title: "Overall SEO",
    icon: FaChartLine,
  },
  {
    key: "technical",
    title: "Technical",
    icon: FaServer,
  },
  {
    key: "onpage",
    title: "On-Page",
    icon: FaSearch,
  },
  {
    key: "content",
    title: "Content",
    icon: FaFileAlt,
  },
  {
    key: "performance",
    title: "Performance",
    icon: FaBolt,
  },
];

const getColor = (percentage) => {
  if (percentage >= 80) return "bg-green-500";
  if (percentage >= 60) return "bg-yellow-500";
  return "bg-red-500";
};

const getStatus = (percentage) => {
  if (percentage >= 90) {
    return {
      text: "Excellent",
      color: "text-green-600",
    };
  }

  if (percentage >= 75) {
    return {
      text: "Good",
      color: "text-blue-600",
    };
  }

  if (percentage >= 50) {
    return {
      text: "Average",
      color: "text-yellow-600",
    };
  }

  return {
    text: "Needs Improvement",
    color: "text-red-600",
  };
};

const ScoreCards = ({ scores }) => {
  if (!scores) return null;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 mt-10">
      {cards.map((card) => {
        const Icon = card.icon;

        const data = scores[card.key];

        const percentage = (data.score / data.max_score) * 100;

        const status = getStatus(percentage);

        return (
          <div
            key={card.key}
            className="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition duration-300"
          >
            <div className="flex items-center justify-between mb-5">
              <h3 className="font-semibold text-gray-700">{card.title}</h3>

              <Icon size={22} className="text-blue-600" />
            </div>

            <div className="text-4xl font-bold text-gray-800">{data.score}</div>

            <div className="text-gray-500 mb-5">/ {data.max_score}</div>

            <div className="w-full h-3 rounded-full bg-gray-200 overflow-hidden">
              <div
                className={`${getColor(
                  percentage,
                )} h-full rounded-full transition-all duration-700`}
                style={{
                  width: `${percentage}%`,
                }}
              />
            </div>

            <div className="mt-4 text-center">
              <p className="text-gray-500 text-sm">{percentage.toFixed(0)}%</p>

              <p className={`font-semibold mt-1 ${status.color}`}>
                {status.text}
              </p>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default ScoreCards;
