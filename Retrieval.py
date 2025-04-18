from pathlib import Path
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

def retrieve_and_respond(query):
    embedder = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    retriver = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="learning_langchain",
        embedding=embedder
    )


    search_results = retriver.similarity_search(
        query=query
    )
    search_result = search_results[0].page_content
    search_result = search_result.replace("\n", " ")

    system_prompt = f"""
    You are a helpful assistant. You will be provided with relevant chunks of text from a document. 
    Your task is to answer the user's question based on the provided chunks {search_result}. If the information is not 
    present in the chunks, respond with "I don't know".
    """

    messages = [
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": query }
    ]

    genAiModel = ChatOpenAI(
        model="gpt-3.5-turbo",
    )

    response = genAiModel.invoke(messages)
    return response.content
