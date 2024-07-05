import os

from crewai import Crew, Agent, Task, Process
from crewai_tools.tools.serper_dev_tool.serper_dev_tool import SerperDevTool
from pydantic import BaseModel


class AgentHandler:

    def __init__(self, openai_api_key: str | None, serper_api_key: str | None):
        self.report_crew = None
        self.openai_api_key = openai_api_key
        self.serper_api_key = serper_api_key

    def build_agent(self):
        os.environ["SERPER_API_KEY"] = self.serper_api_key
        # ToDo - Pass this as arg
        os.environ["OPENAI_API_KEY"] = self.openai_api_key
        search_tool = SerperDevTool()

        # Define your agents
        researcher = Agent(
            role="Researcher",
            goal="Conduct foundational research",
            backstory="An experienced researcher with a passion for uncovering insights",
            tools=[search_tool],
        )
        analyst = Agent(
            role="Data Analyst",
            goal="Analyze research findings",
            backstory="A meticulous analyst with a knack for uncovering patterns",
        )
        writer = Agent(
            role="Writer",
            goal="Draft the final report",
            backstory="A skilled writer with a talent for crafting compelling narratives",
        )

        research_task = Task(
            description="Gather relevant data about exciting web3 startups",
            agent=researcher,
            expected_output="Raw Data",
        )
        analysis_task = Task(
            description="Analyze the data and formulate recommendations",
            agent=analyst,
            expected_output="Data Insights",
        )
        writing_task = Task(
            description="Compose a report in Markdown format containing bullet points reflecting 3 different investment thesis",
            agent=writer,
            expected_output="Final Report",
        )

        # Form the crew with a sequential process
        self.report_crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
        )

        # Execute the crew

    def generate_markdown_report(self) -> str:
        # Too slow, move back to Langchain
        result = self.report_crew.kickoff()
        return result
