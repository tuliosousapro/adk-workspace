# ADK Workspace

This workspace is a collection of AI agents built using Google's **Agent Development Kit (ADK)** for Python. It serves as a laboratory for exploring ADK features like tool integration, state management, Model Context Protocol (MCP) servers, and structured outputs.

## Project Overview

- **Core Technology:** [Google ADK (Agent Development Kit)](https://google.github.io/adk-docs/)
- **Language:** Python 3.x
- **Dependencies:** `google-adk`, `google-genai`, `python-dotenv`, `pydantic`.
- **Architecture:** Modular workspace where each sub-directory represents a standalone agent or a demonstration of a specific ADK capability.

## Directory Structure & Agents

| Agent / Directory | Purpose | Key Features |
| :--- | :--- | :--- |
| `customer_support` | E-commerce assistant | Custom function tools, error handling. |
| `file_reader_assistant` | File explorer | **MCP** (Model Context Protocol) filesystem integration. |
| `geography_assistant` | Simple Q&A | Basic custom tool usage. |
| `math_assistant` | Calculator | **Built-in Code Execution** tool. |
| `name_extractor` | Identity assistant | **State management** (persisting info across turns). |
| `namespace_demo` | Tool organization | Using namespaces to group tools. |
| `personalized_greeter`| Social assistant | Templating and session state. |
| `problem_solver` | Analytical agent | **Built-in Planner** with Thinking Config. |
| `product_extractor` | Data extractor | **Structured Output** with Pydantic schemas. |
| `research_assistant` | Web researcher | **Built-in Google Search** tool. |
| `travel_agent` | Trip planner | Multiple coordinated function tools. |
| `my_config_agent` | Configuration demo | Defining agents via **YAML** configuration. |

## Development Guide

### Environment Setup
1. Ensure Python 3.10+ is installed.
2. A virtual environment `.venv` is already present at the root.
3. Configure your `.env` file with necessary API keys (e.g., `GOOGLE_API_KEY`).

### Building and Running Agents
Agents are typically defined in an `agent.py` file using `LlmAgent`. To test or run them, use a runner script (e.g., `test_state.py`) that utilizes the `google.adk.runners.Runner`.

**Example execution:**
```powershell
# Navigate to an agent directory
cd name_extractor
# Run the test script
python test_state.py
```

### Key ADK Components
- **`LlmAgent`**: The core class for defining an agent's name, model, instructions, and tools.
- **`Runner`**: Executes the agent within a session context.
- **`McpToolset`**: Integrates external tools via Model Context Protocol (e.g., `npx @modelcontextprotocol/server-filesystem`).
- **`SessionService`**: Manages state and history (e.g., `InMemorySessionService`).

## Development Conventions
- **Tool Documentation:** Always provide clear docstrings for tool functions; ADK uses these as tool descriptions for the LLM.
- **State Management:** Use `session.state` for cross-turn persistence as demonstrated in `name_extractor`.
- **Structured Output:** Prefer Pydantic models for `output_schema` to ensure type-safe, structured responses.
- **MCP Integration:** When using MCP, ensure the required server (like Node.js for filesystem) is available in the environment.

## Resources
- [Official ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
