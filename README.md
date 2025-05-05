# The role of robots.txt in web crawling and the implications of disallowing LLM agents on news websites
In recent years, Large Language Models (LLMs) have gained immense popularity, revolutionizing the way we interact with technology. Companies like OpenAI, Google, and DeepSeek have integrated search functionalities into their LLM-based applications, enabling users to access vast amounts of information seamlessly. 

However, this raises an important question: How do websites, particularly news platforms, feel about these new "guests"? To explore this, we conducted an analysis of the robots.txt files of 100 of the most popular news websites worldwide.

### What is a robots.txt file?
The robots.txt file is a simple text file located in the root directory of a website. It serves as a communication tool between website owners and web crawlers (also known as bots or agents). The primary purpose of this file is to instruct web crawlers on which parts of the site they are allowed or disallowed to access. This is particularly important for managing server load, protecting sensitive information, and ensuring that search engines index content appropriately.

The syntax of a robots.txt file is straightforward. It typically includes the following components:
* *User-agent* specifies the name of the bot or agent to which the rule applies. For example, `User-agent: Googlebot` targets Google's web crawler.
* *Disallow* indicates which directories or pages the bot is not allowed to access. For example, `Disallow: /private/` prevents the bot from accessing the /private/ directory.
* *Allow* specifies exceptions to the disallow rules. For example, `Allow: /public/` permits access to the /public/ directory even if a broader disallow rule is in place.

### Our Project: analyzing robots.txt files of news websites
With the increasing use of LLM agents in search functionalities, it is essential to understand how websites, particularly news platforms, are responding to these new "visitors." To this end, we analyzed the robots.txt files of 100 of the most popular news websites worldwide. Our goal was to identify which LLM agents are explicitly disallowed from accessing these sites and to understand the implications of such restrictions.

Methodology:
* data collection: we compiled a list of the top 100 news websites based on global traffic rankings.
* robots.txt extraction: for each website, we retrieved the robots.txt file from the root directory.
* agents identification: we parsed the robots.txt files to extract the names of agents that are disallowed from accessing the sites.

### Findings
A significant number of news websites disallow certain LLM agents from accessing their content.

Here is a [list of bots](data/list_ai.txt), agents, and crawlers used by AI companies, extracted from the provided data and gathered from the official AI developers websites:

| Bot Name                          | Description                                                                                                      | Maintainer/Company         |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------|
| GPTBot                            | OpenAI's web crawler for improving AI models through website data collection                                     | OpenAI                     |
| ChatGPT-User                      | User agent string used by ChatGPT browser interactions                                                          | OpenAI                     |
| OAI-SearchBot                     | OpenAI's search engine crawler for AI training data                                                              | OpenAI                     |
| anthropic-ai                      | Anthropic's AI agent for website interactions and data processing                                               | Anthropic                  |
| ClaudeBot                         | Anthropic's web crawler for Claude AI training                                                                   | Anthropic                  |
| Claude-Web                        | Claude AI's web browsing interface agent                                                                         | Anthropic                  |
| Claude-User                       | User agent for Claude AI browser-based interactions                                                             | Anthropic                  |
| Claude-SearchBot                  | Claude AI's specialized search engine crawler                                                                    | Anthropic                  |
| Google-Extended                   | Google's AI training data crawler (for Bard/Gemini)                                                              | Google                     |
| Google-CloudVertexBot             | Crawler for Google Cloud's Vertex AI platform                                                                    | Google                     |
| cohere-ai                         | Cohere's AI agent for natural language processing tasks                                                          | Cohere                     |
| cohere-training-data-crawler      | Cohere's web crawler for collecting AI training data                                                            | Cohere                     |
| PerplexityBot                     | Perplexity AI's primary web crawler                                                                              | Perplexity AI              |
| Perplexity-ai                     | Secondary crawler for Perplexity's AI search engine                                                              | Perplexity AI              |
| Perplexity-User                   | User agent for Perplexity's browser-based AI interactions                                                        | Perplexity AI              |
| DeepSeek                          | DeepSeek's main AI agent for search and interactions                                                             | DeepSeek                   |
| DeepSeekBot                       | DeepSeek's web crawler for AI training data                                                                      | DeepSeek                   |
| huggingface                       | Crawler for Hugging Face's AI model repository                                                                   | Hugging Face               |
| img2dataset                       | Image-focused web crawler for AI training datasets                                                               | Hugging Face (community)   |
| ImagesiftBot                      | Image analysis and filtering bot for AI training                                                                 | Various AI companies       |
| Diffbot                           | AI-powered web scraper and data extractor                                                                        | Diffbot                    |
| Bytespider                        | ByteDance's web crawler for AI training data                                                                     | ByteDance                  |
| PetalBot                          | Huawei's web crawler for AI/machine learning purposes                                                            | Huawei                     |
| MAZBot                            | Media-focused AI crawler for content analysis                                                                    | MAZ Systems                |
| DataForSeoBot                     | SEO data crawler used for AI-powered marketing insights                                                          | DataForSeo                 |
| Amazonbot                         | Amazon's AI/ML web crawler for product data and Alexa training                                                   | Amazon                     |
| Applebot                          | Apple's web crawler for Siri and machine learning                                                                | Apple                      |
| Applebot-Extended                 | Extended version of Apple's AI crawler for specialized data collection                                           | Apple                      |
| meta-externalagent                | Meta's external AI agent for platform interactions                                                               | Meta (Facebook)            |
| meta-externalfetcher              | Meta's data collection bot for AI training                                                                       | Meta (Facebook)            |
| FacebookBot                       | Meta's primary web crawler for AI/ML applications                                                                | Meta (Facebook)            |
| YandexDialogs                     | Yandex's AI assistant (Alice) interaction bot                                                                    | Yandex                     |
| YandexAdditional                  | Yandex's supplemental AI data crawler                                                                            | Yandex                     |
| YandexAdditionalBot               | Secondary Yandex bot for AI-related data collection                                                              | Yandex                     |
| scalepostAI                       | AI-powered social media content analysis bot                                                                     | Scalepost                  |
| AI2Bot                            | Allen Institute for AI's research crawler                                                                        | Allen Institute for AI     |
| Ai2Bot-Dolma                      | Specialized crawler for the Dolma AI training dataset                                                            | Allen Institute for AI     |
| Twitterbot                        | Twitter's official crawler for AI-powered features                                                               | Twitter (X Corp)           |
| CCBot                             | Common Crawl's open dataset web crawler                                                                          | Common Crawl Foundation    |
| Scrapy                            | Open-source web crawling framework (used by many AI projects)                                                    | Scrapy community           |
| NewsNow                           | AI-powered news aggregation crawler                                                                              | NewsNow Group              |
| TurnitinBot                       | AI plagiarism detection system crawler                                                                           | Turnitin                   |
