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

Here is a [list of bots](list_ai.txt), agents, and crawlers used by AI companies, extracted from the provided data and gathered from the official AI developers websites:

#### OpenAI
* GPTBot
* ChatGPT-User
* OAI-SearchBot

#### Anthropic
* anthropic-ai
* ClaudeBot
* Claude-Web
* Claude-User
* Claude-SearchBot

#### Google
* Google-Extended
* Google-CloudVertexBot

#### Cohere
* cohere-ai

#### Perplexity
* PerplexityBot
* Perplexity-ai

#### DeepSeek
* DeepSeek
* DeepSeekBot

#### ByteDance
* Bytespider

#### Meta/ Facebook
* meta-externalagent
* meta-externalfetcher
* FacebookBot

#### Other AI-related Bots
* huggingface
* img2dataset
* ImagesiftBot
* Diffbot
* PetalBot (likely related to AI or search)
* MAZBot (possibly AI-related)
* DataForSeoBot (AI-driven SEO tool)
* Applebot-Extended

#### Notable Mentions
* CCBot (Common Crawl, used for AI training data)
* Scrapy (often used for AI data collection)
* NewsNow (AI-driven news aggregator)
* TurnitinBot (AI-powered plagiarism detection)