from langgraph.graph import StateGraph

from .configuration import Configuration
from .nodes import answer_question, rerank_documents
from .state import State

# Define a new graph
workflow = StateGraph(State, config_schema=Configuration)

# Add the nodes to the graph
workflow.add_node("rerank_documents", rerank_documents)
workflow.add_node("answer_question", answer_question)

# Connect the nodes
workflow.add_edge("__start__", "rerank_documents")
workflow.add_edge("rerank_documents", "answer_question")
workflow.add_edge("answer_question", "__end__")

# Compile the workflow into an executable graph
graph = workflow.compile()
graph.name = "SurfSense QnA Agent"  # This defines the custom name in LangSmith
