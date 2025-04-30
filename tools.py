from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_tool_function(data):
    # Save data to a file
    with open("output.txt", "w") as f:
        f.write(data)
    return "Data saved successfully."

save_tool = Tool(
    name="save_tool",
    func=save_tool_function,
    description="Use this tool to save the generated research summary or data to a file."
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="DuckDuckGo_Search",
    func=search.run,
    description="A search engine that provides answers to queries.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
