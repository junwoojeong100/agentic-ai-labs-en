# Agentic AI Labs

A hands-on project for building Multi-Agent systems using Azure AI Foundry Agent Service.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/junwoojeong100/agentic-ai-labs?quickstart=1)

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Quick Start](#-quick-start)
3. [Lab Guide](#-lab-guide)
4. [Architecture](#-architecture)
5. [Key Features](#-key-features)
6. [Infrastructure & Resources](#-infrastructure--resources)
7. [Project Structure](#-project-structure)
8. [Prerequisites](#-prerequisites)
9. [Environment Variables & Configuration](#-environment-variables--configuration)
10. [Observability](#-observability)
11. [Changing Models](#-changing-models)
12. [Cleanup](#-cleanup)
13. [References](#-references)

---

## 🎯 Overview

This hands-on lab is a comprehensive guide for **building production-level Multi-Agent systems**. It runs in **GitHub Codespaces** (also supports local environments) and covers the following 4 core areas centered around Azure AI Foundry:

| Core Area | Description | Implementation Technology | Learning Lab |
|---------|------|----------|----------|
| **Multi-Agent Orchestration** | Collaboration and routing of multiple specialized Agents | Foundry Agent Service, Microsoft Agent Framework (MAF), Connected Agent, Workflow Pattern | Lab 3-6 | 
| **Retrieval-Augmented Generation** | Accurate answer generation based on knowledge base | Azure AI Search, Hybrid Search (Vector + BM25), text-embedding-3-large | Lab 2 |
| **Tool & Protocol Integration** | Real-time information utilization through external tool and API integration | MCP (Model Context Protocol), FastMCP, Container Apps | Lab 3-4 |
| **Observability & Tracing** | Agent execution tracking, performance monitoring, quality evaluation | OpenTelemetry, Application Insights, Azure AI Evaluation | Lab 3-4, 6-7 |

> **💡 Lab Environment**  
> - **GitHub Codespace (Recommended)**: Pre-installed with Azure CLI, azd, Python, Docker, etc. - start immediately
> - **Local Environment (VS Code)**: Supports macOS, Linux, Windows - Run Jupyter notebooks in VS Code (See [PREREQUISITES.md](./PREREQUISITES.md) for detailed guide)

**Learning Outcomes**

After completing this lab, you will be able to **implement and operate** the following:

1. **�️ System Design and Deployment**
   - Design Azure AI Foundry-based Multi-Agent system architecture
   - Automated production infrastructure deployment using Bicep IaC
   - Build scalable Agent services based on Container Apps

2. **🤖 Agent Development and Orchestration**
   - Develop and integrate specialized Agents (Tool, Research, Main)
   - Implement complex workflows using Connected Agent Pattern and Workflow Pattern
   - Apply 6 orchestration patterns with Microsoft Agent Framework (MAF): Sequential, Concurrent, Conditional, Loop, Error Handling, Handoff

3. **🔍 RAG and Tool Integration**
   - Build Azure AI Search-based hybrid search (vector + keyword) RAG
   - Integrate external tools/APIs through MCP (Model Context Protocol)
   - Improve answer reliability with automatic Citation feature

4. **📊 Observability and Quality Management**
   - Implement OpenTelemetry-based distributed tracing
   - Monitor operational metrics with Application Insights
   - Automated quality evaluation using Azure AI Evaluation SDK
   - Establish Content Recording operational strategy (PII masking, sampling)

5. **🎯 Production Operations Capability**
   - Understand and appropriately utilize the difference between Monitoring vs Tracing
   - Debug workflows and optimize performance with MAF Dev UI
   - Establish strategies for model changes, resource management, and cost optimization

**💡 One-line Summary**: "A practical guide to building a **production-ready AI Agent system** from start to finish, including RAG + MCP + Multi-Agent + Observability"

---

> **📋 Before You Start**: Check the prerequisites in [PREREQUISITES.md](./PREREQUISITES.md).  
> Most tools are automatically installed when using Codespace, but Azure subscription and permissions need to be prepared in advance.

---

## 🚀 Quick Start

### 1️⃣ Start GitHub Codespace

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/junwoojeong100/agentic-ai-labs?quickstart=1)

**Method:**
- Click the button above, or
- GitHub repository → **Code** → **Codespaces** → **Create codespace on main**
- Environment setup automatically completes (2-3 minutes)

### 2️⃣ Lab Progression

Once Codespace is ready, run the Jupyter notebooks in order:

1. **Lab 1**: Deploy Azure resources (`01_deploy_azure_resources.ipynb`)
2. **Lab 2**: Build RAG knowledge base (`02_setup_ai_search_rag.ipynb`)
3. **Lab 3**: Deploy Foundry Agent without MAF (`03_deploy_foundry_agent.ipynb`)
4. **Lab 4**: Deploy Foundry Agent with MAF (`04_deploy_foundry_agent_with_maf.ipynb`)
5. **Lab 5**: MAF Workflow patterns (`05_maf_workflow_patterns.ipynb`)
6. **Lab 6**: MAF Dev UI (`06_maf_dev_ui.ipynb`)
7. **Lab 7**: Evaluate Agents (`07_evaluate_agents.ipynb`)

> 💡 **Tip**: Each Lab assumes the previous Lab has been completed. Proceed in order!

---

## 📓 Lab Guide

The lab consists of **7 Jupyter notebooks**, and it is recommended to proceed sequentially:

| Lab | Notebook | Goal | Difficulty | Duration | Key Content |
|-----|--------|------|--------|----------|-----------|  
| **1** | [01_deploy_azure_resources.ipynb](./01_deploy_azure_resources.ipynb) | Deploy Azure infrastructure | 🟢 Beginner | 10-15 min | Create AI Foundry, OpenAI, AI Search, Container Apps Environment with `azd provision` |
| **2** | [02_setup_ai_search_rag.ipynb](./02_setup_ai_search_rag.ipynb) | Build RAG knowledge base | 🟢 Beginner | 15-20 min | Create index, embed 50 documents, test hybrid search |
| **3** | [03_deploy_foundry_agent.ipynb](./03_deploy_foundry_agent.ipynb) | Deploy Multi-Agent system | 🟡 Intermediate | 20-30 min | **Connected Agent Pattern**: Deploy Main/Tool/Research Agent + MCP Server to Container Apps |
| **4** | [04_deploy_foundry_agent_with_maf.ipynb](./04_deploy_foundry_agent_with_maf.ipynb) | Deploy Workflow Pattern | 🟡 Intermediate | 25-35 min | **Workflow Pattern**: Router+Executor, parallel execution, custom OpenTelemetry implementation |
| **5** | [05_maf_workflow_patterns.ipynb](./05_maf_workflow_patterns.ipynb) | MAF orchestration patterns | 🔴 Advanced | 40-60 min | Practice 6 patterns (Sequential, Concurrent, Conditional, Loop, Error Handling, Handoff) |
| **6** | [06_maf_dev_ui.ipynb](./06_maf_dev_ui.ipynb) | MAF Dev UI | 🟢 Beginner | 10-15 min | Utilize workflow visualization, debugging, and performance analysis tools |
| **7** | [07_evaluate_agents.ipynb](./07_evaluate_agents.ipynb) | Evaluate Agent quality | 🟡 Intermediate | 20-30 min | Evaluate Groundedness, Relevance, Coherence with Azure AI Evaluation SDK |**💡 Difficulty Criteria**:
- 🟢 **Beginner**: Focus on code execution and concept understanding
- 🟡 **Intermediate**: Requires architecture understanding, some customization possible
- 🔴 **Advanced**: Advanced concepts, various pattern combinations, practical application skills required

**⏱️ Total Estimated Duration**: Approximately 2.5 - 3.5 hours (first time)

### Lab 1: Azure Infrastructure Deployment

**Deployed Resources:**
- **Azure AI Foundry**: Multi-Agent development platform
- **Azure OpenAI Service**: GPT-4o (recommended), text-embedding-3-large models
- **Azure AI Search**: Vector search and RAG support
- **Azure Container Apps Environment**: Agent service hosting environment

**Deployment Method:**
- Automatic deployment based on Bicep templates using `azd provision` command
- Takes approximately 3-5 minutes, automatically generates config.json
- Configures basic infrastructure used in all subsequent Labs

> **💡 Tip**: After deployment, all endpoint information is saved in `config.json`.

### Lab 2: Building RAG Knowledge Base

**Building Process:**
1. **Data Preparation**: 50 travel destination documents (`data/knowledge-base.json`)
2. **Generate Embeddings**: Azure OpenAI text-embedding-3-large (3072 dimensions)
3. **Create Index**: Configure vector index in Azure AI Search
4. **Test Search**: Validate hybrid search (vector + keyword)

**Index Schema:**
- `id`, `title`, `content`: Document basic information
- `category`, `section`: Hierarchical classification
- `contentVector`: 3072-dimensional vector (for search)

> **💡 Tip**: Fast vector search with HNSW algorithm, improved accuracy with hybrid search

### Lab 3: Multi-Agent System Deployment

**Agent Configuration:**
- **Main Agent**: User query analysis and agent routing
- **Tool Agent**: Call external tools via MCP protocol
- **Research Agent**: Knowledge search based on RAG

**Deployment Components:**
1. **MCP Server**: Model Context Protocol server (weather tool)
2. **Agent Service**: Multi-Agent service based on Foundry Agent
3. **Container Apps**: Deploy both services to Container Apps

**Test Scenarios:**
- Simple question → Research Agent (RAG)
- Tool required → Tool Agent (MCP)
- Complex query → Multiple Agent collaboration

> **💡 Tip**: You can visualize Agent interactions with AI Foundry's Tracing feature.

### Lab 4: Agent Framework Deployment

**Framework Patterns:**
- **Router Pattern**: Route to appropriate Agent based on query type
- **Executor Pattern**: Agent execution and result integration
- **OpenTelemetry**: Distributed tracing and monitoring

**Key Features:**
1. **Intelligent Routing**: LLM-based query classification
2. **Dynamic Execution**: Agent selection and execution at runtime
3. **Observability**: Track entire Agent call chain

**Deployment and Testing:**
- Deploy Agent Framework to Container Apps
- Test via REST API endpoints
- Monitor performance with Azure Monitor + OpenTelemetry

> **💡 Tip**: Router Pattern enables efficient Agent orchestration in production environments.

### Lab 5: MAF Workflow Patterns in Detail

**6 Patterns to Learn:**
1. **Sequential**: Sequential execution (A → B → C)
2. **Concurrent**: Parallel execution (simultaneous processing then integration)
3. **Conditional**: Conditional branching (dynamic routing)
4. **Loop**: Iterative improvement (feedback-based)
5. **Error Handling**: Error processing and recovery
6. **Handoff**: Dynamic control transfer (escalation)

**Lab Scenario**: Multi-Agent collaboration through a travel planning system

> **💡 MAF vs Foundry Agent**
> - **Foundry Agent**: Individual agent (LLM inference, tool calling)
> - **MAF Workflow**: Agent execution flow control (orchestration)

### Lab 6: MAF Dev UI

**Required Packages:**
- `agent-framework-devui>=1.0.0b251007` - Microsoft Agent Framework Dev UI tool
  - Web-based interface for workflow visualization and debugging
  - Defined in `requirements.txt` and automatically installed

**Learning Content:**
- **Start Dev UI Server**: Run workflow visualization tool with `agent_framework.devui.serve()` function
- **Workflow Graph**: Visual representation of nodes and edges as a graph
- **Real-time Debugging**: Monitor execution status and input/output data for each node
- **Performance Analysis**: Identify execution time per node, token usage, and bottlenecks
- **Execution History**: Save, view, and compare previous execution results

**Key Features:**
- 🎯 Workflow visualization (Sequential, Concurrent patterns)
- 🔍 Real-time node status monitoring
- 📊 Performance metrics and optimization guides

> **💡 Tip**: Use Dev UI only in development environment, disable with `enable_dev_ui=False` in production.

### Lab 7: Agent Evaluation and Quality Measurement

**Evaluation Framework:**
- **Azure AI Evaluation SDK**: Automated quality evaluation
- **Evaluation Metrics**: Groundedness, Relevance, Coherence, Fluency
- **Performance Measurement**: Response time, token usage, success rate

**Evaluation Process:**
1. **Prepare Test Dataset**: `evals/eval-input.jsonl` (various query scenarios)
2. **Run Automated Evaluation**: Quality evaluation using GPT-4 as evaluator
3. **Analyze Results**: Identify score distribution and improvement points
4. **Visualization**: Generate evaluation results dashboard with `show_eval_results.py`

**Evaluation Items:**
- **Groundedness**: Are answers based on RAG documents?
- **Relevance**: Are answers related to the question?
- **Coherence**: Are answers logically consistent?
- **Fluency**: Natural Korean expressions?

> **💡 Evaluation Best Practices**
> - Include various query types (simple questions, complex reasoning, multi-agent collaboration)
> - Track performance changes with regular evaluations
> - Feed evaluation results back into Agent improvements

---

## �️ Architecture

### Lab 3: Foundry Agent Service - Connected Agent Pattern

**Base Technology:** Azure AI Foundry Agent Service

**Orchestration:** Connected Agent Pattern (Handoff-based)

**Key Features:**
- Uses Foundry Agent Service SDK
- Connect between Agents with `handoff_to_agent()` API
- Thread-based conversation context management
- Main Agent delegates work to Sub Agents

**Monitoring:**
- ✅ Application Insights (automatically collected)
- ✅ OpenTelemetry (SDK automatic instrumentation)
- ✅ Prompt/Completion recording (`AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true`)

```text
┌────────────────────────────────────────────────────────────┐
│         Multi-Agent System (Connected Agent)               │
│                                                            │
│  ┌─────────────────────────────────────────────┐          │
│  │          Main Agent                         │          │
│  │  (Task Analysis & Agent Routing)            │          │
│  │  → handoff_to_tool_agent()                  │          │
│  │  → handoff_to_research_agent()              │          │
│  └────────────┬────────────────┬────────────────┘          │
│               │                │                           │
│       ┌───────▼──────┐  ┌──────▼──────────┐               │
│       │  Tool Agent  │  │  Research       │               │
│       │  (MCP)       │  │  Agent (RAG)    │               │
│       └──────┬───────┘  └────────┬────────┘               │
│              │                   │                         │
│       ┌──────▼───────┐    ┌──────▼─────────┐              │
│       │  MCP Server  │    │  Azure AI      │              │
│       │  (ACA)       │    │  Search (RAG)  │              │
│       └──────────────┘    └────────────────┘              │
└────────────────────────────────────────────────────────────┘
```

### Lab 4: Foundry Agent Service - Workflow Pattern

**Base Technology:** Azure AI Foundry Agent Service (same as Lab 3)

**Orchestration:** Workflow Pattern (Router + Executor)

**Key Features:**
- Uses the same Foundry Agent Service
- Intent classification and routing with Router Executor
- Workflow Context-based state management
- Parallel execution and complex conditional branching possible

**Monitoring:**
- ✅ Application Insights (uses the same infrastructure)
- ✅ OpenTelemetry (custom instrumentation implementation)
- ✅ Prompt/Completion recording (uses the same configuration variables)

```text
┌────────────────────────────────────────────────────────────┐
│      Agent Service - Workflow Pattern                      │
│                                                            │
│  ┌──────────────────────────────────────────┐             │
│  │        Router Executor                   │             │
│  │   (AI-based Intent Classification)       │             │
│  └────┬──────┬────────┬────────────┬────────┘             │
│       │      │        │            │                      │
│   ┌───▼──┐ ┌▼───┐  ┌─▼────┐   ┌──▼────────┐             │
│   │ Tool │ │Research│ │General│ │Orchestrator│            │
│   │Exec  │ │Executor│ │Executor│ │Executor  │             │
│   └───┬──┘ └┬───┘  └─┬────┘   └──┬────────┘             │
│       │     │        │            │                      │
│   ┌───▼─────▼────────▼────────────▼──────┐               │
│   │      Workflow Context                │               │
│   │   (Message Passing & Output)         │               │
│   └──────────────────────────────────────┘               │
│                                                            │
│   External Resources:                                     │
│   ┌──────────────┐    ┌────────────────┐                 │
│   │  MCP Server  │    │  Azure AI      │                 │
│   │  (Tools)     │    │  Search (RAG)  │                 │
│   └──────────────┘    └────────────────┘                 │
└────────────────────────────────────────────────────────────┘
```

**Lab 3 vs Lab 4 Key Differences:**

| Feature | Lab 3 (Connected Agent) | Lab 4 (Workflow Pattern) |
|------|------------------------|-------------------------|
| **Agent Base** | ✅ Foundry Agent Service | ✅ Foundry Agent Service |
| **Workflow Pattern** | Connected Agent (Handoff) | Workflow Pattern (Router+Executor) |
| **Routing Method** | `handoff_to_agent()` API | Router Executor function |
| **Execution Flow** | Main → Handoff → Sub Agent | Router → Executor → Output |
| **State Management** | Thread-based | Workflow Context-based |
| **Parallel Execution** | Sequential Handoff | Orchestrator parallel capable |

> **💡 Commonalities (Agent and Monitoring):**
> - ✅ Both Labs use **the same Azure AI Foundry Agent Service**
> - ✅ Both Labs use **the same Application Insights**
> - ✅ Both Labs use **the same OpenTelemetry settings**
> - ✅ Both Labs controlled by **the same environment variables**
> - ✅ MCP Server and Azure AI Search integration are also the same
> 
> **🎯 Differences (Orchestration):**
> - Lab 3: **Connected Agent Pattern** - Sequential task delegation between Agents via Handoff API
> - Lab 4: **Workflow Pattern** - Flexible flow control and parallel execution with Router and Executor

### Lab 5: MAF Workflow + Foundry Agent Integrated Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│              MAF Workflow Orchestration Layer                    │
│             (Microsoft Agent Framework - WorkflowBuilder)        │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│  │  Sequential    │  │  Concurrent    │  │  Conditional/  │   │
│  │  Pattern       │  │  Pattern       │  │  Loop/Handoff  │   │
│  │                │  │                │  │  Patterns      │   │
│  │  A → B → C     │  │  ┌→ A         │  │  [Conditional] │   │
│  │  (Sequential)  │  │  ├→ B         │  │  A → B or C    │   │
│  │                │  │  └→ C → Merge │  │  (Dynamic)     │   │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘   │
│          │                   │                    │            │
└──────────┼───────────────────┼────────────────────┼────────────┘
           │                   │                    │
┌──────────▼───────────────────▼────────────────────▼────────────┐
│           Azure AI Foundry Agents (Agent Layer)                │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐ │
│  │  Validator      │  │  Transformer    │  │  Summarizer    │ │
│  │  Agent          │  │  Agent          │  │  Agent         │ │
│  │  (Foundry)      │  │  (Foundry)      │  │  (Foundry)     │ │
│  └─────────────────┘  └─────────────────┘  └────────────────┘ │
│                                                                 │
│  ✅ Thread-based State Management                              │
│  ✅ LLM Integration (GPT-4o)                                    │
│  ✅ Tool/MCP Server Integration                                │
└─────────────────────────────────────────────────────────────────┘
```

**MAF Workflow Key Features:**
- **Graph-based Execution**: Define nodes and edges with `WorkflowBuilder`
- **@executor Decorator**: Simply define each node as a function
- **WorkflowContext**: Type-safe data passing between nodes
- **Dynamic Routing**: Conditionally select next node at runtime
- **Parallel Execution**: Execute multiple nodes simultaneously (asyncio.gather)
- **State Management**: Track entire workflow execution state

### Key Components

- **Main Agent**: User request analysis and routing to sub-Agents through Connected Agent
- **Tool Agent**: Utilize MCP server tools (real-time weather information)
- **Research Agent**: RAG-based knowledge base search through Azure AI Search
- **MCP Server**: FastMCP-based tool server deployed to Azure Container Apps

## ⚙️ Key Features Summary

### Azure AI Foundry Agent Service
- **Agent Creation and Management**: Specialized Agents based on GPT-4o
- **Connected Agent Pattern**: Collaboration through connections between Agents
- **Tool Integration**: Azure AI Search, MCP Tools, Function Calling
- **Thread Management**: Maintain conversation context

### Multi-Agent System Configuration
- **Main Agent (Orchestrator)**: 
  - Analyze user requests and select appropriate Agent
  - Call sub-Agents through Connected Agent
  - Integrate multiple Agent responses and generate final answer
  
- **Tool Agent**:
  - Utilize external tools by integrating with MCP server
  - **Real-time Weather Information**: Provide accurate weather data for cities worldwide
  - HTTP-based MCP client implementation
  
- **Research Agent**:
  - Implement RAG through Azure AI Search
  - Hybrid search (vector + keyword)
  - Generate answers based on knowledge base
  - **Automatic Citation Feature**: 
    - Azure AI Foundry SDK automatically displays sources (e.g., `【 3:0†source】`)
    - Click each citation in Tracing UI to view original document
    - Automatically generated by built-in SDK feature without code implementation

### MCP (Model Context Protocol) Server
- **Real-time Weather Information Service**:
  - `get_weather(location)`: Accurate real-time weather information for cities worldwide
  - **Data Source**: wttr.in API (free, no API key required)
  - **Supported Languages**: Supports both Korean/English city names (e.g., 'Seoul', '서울')
  - **Provided Information**: 
    - Current temperature and feels-like temperature
    - Weather conditions (clear, cloudy, rain, etc.)
    - Humidity and wind speed/direction
    - Observation time
- **FastMCP Framework**: Easy Python-based MCP server implementation
- **Azure Container Apps Deployment**: Scalable serverless hosting
- **HTTP/SSE Endpoint**: Provides MCP protocol via `/mcp` path

### Microsoft Agent Framework (MAF) - Lab 5
- **WorkflowBuilder Pattern**: Graph-based workflow orchestration
- **@executor Decorator**: Simply define each workflow node as a function
- **WorkflowContext**: Type-safe data passing and state management between nodes
- **6 Workflow Pattern Implementations**:
  - **Sequential**: Sequential execution (A → B → C)
  - **Concurrent**: Parallel execution (A, B, C execute simultaneously → integration)
  - **Conditional**: Conditional branching (execute A or B or C based on condition)
  - **Loop**: Iterative improvement (feedback-based maximum N iterations)
  - **Error Handling**: Error detection and recovery (retry, alternative paths)
  - **Handoff**: Dynamic control transfer (escalation to expert agents based on complexity)
- **Foundry Agent Integration**: Use Azure AI Foundry Agent as MAF Workflow nodes
- **Asynchronous Execution**: High-performance parallel processing based on asyncio
- **Type Safety**: Message type definition based on dataclass

### RAG (Retrieval-Augmented Generation)
- **Azure AI Search Integration**: Vector + keyword hybrid search
- **Embedding Model**: Azure OpenAI text-embedding-3-large (3072 dimensions)
- **Knowledge Base**: 50 AI Agent-related documents (chunked by category)
- **Search Optimization**: HNSW algorithm, Top-K=5, Semantic Ranker

> **📖 Detailed Schema**: In Lab 2, create an index with id, title, content, category, contentVector (3072 dimensions) fields. For details, see [`02_setup_ai_search_rag.ipynb`](./02_setup_ai_search_rag.ipynb).

## 🧩 Infrastructure & Resources Overview

### Resources Created After Deployment

| Resource | Purpose | Features |
|--------|------|------|
| Azure AI Foundry Project | Agent and AI service integration | **Hub-less standalone project (GA)** |
| Azure OpenAI | LLM models, text embedding | Includes text-embedding-3-large |
| Azure AI Search | RAG knowledge base | Vector search, hybrid query |
| Azure Container Apps | MCP server and Agent API hosting | Auto-scaling, Managed Identity |
| Azure Container Registry | Container image storage | Private registry |
| Azure Key Vault | Secret and key management | RBAC integration |
| Azure Storage Account | Data and log storage | Blob, Table, Queue |

> **💡 Architecture Features**  
> - **Hub-less AI Foundry Project**: Standalone project that directly connects OpenAI, AI Search, etc.
> - **Key Vault & Storage**: Deployed as infrastructure but not used in this lab (can be utilized for production expansion)



## 📁 Project Structure

```text
agentic-ai-labs/
├── infra/                                      # Bicep infrastructure code
│   ├── main.bicep                              # Main Bicep template
│   ├── main.parameters.json                    # Parameters file
│   └── core/                                   # Modularized Bicep resources
│       ├── ai/                                 # AI Foundry, OpenAI
│       ├── host/                               # Container Apps
│       ├── search/                             # AI Search
│       └── security/                           # Key Vault, RBAC
│
├── src/                                        # Source code
│   ├── foundry_agent/                          # Multi-Agent implementation (Foundry Agent Service)
│   │   ├── main_agent.py                       # Main Agent (orchestrator)
│   │   ├── tool_agent.py                       # Tool Agent (MCP integration)
│   │   ├── research_agent.py                   # Research Agent (RAG)
│   │   ├── api_server.py                       # Agent API server
│   │   ├── masking.py                          # PII masking utility
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── agent_framework/                        # Agent Framework Workflow
│   │   ├── main_agent_workflow.py              # Workflow Router & Orchestrator
│   │   ├── tool_agent.py                       # Tool Executor (MCP)
│   │   ├── research_agent.py                   # Research Executor (RAG)
│   │   ├── api_server.py                       # Workflow API server
│   │   ├── test_workflow.py                    # Workflow test
│   │   ├── masking.py                          # PII masking utility
│   │   ├── requirements.txt                    # Includes OpenTelemetry packages
│   │   └── Dockerfile
│   └── mcp/                                    # MCP server
│       ├── server.py                           # FastMCP tool server
│       ├── requirements.txt
│       └── Dockerfile
│
├── data/                                       # Knowledge base
│   └── knowledge-base.json                     # Documents for AI Search indexing
│
├── scripts/                                    # Utility scripts
│   └── generate_knowledge_base.py
│
├── 01_deploy_azure_resources.ipynb             # Lab 1 notebook
├── 02_setup_ai_search_rag.ipynb                # Lab 2 notebook
├── 03_deploy_foundry_agent.ipynb               # Lab 3 notebook
├── 04_deploy_foundry_agent_with_maf.ipynb      # Lab 4 notebook
├── 05_maf_workflow_patterns.ipynb              # Lab 5 notebook
├── 06_maf_dev_ui.ipynb                         # Lab 6 notebook
├── 07_evaluate_agents.ipynb                    # Lab 7 notebook
├── azure.yaml                                  # azd configuration
├── evals/                                      # Evaluation results (Lab 7)
│   ├── eval-queries.json                       # Test queries
│   ├── eval-input.jsonl                        # Agent execution results
│   └── eval-output.json                        # Evaluation scores
├── OBSERVABILITY.md                            # Observability (Tracing/Analytics) advanced guide
└── README.md                                   # This file
```

### Infrastructure Parameters

Customizable in `infra/main.parameters.json`:

| Parameter | Description | Default |
|---------|------|--------|
| `environmentName` | Environment name | Auto-generated |
| `location` | Azure region | `eastus` |
| `principalId` | User Principal ID | Auto-detected |

Key resources are automatically created in the Bicep template, with resource names having hashes added for uniqueness.

### Azure Developer CLI (azd) Configuration

The `azure.yaml` file defines metadata for azd deployment:

```yaml
name: ai-foundry-agent-lab
infra:
  path: ./infra
  module: main
```

**azd Usage Scope:**
- **Lab 1**: Deploy Azure infrastructure using the `azd provision` command (Bicep template-based)
  - Creates Azure AI Foundry Project, OpenAI, AI Search, Container Apps Environment, etc.
  - Provisions infrastructure only without creating Container Apps (takes approximately 3-5 minutes)
- **Lab 3**: Container deployment is done manually using the `az containerapp create` command
  - Deploy MCP Server and Agent Service
  - Manual deployment approach used for more granular control and learning purposes

**Note:** 
- azd is primarily used for infrastructure provisioning (Lab 1)
- Application deployment (Lab 3) is executed manually step-by-step for learning purposes
- Use `azd provision` instead of `azd up` to quickly configure infrastructure only

## ✅ Prerequisites

### 🚀 Quick Start: GitHub Codespace (Recommended)

This lab is designed to be run in **GitHub Codespace**.

**Auto-configured when using Codespace:**
- ✅ Azure CLI, Azure Developer CLI (azd)
- ✅ Python 3.12 + virtual environment (`.venv`)
- ✅ Docker, Git, VS Code extensions
- ✅ All required Python packages automatically installed

**Azure Subscription Requirements:**
- Azure subscription (free trial available)
- Subscription Owner role required
- Recommended to use a separate subscription dedicated to this lab

> **💡 Detailed Guide**: See [PREREQUISITES.md](./PREREQUISITES.md) for local environment setup, Azure permission requirements, and detailed configuration information.

---

## 🌐 Environment Variables & Configuration

### Config.json (Auto-generated)

After Lab 1 deployment, `config.json` is automatically generated and includes the following information:

```json
{
  "project_connection_string": "https://xxx.services.ai.azure.com/api/projects/yyy",
  "search_endpoint": "https://srch-xxx.search.windows.net/",
  "search_index": "ai-agent-knowledge-base",
  "mcp_endpoint": "https://mcp-server.xxx.azurecontainerapps.io",
  "agent_endpoint": "https://agent-service.xxx.azurecontainerapps.io"
}
```

### Agent Environment Variables

When running Lab 3, the `src/foundry_agent/.env` file is automatically generated.

**Core Settings:**
- Azure AI Foundry connection information
- Azure AI Search (RAG)
- MCP Server endpoint
- Application Insights (Observability)
- OpenTelemetry configuration

> **📘 Detailed Guide**: [CONFIGURATION.md](./CONFIGURATION.md)
> - Complete list of environment variables
> - Required vs optional variables
> - Content Recording production strategy
> - Sampling and PII masking settings
> - Change application procedure

---

## 📊 Observability

Provides **Monitoring** and **Tracing** capabilities for operational observability of the Azure AI Foundry Agent system.

### Core Concepts

| Feature | Purpose | Data Type |
|------|------|------------|
| **Monitoring** | System health, SLA, performance trends | Aggregate metrics (call count, latency, error rate, tokens) |
| **Tracing** | Execution flow, debugging, quality analysis | Span Tree, Prompt/Completion |

### Implemented in This Lab

- ✅ **Lab 3 (Foundry Agent)**: Azure Agent Service auto-instrumentation
- ✅ **Lab 4 (Agent Framework)**: Custom OpenTelemetry full implementation

### Detailed Guide

For all details including differences between Monitoring and Tracing, configuration methods, and operational strategies, refer to the **[OBSERVABILITY.md](./OBSERVABILITY.md)** document:

- 🎯 Detailed comparison of Monitoring vs Tracing
- ⚙️ Step-by-step configuration guide (environment variables, code implementation)
- 🔍 Span structure and custom instrumentation
- 📋 Content Recording operational strategy
- 🔧 Sampling, PII masking, Troubleshooting
- 📊 Kusto query examples

---

## 🔄 Changing Models

The project uses an **environment variable-centric design** that allows model changes without code modification.

> **🎯 Key Point: Only 1 place to change models!**  
> Just modify the `model_name` and `model_version` variables in the **Lab 1 notebook** and it will automatically apply to the entire project.  
> No need to modify other files!

### How to Change

Change the model name and version in the **Lab 1 notebook** and deploy:

```python
# In 01_deploy_azure_resources.ipynb
model_name = "gpt-4o"          # 👈 Change to desired model
model_version = "2024-11-20"   # 👈 Model version (varies by model)
model_capacity = 50            # TPM capacity
```

After deployment, simply change the `AZURE_AI_MODEL_DEPLOYMENT_NAME` environment variable in the `.env` file.

### Supported Model Examples

| Model Name | Version | Features |
|--------|------|------|
| `gpt-4o` | `2024-11-20` | Multimodal, fast response, cost-efficient (recommended) |
| `gpt-4o-mini` | `2024-07-18` | Lightweight version, low cost |

**Key Features:**
- Context Length: 128,000 tokens
- Multimodal input support (text, images)
- Real-time streaming and full tool support
- Fast response speed and cost efficiency
- Enhanced safety (Jailbreak defense 84/100)

> **📘 Detailed Guide**: See [MODEL_CHANGE_GUIDE.md](./MODEL_CHANGE_GUIDE.md)

---

## 🧹 Resource Cleanup

After completing the lab, clean up resources to reduce costs:

```bash
# Check resource group name in config.json
cat config.json | grep resource_group

# Delete entire resource group (recommended)
az group delete --name <resource-group-name> --yes --no-wait
```

> ⚠️ Deleting the resource group will permanently delete all resources. This cannot be undone.

---

## 📚 References

### Official Documentation
- [Azure AI Foundry Agent Service](https://learn.microsoft.com/azure/ai-foundry/concepts/agents)
- [Azure AI Search RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
- [Model Context Protocol](https://spec.modelcontextprotocol.io/)
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)

### Additional Guides 📘
- [PREREQUISITES.md](./PREREQUISITES.md) - Detailed prerequisites
- [DEVCONTAINER.md](./DEVCONTAINER.md) - Dev Container setup guide
- [CONFIGURATION.md](./CONFIGURATION.md) - Environment variable configuration guide
- [OBSERVABILITY.md](./OBSERVABILITY.md) - Advanced observability guide
- [MODEL_CHANGE_GUIDE.md](./MODEL_CHANGE_GUIDE.md) - How to change models

---

**Built with ❤️ using Azure AI Foundry** | MIT License | [Issues](https://github.com/junwoojeong100/agentic-ai-labs/issues)
