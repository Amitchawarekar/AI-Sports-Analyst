from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from tools.match_lookup import get_match_summary
from tools.player_stats import get_player_stats
from tools.training_tool import suggest_training

llm = ChatOpenAI(model="gpt-4", temperature=0)

tools = [
    Tool(name="Match Lookup", func=get_match_summary, description="Fetches past match summaries"),
    Tool(name="Player Stats", func=get_player_stats, description="Retrieves player performance data"),
    Tool(name="Training Recommender", func=suggest_training, description="Gives training and workout tips"),
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
