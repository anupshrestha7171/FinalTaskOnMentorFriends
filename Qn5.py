import networkx as nx

# Load the knowledge graph from the saved file
knowledge_graph = nx.read_graphml("knowledge_graph.graphml")


# Function to answer a question from the knowledge graph
def answer_question(question):
    # Process the question and extract relevant entities or keywords
    # Query the knowledge graph for relevant nodes and relationships
    # Retrieve the information from the graph to generate the answer

    # Example implementation
    if question == "What is the relationship between government and rules?":
        # Replace X and Y with the specific entities in your question
        x = "entity_X"
        y = "entity_Y"

        # Check if the entities exist in the graph
        if x in knowledge_graph.nodes and y in knowledge_graph.nodes:
            # Check if there is a direct edge between X and Y
            if knowledge_graph.has_edge(x, y):
                relationship_type = knowledge_graph.edges[x, y]["relationship_type"]
                answer = f"The relationship between {x} and {y} is {relationship_type}."
                return answer
            else:
                answer = f"There is no direct relationship between {x} and {y}."
                return answer
        else:
            answer = "One or both entities are not present in the knowledge graph."
            return answer

    # Handle other types of questions similarly

    # If the question does not match any known pattern
    answer = "I'm sorry, I don't have the information to answer that question."
    return answer


# Example question
question = "What is the relationship between government and rules?"

# Call the answer_question function
answer = answer_question(question)

print("Answer:", answer)
