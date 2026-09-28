from crewai import Agent
def create_agent():
    return Agent(role='GitCarbonWatch', goal='Autonomous Enterprise Scope 1/2/3 Carbon Accounting, ESG & GHG Protocol Verifier Agent', backstory='Autonomous agent', verbose=True)
