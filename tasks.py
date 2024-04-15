#defining specific task that need to be execute.
from functools import partial
from crewai import Task
from textwrap import dedent

class CareerPathAgents:
    def __init__(self):
        self.user_profile = {
            "current_state": None,
            "career_interests": [],
            "job_opportunities": []
        }
    
    def ask_current_state(self):
        print("Please select the statement that best describes where you are in your career decision-making process:")
        print("1. I really don't know what I want to become.")
        print("2. I have several ideas about what I might want to become.")
        
        choice = input("Enter the number of your current situation: ")
        if choice == "1":
            self.user_profile["current_state"] = "Undecided"
        elif choice == "2":
            self.user_profile["current_state"] = "ExploringOptions"
        else:
            print("Invalid input. Please choose 1 or 2.")
            self.ask_current_state()
        
    def find_job_opportunities(self, agent, career_topic, description):
        self.ask_current_state()  # Update current state based on user input
        return Task(
            description=dedent(f"""Find 5 high-interest job opportunities for the user based on the provided career topic and description.
                Career Topic: {career_topic}
                Career Description: {description}
                Current State: {self.user_profile['current_state']}

                The job opportunities should be relevant to the user's interests and current readiness to pursue a career path.
                """),
            agent=agent,
            expected_output=dedent("""Generate a list of 5 job opportunities that closely match the user's career interests and readiness level.
                Each opportunity should be well-researched and include detailed information about the role, company, and why it might be suitable for the user.
                """)
        )

    def career_exploration_task(self, agent, interests):
            return Task(
                description=dedent(f"""Research and provide information on various career fields relevant to the user's interests.
                    User's Interests: {interests}

                    Task:
                    - Collect updated data on job requirements, future prospects, educational pathways, and career progression related to the interests.
                    - Provide a comprehensive overview of each career option to educate the user about potential choices.
                    """),
                agent=agent,
                expected_output=dedent("""Provide a detailed report on career options that includes:
                    - Description of each field
                    - Necessary qualifications and skills
                    - Future career prospects
                    - Recommended educational pathways
                    """)
            )

    def comparison_task(self, agent, user_profile):
        return Task(
            description=dedent(f"""Compare the user's profile with potential career options to identify the best matches.
                User Profile: {user_profile}

                Task:
                - Use matching algorithms to assess compatibility between the user’s skills, interests, and career opportunities.
                - Highlight both suitable career options and areas where the user might need further development.
                """),
            agent=agent,
            expected_output=dedent("""Generate a comparative analysis report that includes:
                - Suitable career options for the user
                - Areas requiring skill development
                - Personalized recommendations based on the user's profile
                """)
        )

    def career_investigation_task(self, agent, career_choice):
        return Task(
            description=dedent(f"""Provide an in-depth exploration of specific careers chosen by the user.
                Selected Career: {career_choice}

                Task:
                - Conduct virtual job shadowing and arrange interviews with professionals in the field.
                - Facilitate realistic job simulations to give the user a practical understanding of daily tasks and responsibilities.
                """),
            agent=agent,
            expected_output=dedent("""Deliver an immersive exploration report that includes:
                - Insights from job shadowing
                - Summaries of professional interviews
                - Outcomes from job simulations
                - A day in the life of someone in the selected career
                """)
        )

    def decision_making_task(self, agent, career_options):
        return Task(
            description=dedent(f"""Assist the user in making the final decision on their career path.
                Career Options: {career_options}

                Task:
                - Utilize decision-making tools and models to evaluate the pros and cons of each option.
                - Integrate insights from previous stages to guide the user towards a well-informed decision.
                """),
            agent=agent,
            expected_output=dedent("""Produce a decision-making report that includes:
                - A comprehensive comparison of career options
                - Recommendations for the best-suited career path
                - Steps for pursuing the selected career
                """)
        )

class Task:
    def __init__(self, description, agent, expected_output):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output

