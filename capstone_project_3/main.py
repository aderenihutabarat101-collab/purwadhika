import os
import streamlit as st 


from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.agents import create_agent
from langchain_core.messages import ToolMessage
from langchain.chat_models import init_chat_model
from langchain.tools import tool 
# from rag.retriever import retriever
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
try: 
  os.environ["OPENAI_API_KEY"] = os.getenv ("OPENAI_API_KEY")
except:
  os.environ["OPENAI_API_KEY"] = st.text_input("Enter your API Key :", type="password")


QDRANT_URL = os.environ["QDRANT_URL"]
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key = OPENAI_API_KEY)

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="Movie_documents",
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
    check_compatibility=False
)

df = pd.read_csv("/Users/alisyariati/Reni/python/imdb_top_1000 (1).csv")

model = ChatOpenAI(model="gpt-4o-mini")


# @tool
# def rag_search_tool(question: str) -> str:
#     """
#     Search movie information from Qdrant vector database.
#     """

#     docs = retriever.invoke(question)

#     if not docs:
#         return "No information found."

#     context = "\n\n".join(
#         [doc.page_content for doc in docs]
#     )

#     return context

@tool
def genre_recommendation_tool(
    genre: str
) -> str:
    """
    Recommend movies based on genre.
    """

    result = df[
        df["Genre"].str.contains(
            genre,
            case=False,
            na=False
        )
    ]

    if result.empty:
        return f"No movie found for genre {genre}"

    movies = result[
        ["Series_Title", "IMDB_Rating"]
    ].head(5)

    recommendations = []

    for _, row in movies.iterrows():

        recommendations.append(
            f"{row['Series_Title']} (Rating: {row['IMDB_Rating']})"
        )

    return "\n".join(recommendations)


@tool
def top_rating_tool() -> str:
    """
    Get highest rated movie.
    """

    movie = df.sort_values(
        by="IMDB_Rating",
        ascending=False
    ).iloc[0]

    return f"""
Movie: {movie['Series_Title']}
Rating: {movie['IMDB_Rating']}
Director: {movie['Director']}
"""

# @tool
# def similar_movie_tool(
#     movie_name: str
# ) -> str:
#     """
#     Find movies similar to a movie title.
#     """

#     docs = retriever.invoke(
#         f"Movie similar to {movie_name}"
#     )

#     if not docs:
#         return "No similar movie found."

#     result = []

#     for doc in docs:

#         title = doc.metadata.get(
#             "title",
#             "Unknown Movie"
#         )

#         result.append(title)

#     return "\n".join(result)

tools = [
        genre_recommendation_tool,
        top_rating_tool,
        # similar_movie_tool,
        # rag_search_tool,
]

def chat_movie(question, history):
    agent = create_agent(
        model="openai:gpt-4o-mini",
        tools=tools,
        system_prompt="You are an IMDb movie expert. Answer only questions related to movies, TV shows, actors, directors, ratings, overview, genres, and recommendations. Use available tools whenever needed.."
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Chat History:
                    {history}

                    User Question:
                    {question}
                    """
                }
            ]
        }
    )

    answer = result["messages"][-1].content

    total_input_tokens = 0
    total_output_tokens = 0

    for message in result["messages"]:
        if "usage_metadata" in message.response_metadata:
            total_input_tokens += message.response_metadata["usage_metadata"]["input_tokens"]
            total_output_tokens += message.response_metadata["usage_metadata"]["output_tokens"]
        elif "token_usage" in message.response_metadata:
            # Fallback for older or different structures
            total_input_tokens += message.response_metadata["token_usage"].get("prompt_tokens", 0)
            total_output_tokens += message.response_metadata["token_usage"].get("completion_tokens", 0)

    price = 17_000*(total_input_tokens*0.15 + total_output_tokens*0.6)/1_000_000

    tool_messages = []
    for message in result["messages"]:
        if isinstance(message, ToolMessage):
            tool_message_content = message.content
            tool_messages.append(tool_message_content)

    response = {
        "answer": answer,
        "price": price,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "tool_messages": tool_messages
    }
    return response



st.title("IMDb Movie Intelligence Assistant")
st.image("./IMDBmovie.png")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me IMDb Movie question"):
    messages_history = st.session_state.get("messages", [])[-20:]
    history = "\n".join([f'{msg["role"]}: {msg["content"]}' for msg in messages_history]) or " "

    # Display user message in chat message container
    with st.chat_message("Human"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "Human", "content": prompt})
    
    # Display assistant response in chat message container
    with st.chat_message("AI"):
        response = chat_movie(prompt, history)
        answer = response["answer"]
        st.markdown(answer)
        st.session_state.messages.append({"role": "AI", "content": answer})

    with st.expander("**Tool Calls:**"):
        st.code(response["tool_messages"])

    with st.expander("**History Chat:**"):
        st.code(history)

    with st.expander("**Usage Details:**"):
        st.code(f'input token : {response["total_input_tokens"]}\noutput token : {response["total_output_tokens"]}')

