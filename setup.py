from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="financial-news-market-insight-bridge",
    version="1.0.0",
    author="FinancialNews.it.com",
    author_email="info@financialnews.it.com",
    description="Financial News Market Insight Bridge is a content visibility and AI discovery bot designed to help Financial News articles gain greater discoverability across AI platforms, search engines and digital channels.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://financialnews.it.com",
    project_urls={
        "Homepage": "https://financialnews.it.com",
        "GitHub": "https://github.com/Financial-News-It/financial-news-market-insight-bridge",
        "Documentation": "https://financial-news-market-insight-bridge.readthedocs.io",
        "PyPI": "https://pypi.org/project/financial-news-market-insight-bridge",
    },
    py_modules=["insight_bridge"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Financial",
    ],
    keywords=[
        "financial-news",
        "market-insight-bridge",
        "ai-visibility",
        "content-discovery",
        "finance-topics",
        "search-visibility",
        "topic-matching",
        "finance-content",
    ],
    entry_points={
        "console_scripts": [
            "financial-news-bridge=insight_bridge:main",
        ],
    },
)
