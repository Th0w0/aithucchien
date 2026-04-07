from __future__ import annotations

import logging
import os
from typing import Annotated, Any, List, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from tools import calculate_budget, search_flights, search_hotels

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("travelbuddy")


with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt: str = f.read()


class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]


tools_list = [search_flights, search_hotels, calculate_budget]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

llm_with_tools = llm.bind_tools(tools_list)


def extract_text(message: Any) -> str:
    content: Any = getattr(message, "content", message)

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)

    return str(content)


def agent_node(state: AgentState) -> dict[str, list[Any]]:
    messages: list[BaseMessage] = state["messages"]
    prompt_messages: list[BaseMessage] = [SystemMessage(content=system_prompt)] + messages

    logger.info("Invoking LLM with %d message(s)", len(prompt_messages))
    response: Any = llm_with_tools.invoke(prompt_messages)

    tool_calls: list[dict[str, Any]] = getattr(response, "tool_calls", []) or []
    if tool_calls:
        for tc in tool_calls:
            logger.info("Tool called: %s | args=%s", tc.get("name"), tc.get("args"))
    else:
        logger.info("Direct response returned")

    return {"messages": [response]}


builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
builder.add_node("tool", ToolNode(tools_list))

builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "tool",
        "__end__": END,
    },
)
builder.add_edge("tool", "agent")

graph = builder.compile()


if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý du lịch Thông minh")
    print("Gõ 'quit' để thoát.")
    print("=" * 60)

    chat_history: list[BaseMessage] = []

    while True:
        try:
            user_input: str = input("Bạn: ").strip()
        except KeyboardInterrupt:
            print("\nTạm biệt!")
            break

        if user_input.lower() in ("quit", "exit", "q"):
            break

        if not user_input:
            continue

        logger.info("User input: %s", user_input)
        print("\nTravelBuddy đang suy nghĩ...")

        chat_history.append(HumanMessage(content=user_input))

        result: dict[str, list[Any]] = graph.invoke(
            {"messages": chat_history},
            config={"recursion_limit": 8},
        )

        final_message: Any = result["messages"][-1]
        final_text: str = extract_text(final_message)

        logger.info("Assistant response ready")
        print(f"\nTravelBuddy: {final_text}\n")

        chat_history = result["messages"]