from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROK_API_KEY

llm = ChatGroq(
    groq_api_key = GROK_API_KEY,
    model_name = "llama-3.3-70b-versatile",
    temperature = 0.3 
)


itinerary_prompt = ChatPromptTemplate([
    ('system',"You are a helpful travel assistant. Create a day trip itinerary for {city} based on user's interest: {interests}, Provide a brief bulleted itinerary."),
    ('human',"Create am itinerary for my day trip")
])

def generate_itinerary(city:str,interests:list[str])->str:
    response = llm.invoke(
        itinerary_prompt.format_prompt(city=city,interests=', '.join(interests))
    )

    return response.content


