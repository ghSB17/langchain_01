import os
os.environ["SERPAPI_API_KEY"] = "44f220acc03295fc758437a534ca26ea4ac9c21f7967211544e1b011367edc71"

from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper

tool = GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())

result = tool.run("Get senior level job postings related to 'FX' Software Engineer C#, .NET in NYC")
print(result)