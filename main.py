#store the logic, connects all agents, tasks and run the crew 

#1. create agents
from agents import CareerPathAgents
#setum agents
agents=CareerPathAgents
career_manager=agents.career_manager
self_discovery_agent=agents.self_discovery_agent
career_exploration_agent=agents.career_exploration_agent
comparison_agent=agents.comparison_agent
career_investigation_agent=agents.career_investigation_agent
decision_making_agent=agents.decision_making_agent

#background info about career path:
career_topic="Berufswahltagebuch"
description="In this career diary were diving into the innovative ways Im using CrewAI to optimize my career path. Im exploring how ot harness the power of CrewAI to generate personalized Job opportunities "
user_profiile=""
#2. create tasks

tasks=CareerPathAgents()

tasks.ask_current_state(
    agent=self_discovery_agent,
    career_topic=career_topic,
    description=description,
)

tasks.find_job_opportunities(
    agent=career_exploration_agent,
    career_topic=career_topic,
    description=description,
)

tasks.comparison_task(
    agent=comparison_agent,
    career_topic=career_topic,
    description=description,
)
tasks.career_investigation_task(
    agent=career_investigation_agent,
    career_topic=career_topic,
    description=description,
)

tasks.decision_making_task(
    agent=decision_making_agent,
    career_topic=career_topic,
    description=description, 
)

#3. create tools

