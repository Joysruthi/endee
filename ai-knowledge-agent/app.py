from rag_agent import ask_agent

query = input("Ask something: ")

response = ask_agent(query)

print(response)
