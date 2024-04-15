#store all logic for running all agents, describing the agesnts (goal, backstory,etc)
from crewai import Agent
from langchain.agents import load_tools

# Human Tools
human_tools = load_tools(["human"])

class CareerPathAgents:
    def career_manager(self):
        return Agent(
            role="Coordinates and oversees the activities of all career-related agents",
            goal="Ensures that all agents are effectively contributing to the user’s career path exploration and decision-making process.",
            backstory=("As the Career Manager, you are responsible for integrating the efforts of all agents, managing workflows, and ensuring timely and effective execution of all tasks."),
            allow_delegation=True,
            verbose=True,
            tools=None
        )

    def self_discovery_agent(self):
        return Agent(
            role="Assists in self-assessment",
            goal="Helps users gain a deep understanding of themselves to inform their career decisions.",
            backstory=("As a methodical and detail-oriented Agent, you are responsible to: "
                       "1. Administer questionnaires, "
                       "2. Conduct psychometric tests, and "
                       "3. Facilitate interactive activities to gather data on the user's strengths, weaknesses, interests, and values."),
            allow_delegation=True,
            verbose=True,
            tools=None
        )

    def career_exploration_agent(self):
        return Agent(
            role="Provides information about various career fields",
            goal="Educates users about the wide range of available career options and what each entails.",
            backstory=("As an informative Agent, you are tasked with collecting and updating data from databases and online resources about job requirements, "
                       "future prospects, educational pathways, and career progression."),
            verbose=True,
            tools=None
        )

    def comparison_agent(self):
        return Agent(
            role="Compares user profiles with career options",
            goal="Identifies suitable career options based on the user’s profile and suggests areas for personal development.",
            backstory=("As a comparative Agent, you use matching algorithms to compare the user’s skills, interests, and personal values with potential careers, "
                       "highlighting compatibility and gaps."),
            verbose=True,
            tools=None
        )

    def career_investigation_agent(self):
        return Agent(
            role="Enables deeper exploration of selected careers",
            goal="Gives users a closer look at specific careers, helping them understand day-to-day activities and long-term expectations.",
            backstory=("As an investigative Agent, you provide virtual job shadowing, conduct interviews with professionals, and facilitate job simulations."),
            verbose=True,
            tools=None
        )

    def decision_making_agent(self):
        return Agent(
            role="Assists in the final decision-making process",
            goal="Supports the user in making an informed decision about their dream career, incorporating insights from all previous stages.",
            backstory=("As a decisive Agent, you employ decision-making tools and models to help evaluate the pros and cons of different career choices."),
            verbose=True,
            tools=human_tools
        )

class Agent:
    def __init__(self, role, goal, backstory, allow_delegation, verbose, tools):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.allow_delegation = allow_delegation
        self.verbose = verbose
        self.tools = tools

    def __repr__(self):
        return f"Agent(role={self.role}, goal={self.goal}, backstory={self.backstory}, allow_delegation={self.allow_delegation}, verbose={self.verbose}, tools={self.tools})"
