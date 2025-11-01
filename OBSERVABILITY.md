# Observability (Monitoring & Tracing) Complete Guide

> 🏠 Return to main guide: [README.md](./README.md)

Complete guide for **Operational Observability** of Azure AI Foundry Agent systems. Covers everything from concepts of Monitoring and Tracing to practical implementation and operational strategies step by step.

---

## 📑 Table of Contents

### 🎯 Getting Started
1. [Observability Overview](#1-observability-overview)
2. [Monitoring vs Tracing Key Differences](#2-monitoring-vs-tracing-key-differences)

### 📊 Monitoring Implementation
3. [Monitoring Configuration Guide](#3-monitoring-configuration-guide)
4. [Detailed Collected Metrics](#4-detailed-collected-metrics)
5. [Viewing in Portal](#5-viewing-monitoring-in-portal)

### 🔍 Tracing Implementation
6. [Tracing Configuration Guide](#6-tracing-configuration-guide)
7. [Span Structure and Custom Instrumentation](#7-span-structure-and-custom-instrumentation)
8. [Content Recording (Prompt/Completion)](#8-content-recording-promptcompletion)

### ⚙️ Advanced Configuration
9. [Instrumentation Order (Order Matters)](#9-instrumentation-order-order-matters)
10. [Complete Environment Variables Guide](#10-complete-environment-variables-guide)
11. [Operational Strategy](#11-operational-strategy)
12. [Sampling Configuration](#12-sampling-configuration)

### 🛠️ Production Operations
13. [Kusto Query Examples](#13-kusto-query-examples)
14. [Troubleshooting Guide](#14-troubleshooting-guide)
15. [Checklist](#15-checklist)

### 📚 Appendix
16. [FAQ](#16-faq)
17. [References](#17-references)

---

## 1. Observability Overview

### 1.1. Three Observability Layers

Layers for observing Agent systems in Azure AI Foundry:

| Layer | Purpose | Data Type | Portal Location |
|------|------|------------|-------------|
| **Monitoring** | System health, SLA, performance trends | Aggregated metrics (numbers) | Monitoring > Application Analytics |
| **Tracing** | Execution flow, debugging, quality analysis | Span Tree, Attributes | Tracing tab |
| **Logging** | Runtime exceptions, status messages | Text logs | Container Apps Logs |

### 1.2. Patterns Implemented in This Lab

| Category | Lab 3 | Lab 4 |
|------|-------|-------|
| **Notebook** | 03_deploy_foundry_agent.ipynb | 04_deploy_foundry_agent_with_maf.ipynb |
| **Agent Foundation** | ✅ Azure AI Foundry Agent Service | ✅ Azure AI Foundry Agent Service |
| **Workflow Pattern** | Connected Agent (Handoff) | Workflow Pattern (Router+Executor) |
| **Monitoring** | ✅ Application Insights + OpenTelemetry | ✅ Application Insights + OpenTelemetry |
| **Tracing** | ✅ Content Recording support | ✅ Content Recording support |
| **Environment Variables** | Same OTEL configuration | Same OTEL configuration |

> **💡 Key Points**  
> - Both Labs use the **same Azure AI Foundry Agent Service**
> - **Observability configuration (Monitoring & Tracing) is also identical**
> - The difference is the **workflow orchestration pattern** (Connected Agent vs Workflow Pattern)

---

## 2. Monitoring vs Tracing Key Differences

### 2.1. Quick Comparison Table

| Category | Monitoring (Application Analytics) | Tracing |
|------|-----------------------------------|---------|  
| **Purpose** | System health, SLA, performance trend analysis | Individual request execution flow and debugging |
| **Data** | Aggregated metrics<br>(call count, average latency, error rate) | Detailed Span Tree<br>(step-by-step execution, Prompt/Completion) |
| **Use Cases** | • Daily call volume trend tracking<br>• SLA violation alerts<br>• Performance degradation detection<br>• Cost monitoring | • Analyzing slow request causes<br>• Prompt optimization<br>• Error debugging<br>• Agent routing verification |
| **Portal** | Monitoring > Application Analytics | Tracing tab |
| **Prompt/Completion** | ❌ Not supported | ✅ When Content Recording is enabled |
| **Prerequisites** | Container App + environment variables | Monitoring + additional instrumentation |
| **Data Latency** | 5-10 minutes | Real-time (1-2 minutes) |

### 2.2. When to Use What?

**📊 Use Monitoring for:**
- ✅ "Has the average response time increased this week?"
- ✅ "How many LLM calls occurred per day?"
- ✅ "I want to receive alerts when error rate exceeds 5%"
- ✅ "I want to see token usage trends and predict costs"**🔍 Use Tracing for:**
- ✅ "Why was Tool Agent selected instead of Research Agent for a specific question?"
- ✅ "How was the prompt delivered and how was the response generated?"
- ✅ "Why did the MCP call take 5 seconds?"
- ✅ "Why did the RAG search return these results?"

---

## 3. Monitoring Configuration Guide

### 3.1. Purpose

Monitoring provides insights into **overall system health** through aggregated metrics:
- Total Calls
- Average/P50/P95/P99 response time
- Error occurrence rate
- Token usage (input/output tokens)

### 3.2. Required Environment Variables

```bash
# Application Insights connection
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=...;IngestionEndpoint=...

# Service identifier (used for filtering in Tracing)
OTEL_SERVICE_NAME=foundry-agent-service  # or agent-framework-workflow

# Metrics Exporter specification
OTEL_METRICS_EXPORTER=azure_monitor
```

> **📍 How to Check CONNECTION_STRING**  
> Azure Portal > Application Insights resource > Properties > Copy Connection String

### 3.3. Code Implementation - Foundry Agent

`src/foundry_agent/api_server.py`:

```python
from azure.monitor.opentelemetry import configure_azure_monitor
from azure.ai.inference.tracing import AIInferenceInstrumentor
from azure.ai.projects import AIProjectClient
import logging

logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    # ✅ Step 1: Configure Azure Monitor (First!)
    app_insights_conn = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
    if app_insights_conn:
        configure_azure_monitor(
            connection_string=app_insights_conn,
            enable_live_metrics=True,  # Enable real-time metrics
            instrumentation_options={
                "azure_sdk": {"enabled": True},
                "fastapi": {"enabled": True},
                "requests": {"enabled": True},
            }
        )
        logger.info("✅ Azure Monitor configured for Monitoring")
        
        # ✅ Step 2: AI Inference instrumentation (Auto-track LLM calls)
        AIInferenceInstrumentor().instrument()
        logger.info("✅ AI Inference instrumentation enabled")
    else:
        logger.warning("⚠️ APPLICATIONINSIGHTS_CONNECTION_STRING not set")
    
    # ✅ Step 3: Create AIProjectClient (logging_enable=True required!)
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint,
        logging_enable=True  # ⭐ Very important!
    )
```

### 3.4. Code Implementation - Agent Framework

`src/agent_framework/main_agent_workflow.py`:

```python
from azure.monitor.opentelemetry import configure_azure_monitor
from azure.ai.inference.tracing import AIInferenceInstrumentor

def _initialize_agents(self):
    # ✅ Step 1: Configure Azure Monitor
    app_insights_conn = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
    if app_insights_conn:
        configure_azure_monitor(
            connection_string=app_insights_conn
        )
        logger.info("✅ Azure Monitor configured")
        
        # ✅ Step 2: AI Inference instrumentation
        AIInferenceInstrumentor().instrument()
        logger.info("✅ AI Inference instrumentation enabled")
    
    # ✅ Step 3: Create AIProjectClient
    self.project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint,
        logging_enable=True  # ⭐ Required!
    )
```

### 3.5. Prerequisites (Important!)

| Condition | Reason | Verification Method |
|------|------|--------|
| **Container App deployment** | Notebook execution doesn't collect metrics | `az containerapp show` |
| **Persistent service** | One-time scripts can't be aggregated | Verify Container App Running status |
| **Sufficient call volume** | Minimum 10+ requests recommended | Run test script |
| **Wait 5-10 minutes** | Initial metric display delay | Refresh Portal |

> **⚠️ Warning: Metrics won't be collected if you run Agents directly from Notebook!**  
> Metrics will only be aggregated when you deploy to Container App and call via HTTP requests.

---

## 4. Detailed Collected Metrics

### 4.1. Application Analytics Metric Categories

| Category | Metric | Description | Use Case |
|---------|--------|------|---------|
| **Volume** | Total Calls | Total LLM call count | Daily/weekly traffic trend analysis |
| | Requests/sec | Requests per second | Load pattern identification |
| **Performance** | Average Duration | Average response time (ms) | Performance baseline setting |
| | P50/P95/P99 | Percentile latency | SLA monitoring (e.g., P95 < 3s) |
| **Reliability** | Error Rate | Error occurrence rate (%) | Stability tracking |
| | Success Rate | Success rate (%) | Quality metric |
| **Cost** | Prompt Tokens | Total input tokens | Cost forecasting |
| | Completion Tokens | Total output tokens | Cost optimization strategy |

---

## 5. Verify Monitoring in Portal

### 5.1. Access Path

1. **Access Azure AI Foundry Portal** (https://ai.azure.com)
2. Select project
3. Left menu: **Monitoring** > **Application Analytics**
4. Select time range (e.g., Last 24 hours)

### 5.2. Metrics Dashboard Layout

- **Overview**: Overall summary (call count, average time, error rate)
- **Performance**: Response time distribution and trend charts
- **Reliability**: Success/failure ratio and error types
- **Usage**: Token usage statistics and cost analysis

### 5.3. If Metrics Are Not Visible

**Checklist:**

- [ ] Is the Container App in Running status?
- [ ] Is `APPLICATIONINSIGHTS_CONNECTION_STRING` correct?
- [ ] Did you create AIProjectClient with `logging_enable=True`?
- [ ] Have you executed at least 10 requests?
- [ ] Has 5-10 minutes passed since the first request?
- [ ] Did you select the correct time range in Portal?

**Debugging Commands:**

```bash
# Check Container App logs
az containerapp logs show \
  --name <container-app-name> \
  --resource-group <rg-name> \
  --follow

# Check Application Insights metrics
az monitor app-insights metrics show \
  --app <app-insights-name> \
  --resource-group <rg-name> \
  --metrics requests/count
```

---

## 6. Tracing Configuration Guide

### 6.1. Purpose

Tracing tracks the **execution flow of individual requests** in detail:
- Router → Executor → Tool/RAG execution flow
- Time taken for each step
- Prompt and Completion (when Content Recording enabled)
- Error location and stack trace

### 6.2. Additional Environment Variables

```bash
# ✅ Required Monitoring variables (same as section 3)
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=...
OTEL_SERVICE_NAME=foundry-agent-service

# ✅ Additional Tracing variables
OTEL_TRACES_EXPORTER=azure_monitor
OTEL_LOGS_EXPORTER=azure_monitor
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

# ✅ Display Prompt/Completion (recommended for Dev/Staging)
AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true
```

> **📍 Important:** Monitoring must be configured first for Tracing to work!

### 6.3. Foundry Agent - Auto Instrumentation

Azure Agent Service provides auto instrumentation by default:

```python
# ✅ After completing Monitoring setup (section 3)

# (Optional) Agent structure auto instrumentation
try:
    from azure.ai.agents.telemetry import AIAgentsInstrumentor
    AIAgentsInstrumentor().instrument()
    logger.info("✅ AIAgentsInstrumentor enabled")
except ImportError:
    logger.warning("⚠️ AIAgentsInstrumentor not available (optional)")
```

### 6.4. Agent Framework - Custom Instrumentation

Agent Framework implements OpenTelemetry manually:

**FastAPI Instrumentation (`api_server.py`):**

```python
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

@app.on_event("startup")
async def startup_event():
    # ... Monitoring setup (section 3) ...
    
    # ✅ Track FastAPI HTTP requests
    FastAPIInstrumentor.instrument_app(app)
    logger.info("✅ FastAPI instrumentation enabled")
```

---

## 7. Span Structure and Custom Instrumentation

### 7.1. What is a Span?

A Span represents **a unit of execution**:
- HTTP request processing
- Agent routing decision
- MCP tool invocation
- RAG search execution
- LLM call

Spans are connected in parent-child relationships to form a **Span Tree**.

### 7.2. Agent Framework Span Structure Example

```
POST /chat (FastAPI Span)
├── workflow.router (AI intent classification)
│   └── gen_ai.chat.completions (GPT-4o call)
├── workflow.executor.tool (Tool Executor)
│   └── tool_agent.mcp_call (MCP call)
│       └── http.client.request (HTTP request)
└── workflow.executor.research (Research Executor)
    └── research_agent.rag_search (RAG search)
        ├── gen_ai.embeddings.create (Embedding generation)
        └── azure.search.documents.query (AI Search query)
```

### 7.3. Custom Span Implementation

**Basic Pattern:**

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("operation_name") as span:
    # Set span attributes
    span.set_attribute("custom.key", "value")
    
    # Perform operation
    result = do_something()
    
    # Record result
    span.set_attribute("result.status", "success")
```

**Router Span (AI-based Intent Classification):**

```python
with tracer.start_as_current_span("workflow.router") as span:
    span.set_attribute("router.method", "ai_based")
    span.set_attribute("router.user_message", user_message[:100])
    
    # Classify intent with LLM
    intent = await self._classify_intent(user_message)
    
    span.set_attribute("router.intent", intent)
    span.set_attribute("router.executor", executor_name)
```

**Tool Executor Span:**

```python
with tracer.start_as_current_span("workflow.executor.tool") as span:
    span.set_attribute("executor.type", "tool")
    span.set_attribute("tool.name", "weather")
    span.set_attribute("tool.location", location)
    
    # Call MCP
    result = await tool_agent.execute(message)
    
    span.set_attribute("tool.result.length", len(result))
```

### 7.4. GenAI Semantic Conventions

OpenTelemetry GenAI Standard Attributes:

| Attribute | Description | Example Value |
|------|------|--------|
| `gen_ai.system` | AI system type | `azure_openai` |
| `gen_ai.request.model` | Model name | `gpt-4o` |
| `gen_ai.request.temperature` | Temperature setting | `0.7` |
| `gen_ai.prompt` | Input prompt | `"What is RAG?"` |
| `gen_ai.completion` | LLM response | `"RAG is..."` |
| `gen_ai.usage.prompt_tokens` | Input token count | `15` |
| `gen_ai.usage.completion_tokens` | Output token count | `120` |

---

## 8. Content Recording (Prompt/Completion)

### 8.1. What is Content Recording?

Content Recording is a feature that **includes Prompts (input) and Completions (output) in Tracing**.

**When Activated:**
- ✅ View exact Prompts in Tracing UI
- ✅ View complete LLM response content
- ✅ Optimize prompt engineering
- ✅ Quality analysis and debugging

**When Deactivated:**
- ❌ Prompt/Completion content not displayed
- ✅ Only metadata collected (model name, token count, duration)
- ✅ Protect sensitive information
- ✅ Save storage space

### 8.2. Activation Method

```bash
# Set environment variable
AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true
```

### 8.3. Recommended Settings by Environment

| Environment | Recording | Sampling | Masking | Notes |
|------|----------|--------|--------|------|
| **Dev** | ✅ ON | 100% | Optional | Detailed debugging |
| **Staging** | ✅ ON | 50% | ✅ Recommended | Validate with real data |
| **Prod (non-sensitive)** | ✅ ON | 10-20% | ✅ Recommended | Quality analysis |
| **Prod (sensitive)** | ❌ OFF | N/A | N/A | Regulatory compliance |

### 8.4. PII Masking Implementation

Masking utility for sensitive information protection:

**`src/foundry_agent/masking.py` or `src/agent_framework/masking.py`:**

```python
import re

def mask_text(text: str, mode: str = "standard") -> str:
    """
    PII masking utility
    
    Args:
        text: Original text
        mode: "standard" | "strict" | "off"
    """
    if mode == "off":
        return text
    
    # Email masking
    text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        '[EMAIL]',
        text
    )
    
    # Phone number masking
    text = re.sub(
        r'\b\d{2,3}-\d{3,4}-\d{4}\b',
        '[PHONE]',
        text
    )
    
    if mode == "strict":
        # Card number masking
        text = re.sub(
            r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            '[CARD]',
            text
        )
        
        # Social security number masking
        text = re.sub(
            r'\b\d{6}-[1-4]\d{6}\b',
            '[SSN]',
            text
        )
    
    return text
```

**Usage Example:**

```python
from masking import mask_text

masking_mode = os.getenv("AGENT_MASKING_MODE", "standard")

with tracer.start_as_current_span("llm_call") as span:
    span.set_attribute("gen_ai.prompt", mask_text(user_message, masking_mode))
    
    response = await llm_call()
    
    span.set_attribute("gen_ai.completion", mask_text(response, masking_mode))
```

---

## 9. Instrumentation Order (Order Matters!)

OpenTelemetry instrumentation **order is very important**. Initializing in the wrong order can result in missing telemetry.

### 9.1. Correct Initialization Order

```python
# ✅ Step 1: configure_azure_monitor() first!
configure_azure_monitor(
    connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
)

# ✅ Step 2: Enable instrumentation libraries
AIInferenceInstrumentor().instrument()  # Track LLM calls
FastAPIInstrumentor.instrument_app(app)  # Track HTTP requests (Agent Framework)

# ✅ Step 3: Create AIProjectClient (logging_enable=True)
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint,
    logging_enable=True
)

# ✅ Step 4: Create and use Agent
agent = project_client.agents.create_agent(...)
```

### 9.2. Incorrect Order (Anti-pattern)

```python
# ❌ Wrong example: Create AIProjectClient first
project_client = AIProjectClient(...)  # Created before configure_azure_monitor()

configure_azure_monitor(...)  # Too late!
AIInferenceInstrumentor().instrument()  # Already created client won't be instrumented

# Result: LLM calls are not tracked
```

---

## 10. Complete Environment Variables Guide

### 10.1. Required Environment Variables

| Variable | Category | Description |
|------|------|------|
| `APPLICATIONINSIGHTS_CONNECTION_STRING` | Required | Application Insights connection string |
| `OTEL_SERVICE_NAME` | Required | Service name (for Tracing filtering) |
| `PROJECT_CONNECTION_STRING` | Required | Azure AI Foundry Project connection |

### 10.2. Monitoring Related Variables

| Variable | Default Value | Description |
|------|--------|------|
| `OTEL_METRICS_EXPORTER` | `azure_monitor` | Specify metrics exporter |
| `OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED` | `true` | Enable automatic logging |

### 10.3. Tracing Related Variables

| Variable | Default Value | Description |
|------|--------|------|
| `OTEL_TRACES_EXPORTER` | `azure_monitor` | Specify Trace exporter |
| `OTEL_LOGS_EXPORTER` | `azure_monitor` | Specify Log exporter |
| `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED` | `false` | Display Prompt/Completion |

### 10.4. Sampling Related Variables (Optional)

| Variable | Example Value | Description |
|------|---------|------|
| `OTEL_TRACES_SAMPLER` | `parentbased_traceidratio` | Sampling strategy |
| `OTEL_TRACES_SAMPLER_ARG` | `0.2` | Sampling ratio (20%) |

### 10.5. Other Variables

| Variable | Example Value | Description |
|------|---------|------|
| `SEARCH_ENDPOINT` | `https://xxx.search.windows.net/` | AI Search endpoint (for RAG) |
| `SEARCH_KEY` | `...` | AI Search admin key |
| `MCP_ENDPOINT` | `https://mcp-xxx.azurecontainerapps.io` | MCP server endpoint |
| `AGENT_MASKING_MODE` | `standard` | PII masking mode (`standard`/`strict`/`off`) |

---

## 11. Operational Strategy

### 11.1. Content Recording Strategy

| Environment | Recording | Additional Recommendations | Notes |
|------|----------|-----------|------|
| **Development** | ✅ ON | Detailed debugging | Record all requests |
| **Staging** | ✅ ON + Masking | Validate with real data | PII masking required |
| **Production (non-sensitive)** | ✅ ON + Sampling (10-20%) | Cost optimization | For quality analysis |
| **Production (sensitive)** | ❌ OFF | Regulatory compliance | Collect metadata only |

### 11.2. Cost Optimization Strategy

**1. Apply Sampling** (see section 12)
- 10-20% sampling in high-traffic environments
- 100% collection for important requests (errors, slow requests)

**2. Adjust Data Retention Period**
- Set Application Insights retention period (30-90 days)
- Move old data to Archive Storage

**3. Selective Content Recording Use**
- OFF or sampled in Prod environment
- Temporarily enable only when investigating issues

---

## 12. Sampling Configuration

### 12.1. What is Sampling?

Sampling is a technique to **track only some requests, not all** to save cost and storage space.

### 12.2. How to Configure Sampling

```bash
# Set environment variables
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.2  # 20% sampling
```

### 12.3. Sampling Strategy

| Traffic Volume | Sampling Ratio | Description |
|-----------|-----------|------|
| Low (< 1000/day) | 100% (1.0) | Track all requests |
| Medium (1000-10000/day) | 50% (0.5) | Half sampling |
| High (> 10000/day) | 10-20% (0.1-0.2) | Cost optimization |

### 12.4. Precautions

- 🔴 Low sampling ratio may miss rare errors
- 🟡 Temporarily recommend 100% sampling when investigating issues
- 🟢 Sampling only affects Tracing (Monitoring metrics are always 100%)

---

## 13. Kusto Query Examples

### 13.1. Verify Content Recording

```kusto
dependencies
| where timestamp > ago(30m)
| where name contains "ChatCompletions" or customDimensions has "gen_ai.prompt"
| summarize count() by bin(timestamp, 5m)
```

### 13.2. Query Recent Prompt/Completion

```kusto
dependencies
| where timestamp > ago(30m)
| where customDimensions has "gen_ai.prompt"
| project 
    timestamp, 
    name, 
    prompt = customDimensions["gen_ai.prompt"],
    completion = customDimensions["gen_ai.completion"],
    duration
| take 10
```

### 13.3. Aggregate Call Count by Minute

```kusto
dependencies
| where timestamp > ago(1h)
| summarize calls = count() by bin(timestamp, 5m)
| order by timestamp desc
```

### 13.4. Error Tracking

```kusto
traces
| where timestamp > ago(1h)
| where severityLevel >= 3  // Error and above
| project timestamp, message, customDimensions
| take 20
```

### 13.5. Slow Request Analysis

```kusto
dependencies
| where timestamp > ago(1h)
| where duration > 3000  // Over 3 seconds
| project timestamp, name, duration, customDimensions
| order by duration desc
| take 20
```

---

## 14. Troubleshooting Guide

### 14.1. When Metrics Show 0

| Symptom | Cause | Solution |
|------|------|--------|
| Application Analytics shows 0 | Container App not deployed | Check Container App deployment |
| | CONNECTION_STRING missing | Check environment variables and redeploy |
| | Insufficient call volume | Execute at least 10 requests |
| | Time range error | Adjust time range in Portal |

### 14.2. When Tracing is Empty

| Symptom | Cause | Solution |
|------|------|--------|
| No tracing data | `configure_azure_monitor()` order error | Check initialization order (Section 9) |
| | TRACES_EXPORTER not set | Set `OTEL_TRACES_EXPORTER=azure_monitor` |
| | Instrumentation missing | Check `AIInferenceInstrumentor().instrument()` call |

### 14.3. When Prompt/Completion is Not Displayed

| Symptom | Cause | Solution |
|------|------|--------|
| No Input/Output | Recording flag OFF | `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true` |
| | Span attributes not set | Add `gen_ai.prompt`, `gen_ai.completion` attributes |
| | Not redeployed | Build new image and redeploy |

### 14.4. General Debugging Procedures

1. **Check Container App logs:**
   ```bash
   az containerapp logs show \
     --name <app-name> \
     --resource-group <rg> \
     --follow
   ```

2. **Verify environment variables:**
   ```bash
   az containerapp show \
     --name <app-name> \
     --resource-group <rg> \
     --query properties.template.containers[0].env
   ```

3. **Test Application Insights connection:**
   ```bash
   az monitor app-insights component show \
     --app <app-name> \
     --resource-group <rg>
   ```

---

## 15. Checklist

### 15.1. Monitoring Activation Checklist

- [ ] Set `APPLICATIONINSIGHTS_CONNECTION_STRING` environment variable
- [ ] Call `configure_azure_monitor()` (before creating AIProjectClient)
- [ ] Call `AIInferenceInstrumentor().instrument()`
- [ ] Create `AIProjectClient(logging_enable=True)`
- [ ] Deploy to Container App
- [ ] Execute 10+ test requests
- [ ] Verify metrics in Portal after 5-10 minutes

### 15.2. Tracing Activation Checklist

- [ ] Complete all Monitoring checklist items
- [ ] Set `OTEL_TRACES_EXPORTER=azure_monitor`
- [ ] Set `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true`
- [ ] (Agent Framework) Add FastAPI instrumentation
- [ ] (Agent Framework) Implement custom Spans
- [ ] Redeploy Container App
- [ ] Verify Span Tree in Portal Tracing tab

### 15.3. Production Readiness Checklist

- [ ] Implement PII masking (Prod environment)
- [ ] Configure sampling (high-traffic environment)
- [ ] Set up alerts (error rate, response time)
- [ ] Configure data retention period
- [ ] Set up cost monitoring dashboard

---

## 16. FAQ

**Q1: Will metrics be collected when running from Notebook?**  
A: No. Monitoring only supports services deployed to Container App. Notebook execution is one-time and not aggregated.

**Q2: Is it okay to use Content Recording in production?**  
A: Yes if there's no sensitive information, but we recommend applying sampling (10-20%) and PII masking together.

**Q3: Can I enable only one of Tracing or Monitoring?**  
A: Tracing requires Monitoring to be configured first. Monitoring can be used independently.

**Q4: Does sampling affect metrics too?**  
A: No. Sampling only affects Tracing, while Monitoring metrics are always collected at 100%.

**Q5: Why don't metrics appear immediately in Portal?**  
A: Application Insights has a 5-10 minute data delay. Wait after executing sufficient requests (10+).

---

## 17. References

### Official Documentation
- [Azure Monitor OpenTelemetry](https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-enable)
- [Azure AI Foundry Tracing](https://learn.microsoft.com/azure/ai-foundry/concepts/tracing)
- [OpenTelemetry Python SDK](https://opentelemetry-python.readthedocs.io/)
- [GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

### Related Labs
- [Lab 3: Deploy Foundry Agent without MAF](./03_deploy_foundry_agent.ipynb)
- [Lab 4: Deploy Foundry Agent with MAF](./04_deploy_foundry_agent_with_maf.ipynb)

### Additional Resources
- [Azure Monitor Pricing](https://azure.microsoft.com/pricing/details/monitor/)
- [Application Insights Sampling](https://learn.microsoft.com/azure/azure-monitor/app/sampling)
- [PII Data Protection Best Practices](https://learn.microsoft.com/azure/architecture/framework/security/design-storage)

---

**✅ Complete!** Through this guide, you can implement perfect observability for your Azure AI Foundry Agent system.

💡 **Tip:** Refer to the simple summary in README during early labs, and use this document for detailed tuning or operations!

🏠 [Back to README.md](./README.md)
