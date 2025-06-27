import os
from langchain.chat_models import init_chat_model
import dotenv

dotenv.load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")