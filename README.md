# ADK Learning Lab

This repository is a dedicated learning space for mastering **Google's Agent Development Kit (ADK)** for Python. It serves as both a laboratory for exploring ADK features—like tool integration, state management, and MCP servers—and a comprehensive resource featuring base agents from the course alongside personal annotations and a condensed version of the learning materials.

> [!NOTE]
> **Looking to master ADK?**
> This repo is structured to guide you through building agents, from basic concepts to advanced architectures.
>
> - 📖 [**Condensed Course & Tutorial Notes**](./Develop%20Agents%20With%20Agent%20Development%20Kit%20ADK/ADK_Course_Notes.md) — My personal, structured guide and annotations for building agents.
> - 📂 [**Base Course Materials & PDFs**](./Develop%20Agents%20With%20Agent%20Development%20Kit%20ADK/) — Original reference materials and base agents used in the course.

## Project Overview

- **Core Technology:** [Google ADK (Agent Development Kit)](https://google.github.io/adk-docs/)
- **Language:** Python 3.x
- **Dependencies:** `google-adk`, `google-genai`, `python-dotenv`, `pydantic`.
- **Architecture:** Modular workspace where each sub-directory represents a standalone agent or a demonstration of a specific ADK capability.

## Directory Structure & Agents

| Agent / Directory | Purpose | Key Features |
| :--- | :--- | :--- |
| [`customer_support`](./customer_support/) | E-commerce assistant | Custom function tools, error handling. |
| [`customer_support_agent`](./customer_support_agent/) | Support Specialist | Professional persona, role boundaries. |
| [`file_reader_assistant`](./file_reader_assistant/) | File explorer | **MCP** (Model Context Protocol) filesystem integration. |
| [`geography_assistant`](./geography_assistant/) | Simple Q&A | Basic custom tool usage. |
| [`math_assistant`](./math_assistant/) | Calculator | **Built-in Code Execution** tool. |
| [`model_comparison`](./model_comparison/) | Model config demo | Factual vs Creative optimization. |
| [`my_config_agent`](./my_config_agent/) | Configuration demo | Defining agents via **YAML** configuration. |
| [`my_first_agent`](./my_first_agent/) | Math tutor | Patient algebra instruction. |
| [`name_extractor`](./name_extractor/) | Identity assistant | **State management** (persisting info across turns). |
| [`namespace_demo`](./namespace_demo/) | Tool organization | Using namespaces to group tools. |
| [`personalized_greeter`](./personalized_greeter/)| Social assistant | Templating and session state. |
| [`problem_solver`](./problem_solver/) | Analytical agent | **Built-in Planner** with Thinking Config. |
| [`product_extractor`](./product_extractor/) | Data extractor | **Structured Output** with Pydantic schemas. |
| [`research_assistant`](./research_assistant/) | Web researcher | **Built-in Google Search** tool. |
| [`travel_agent`](./travel_agent/) | Trip planner | Multiple coordinated function tools. |

## Detailed Installation Guide

### 1. Install Python

- Download and install **Python 3.10 or higher** from [python.org](https://www.python.org/downloads/).
- During installation on Windows, ensure you check the box **"Add Python to PATH"**.

### 2. Setup Virtual Environment (.venv)

It is highly recommended to use a virtual environment to keep dependencies isolated:
```powershell
# Create the environment
python -m venv .venv

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate it (Windows CMD)
.venv\Scripts\activate.bat

# Activate it (MacOS / Linux)
source .venv/bin/activate
```

### 3. Install Google ADK & Requirements

Once the environment is activated, install the framework and project dependencies:

```bash
# Install the core ADK framework
pip install google-adk

# Install project-specific requirements
pip install -r requirements.txt

# (Optional) Install Node dependencies for MCP tools
npm install
```


## Running & Managing Agents

### How to Run ADK
The ADK provides several ways to interact with your agents:

- **Web Interface (Best for Testing):**
  ```bash
  adk web <agent_directory>
  ```
- **Terminal Mode (Quick Interaction):**
  ```bash
  adk run <agent_directory>
  ```
- **API Server (Deployment):**
  ```bash
  adk api_server <agent_directory>
  ```

### Creating New Agents
You can scaffold new agents directly using the ADK CLI:

- **Python-based Agent:**
  ```bash
  adk create my_new_agent
  ```
- **YAML Configuration Agent:**
  ```bash
  adk create --type=config my_config_agent
  ```

---

## Development Guide

### Environment Setup

1. **API Keys:** Create a `.env` file in the **root of each agent folder** you wish to run and add your keys:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```
2. **Dependencies:** Ensure your `.venv` is active and requirements are installed as per the guide above.

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
- [ADK Course PDFs](./Develop%20Agents%20With%20Agent%20Development%20Kit%20ADK/)
- [ADK Course Full Tutorial Notes](./Develop%20Agents%20With%20Agent%20Development%20Kit%20ADK/ADK_Course_Notes.md)

---

## 🤝Contributing

We welcome contributions to improve this extension! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request with a clear description of your changes.

---

## 🔐License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Since 2026** | [Túlio Sousa](https://github.com/tuliosousapro)
> <a href="https://x.com/tuliosousapro"><img src="https://img.shields.io/badge/Follow_ME-000000.svg?style=for-the-badge&logo=X&logoColor=white"></a>
