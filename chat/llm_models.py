from langchain_openai import ChatOpenAI

from src.settings import settings


gpt_4_1_mini = ChatOpenAI(
    openai_api_key=settings.OPENAI_API_KEY,
    model="gpt-4.1-mini",
    temperature=1,
)

gpt_5_nano = ChatOpenAI(
    openai_api_key=settings.OPENAI_API_KEY,
    model="gpt-5-nano",
    temperature=0,
)
