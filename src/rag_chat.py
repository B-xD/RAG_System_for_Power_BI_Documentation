# rag_chat.py

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from retriever import get_retriever
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from config import CHAT_MODEL, OPENAI_API_KEY, BASE_URL
from openai import OpenAI


#create an empty list to store chat history 
chat_history = []

retriever = get_retriever()
def main():
    """ This funcion takes the user query, adds the previous answer to the chat history,
        and closes the chatbot 
    """
    print("Hello! I am you power BI assistant.")
    while True:
        print("How may I assist? (click q to exit the chat):")
        question = str(input("USER: ")).strip()

        if question.lower()== 'q':
            print('See you later!')
            break
        else:
            chat_bot(question)

def chat_bot(question):

    client = OpenAI(
        api_key = OPENAI_API_KEY,
        base_url = BASE_URL
    )

    relevant_chunks = retriever.invoke(question)
    context_list = [d.page_content for d in relevant_chunks]
    context_for_query = chr(10).join(context_list)

    prompt = [
        {'role': 'developer', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': USER_PROMPT_TEMPLATE.format(
            context = context_for_query,
            question = question,
            chat_history = chat_history
        )
        }
    ]
    try:
        response = client.chat.completions.create(
            model = CHAT_MODEL,
            messages = prompt,
            temperature = 0
        )

        prediction = response.choices[0].message.content.strip()
    except Exception as e:
        prediction = f'Sorry, I encountered the following error: \n {e}'
    chat_history.append(prediction)
    return print(f"POWER BI ASSISTANT: {prediction}")

main()
