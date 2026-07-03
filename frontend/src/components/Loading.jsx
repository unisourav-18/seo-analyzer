const Loading = () => {
  return (
    <div className="bg-white rounded-xl shadow-md p-8 text-center mt-6">
      <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto"></div>

      <h2 className="text-xl font-semibold mt-4">
        Analyzing Website...
      </h2>

      <p className="text-gray-500 mt-2">
        Please wait while we perform the SEO audit.
      </p>
    </div>
  );
};

export default Loading;