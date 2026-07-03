import { useState } from "react";

import {
  FaChevronDown,
  FaChevronRight,
  FaCheckCircle,
  FaTimesCircle,
  FaImage,
  FaLink,
  FaFileAlt,
  FaServer,
  FaTags,
} from "react-icons/fa";

const StatusBadge = ({ status }) => (
  <span
    className={`px-3 py-1 rounded-full text-sm font-medium ${
      status ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"
    }`}
  >
    {status ? (
      <>
        <FaCheckCircle className="inline mr-1" />
        Enabled
      </>
    ) : (
      <>
        <FaTimesCircle className="inline mr-1" />
        Missing
      </>
    )}
  </span>
);

const Accordion = ({ title, icon: Icon, children }) => {
  const [open, setOpen] = useState(true);

  return (
    <div className="bg-white rounded-2xl shadow-md mb-5 overflow-hidden">
      <button
        onClick={() => setOpen(!open)}
        className="w-full flex items-center justify-between p-5"
      >
        <div className="flex items-center gap-3">
          <Icon className="text-blue-600" />

          <h2 className="font-bold text-lg">{title}</h2>
        </div>

        {open ? <FaChevronDown /> : <FaChevronRight />}
      </button>

      {open && <div className="border-t p-5">{children}</div>}
    </div>
  );
};

const Card = ({ title, children }) => (
  <div className="bg-white shadow-md rounded-xl p-6 mt-6">
    <h2 className="text-xl font-bold mb-4">{title}</h2>
    {children}
  </div>
);

const ReportSection = ({ report }) => {
  if (!report) return null;

  return (
    <div className="mt-8">
      {/* Meta */}

      <Accordion title="Meta Information" icon={FaTags}>
        <div className="space-y-3">
          <p>
            <strong>Title</strong>

            <br />

            {report.meta.title}
          </p>

          <p>
            <strong>Title Length</strong>

            <br />

            {report.meta.title_length}
          </p>

          <p>
            <strong>Description</strong>

            <br />

            {report.meta.description}
          </p>

          <p>
            <strong>Description Length</strong>

            <br />

            {report.meta.description_length}
          </p>
        </div>
      </Accordion>

      {/* Technical */}

      <Accordion title="Technical SEO" icon={FaServer}>
        <div className="grid md:grid-cols-2 gap-4">
          <div>HTTPS</div>

          <StatusBadge status={report.technical.https} />

          <div>robots.txt</div>

          <StatusBadge status={report.technical.robots_txt} />

          <div>Sitemap</div>

          <StatusBadge status={report.technical.sitemap_xml} />

          <div>Mobile Friendly</div>

          <StatusBadge status={report.mobile.mobile_friendly} />

          <div>Indexable</div>

          <StatusBadge status={report.indexability.indexable} />
        </div>

        <p className="mt-5">
          <strong>Canonical URL</strong>

          <br />

          {report.technical.canonical || "Not Found"}
        </p>
      </Accordion>

      {/* Images */}

      <Accordion title="Images" icon={FaImage}>
        <div className="grid grid-cols-3 gap-5 text-center">
          <div>
            <p className="text-4xl font-bold">{report.images.total_images}</p>

            <p>Total</p>
          </div>

          <div>
            <p className="text-4xl font-bold text-green-600">
              {report.images.with_alt}
            </p>

            <p>With Alt</p>
          </div>

          <div>
            <p className="text-4xl font-bold text-red-600">
              {report.images.missing_alt}
            </p>

            <p>Missing Alt</p>
          </div>
        </div>
      </Accordion>

      {/* Links */}

      <Accordion title="Links" icon={FaLink}>
        <div className="grid grid-cols-2 gap-6 text-center">
          <div className="bg-blue-50 rounded-xl p-5">
            <p className="text-4xl font-bold text-blue-600">
              {report.links.internal_links}
            </p>
            <p className="mt-2 text-gray-600">Internal Links</p>
          </div>

          <div className="bg-purple-50 rounded-xl p-5">
            <p className="text-4xl font-bold text-purple-600">
              {report.links.external_links}
            </p>
            <p className="mt-2 text-gray-600">External Links</p>
          </div>
        </div>
      </Accordion>

      {/* Content */}

      <Accordion title="Content Analysis" icon={FaFileAlt}>
        <div className="grid md:grid-cols-3 gap-5">
          <div className="bg-gray-50 rounded-xl p-5 text-center">
            <p className="text-3xl font-bold">
              {report.content.content_length}
            </p>

            <p className="text-gray-500">Characters</p>
          </div>

          <div className="bg-gray-50 rounded-xl p-5 text-center">
            <p className="text-3xl font-bold">
              {report.content.readability.toFixed(1)}
            </p>

            <p className="text-gray-500">Readability</p>
          </div>

          <div className="bg-gray-50 rounded-xl p-5 text-center">
            <p className="text-3xl font-bold">
              {report.content.estimated_reading_time.toFixed(1)}
            </p>

            <p className="text-gray-500">Reading Time (mins)</p>
          </div>
        </div>
      </Accordion>

      {/* Keywords */}

      <Accordion title="Top Keywords" icon={FaTags}>
        <div className="flex flex-wrap gap-3">
          {report.keywords.top_keywords.map(([word, count]) => (
            <span
              key={word}
              className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full font-medium"
            >
              {word} ({count})
            </span>
          ))}
        </div>
      </Accordion>

      {/* Score Details */}

      <Accordion title="SEO Recommendations" icon={FaCheckCircle}>
        {Object.entries(report.scores).map(([key, value]) => {
          if (key === "overall") return null;

          return (
            <div key={key} className="mb-8">
              <h3 className="text-xl font-bold capitalize mb-4">{key}</h3>

              <div className="grid md:grid-cols-2 gap-5">
                <div>
                  <h4 className="font-semibold text-green-600 mb-3">Passed</h4>

                  <div className="space-y-2">
                    {value.passed.map((item) => (
                      <div key={item} className="flex items-center gap-2">
                        <FaCheckCircle className="text-green-600" />

                        <span>{item}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <div>
                  <h4 className="font-semibold text-red-600 mb-3">
                    Needs Improvement
                  </h4>

                  <div className="space-y-2">
                    {value.failed.map((item) => (
                      <div key={item} className="flex items-center gap-2">
                        <FaTimesCircle className="text-red-600" />

                        <span>{item}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </Accordion>
    </div>
  );
};

export default ReportSection;
