# Configuration Guide

This document is a detailed guide on environment variables and settings for the Azure AI Foundry Agent system.

## 📋 Table of Contents

1. [Config.json Structure](#configjson-structure)
2. [Agent Container Environment Variables](#agent-container-environment-variables)
3. [Required vs Optional Variables](#required-vs-optional-variables)
4. [Content Recording Operations Guide](#content-recording-operations-guide)
5. [Change Application Procedure](#change-application-procedure)

---

## Config.json Structure

Settings automatically saved in `config.json` after deployment:

```json
{
  "resource_group": "rg-aiagent-xxxxx",
  "location": "eastus",
  "project_connection_string": "https://xxx.services.ai.azure.com/api/projects/yyy;subscription_id=...;resource_group=...",
  "search_endpoint": "https://srch-xxx.search.windows.net/",
  "search_service_name": "srch-xxx",
  "container_registry_endpoint": "crxxx.azurecr.io",
  "container_apps_environment_id": "/subscriptions/.../resourceGroups/.../providers/Microsoft.App/managedEnvironments/cae-xxx",
  "model_deployment_name": "gpt-4o",
  "model_version": "2024-11-20",
  "model_capacity": 50,
  "search_index": "ai-agent-knowledge-base",
  "mcp_endpoint": "https://mcp-server.xxx.azurecontainerapps.io",
  "agent_endpoint": "https://agent-service.xxx.azurecontainerapps.io",
  "agent_framework_endpoint": "https://agent-framework.xxx.azurecontainerapps.io"
}
```

### Key Field Descriptions

| Field | Description | Usage |
|------|------|------|
| `resource_group` | Resource group name | Azure resource management |
| `location` | Azure region | Deployment location |
| `project_connection_string` | Azure AI Foundry project connection string | Agent SDK connection |
| `search_endpoint` | Azure AI Search endpoint | RAG search |
| `search_service_name` | AI Search service name | Management operations |
| `search_index` | AI Search index name | RAG query target |
| `container_registry_endpoint` | Azure Container Registry endpoint | Docker image repository |
| `container_apps_environment_id` | Container Apps Environment ID | Container deployment target |
| `model_deployment_name` | Deployed OpenAI model name | Used for LLM calls |
| `model_version` | OpenAI model version | Model version tracking |
| `model_capacity` | Model capacity (TPM) | Throughput configuration |
| `mcp_endpoint` | Deployed MCP server endpoint | Tool invocation |
| `agent_endpoint` | Foundry Agent API server endpoint | REST API provision (Lab 3) |
| `agent_framework_endpoint` | Agent Framework API server endpoint | REST API provision (Lab 4) |

---

## Agent Container Environment Variables

When running Lab 3, the `src/foundry_agent/.env` file is **automatically generated**.

### Complete Environment Variable List

```properties
# ============================================
# Azure AI Foundry (Required)
# ============================================
PROJECT_CONNECTION_STRING=https://xxx.services.ai.azure.com/api/projects/yyy

# ============================================
# Azure AI Search - RAG (Required)
# ============================================
SEARCH_ENDPOINT=https://srch-xxx.search.windows.net/
SEARCH_KEY=xxx
SEARCH_INDEX=ai-agent-knowledge-base

# ============================================
# MCP Server (Required)
# ============================================
MCP_ENDPOINT=https://mcp-server.xxx.azurecontainerapps.io

# ============================================
# Application Insights (Required)
# ============================================
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=xxx;...

# ============================================
# OpenTelemetry Core (Required)
# ============================================
OTEL_SERVICE_NAME=azure-ai-agent
OTEL_TRACES_EXPORTER=azure_monitor
OTEL_METRICS_EXPORTER=azure_monitor
OTEL_LOGS_EXPORTER=azure_monitor
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

# ============================================
# GenAI Content Recording (Recommended)
# ============================================
AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true

# ============================================
# Sampling - High Traffic Environment Optimization (Optional)
# ============================================
# OTEL_TRACES_SAMPLER=parentbased_traceidratio
# OTEL_TRACES_SAMPLER_ARG=0.2   # 20% sampling

# ============================================
# PII Masking Policy (Optional)
# ============================================
# AGENT_MASKING_MODE=standard   # off|standard|strict
```

---

## Required vs Optional Variables

### Required Variables

| Variable | Description | No Default |
|------|------|------------|
| `PROJECT_CONNECTION_STRING` | AI Foundry Project identifier | ❌ |
| `SEARCH_ENDPOINT` | AI Search endpoint | ❌ |
| `SEARCH_KEY` | AI Search access key | ❌ |
| `SEARCH_INDEX` | RAG index name | ❌ |
| `MCP_ENDPOINT` | MCP server URL | ❌ |
| `APPLICATIONINSIGHTS_CONNECTION_STRING` | App Insights connection string | ❌ |
| `OTEL_SERVICE_NAME` | Service logical name | ❌ |

### Recommended Variables

| Variable | Description | Recommended Value |
|------|------|---------|
| `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED` | Prompt/Completion recording | `true` (dev), `false` (prod) |
| `OTEL_TRACES_EXPORTER` | Trace export target | `azure_monitor` |
| `OTEL_METRICS_EXPORTER` | Metrics export target | `azure_monitor` |
| `OTEL_LOGS_EXPORTER` | Logs export target | `azure_monitor` |

### Optional Variables

| Variable | Description | Example Value |
|------|------|---------|
| `OTEL_TRACES_SAMPLER` | Sampling strategy | `parentbased_traceidratio` |
| `OTEL_TRACES_SAMPLER_ARG` | Sampling ratio | `0.2` (20%) |
| `AGENT_MASKING_MODE` | PII masking level | `off`, `standard`, `strict` |

---

## Content Recording Operations Guide

### Environment-Specific Recommended Settings

| Environment | Content Recording | Sampling | Masking | Reason |
|------|-------------------|--------|--------|------|
| **Development** | ✅ `true` | ❌ Disabled | ❌ Not needed | Full debugging info required |
| **QA/Test** | ✅ `true` | ❌ Disabled | ⚠️ `standard` | Test data validation |
| **Staging** | ✅ `true` | ⚠️ 50% | ✅ `standard` | Real-like environment monitoring |
| **Production (non-sensitive)** | ✅ `true` | ✅ 10-20% | ✅ `strict` | Quality analysis + cost optimization |
| **Production (sensitive)** | ❌ `false` | ✅ 5-10% | ✅ `strict` | Regulatory compliance (GDPR, HIPAA) |

### Content Recording Details

**When Enabled (`true`)**
- ✅ Full Prompt and Completion are recorded in Trace
- ✅ Complete input/output viewable in Tracing UI
- ✅ Useful for debugging and quality analysis
- ⚠️ Possible exposure of sensitive information
- ⚠️ Increased storage costs

**When Disabled (`false`)**
- ❌ Prompt/Completion not recorded in Trace
- ✅ Only metadata recorded (token count, latency, etc.)
- ✅ Protection of sensitive information
- ✅ Reduced storage costs
- ⚠️ Difficult debugging

### Sampling Configuration

To reduce costs in high-traffic environments, enable sampling:

```properties
# 20% sampling (only 1 out of 5 requests recorded)
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.2
```

**Sampling Ratio Recommendations:**
- Development: 100% (no sampling)
- Staging: 50% (`0.5`)
- Production (low traffic): 20-50% (`0.2-0.5`)
- Production (high traffic): 5-10% (`0.05-0.1`)

### PII Masking

You can mask sensitive information using the `masking.py` utility:

```properties
# Set masking mode
AGENT_MASKING_MODE=standard
```

**Masking Levels:**
- `off`: Masking disabled (development environment)
- `standard`: Basic pattern masking (email, phone, card number)
- `strict`: Strict masking (additional name, address, etc.)

**Masking Targets (standard mode):**
- Email address: `user@example.com` → `[EMAIL]`
- Phone number: `010-1234-5678` → `[PHONE]`
- Credit card: `1234-5678-9012-3456` → `[CARD]`
- Social Security Number: `123456-1234567` → `[SSN]`

---

## Change Application Procedure

After changing environment variables, you must perform the following steps.

### 1. Edit .env File

```bash
# Edit .env file
nano src/foundry_agent/.env

# Or re-run the corresponding cell in Lab 3 notebook
```

### 2. Rebuild Docker Image

```bash
# Login to ACR
az acr login --name <your-acr-name>

# Build image
docker build -t <your-acr-name>.azurecr.io/agent-service:latest \
  src/foundry_agent/

# Push image
docker push <your-acr-name>.azurecr.io/agent-service:latest
```

### 3. Redeploy Container Apps

```bash
# Deploy new revision (automatically uses latest image)
az containerapp update \
  --name agent-service \
  --resource-group <resource-group> \
  --image <your-acr-name>.azurecr.io/agent-service:latest
```

### 4. Verify Changes

```bash
# Check environment variables
az containerapp show \
  --name agent-service \
  --resource-group <resource-group> \
  --query properties.template.containers[0].env

# Check logs
az containerapp logs show \
  --name agent-service \
  --resource-group <resource-group> \
  --tail 50
```

### 5. Verify Tracing (Optional)

Check immediately in Application Insights using Kusto query:

```kql
// Verify Content Recording enabled
dependencies
| where timestamp > ago(10m)
| where customDimensions.["gen_ai.system"] == "az.ai.agents"
| project timestamp, name, customDimensions.["gen_ai.prompt"], customDimensions.["gen_ai.completion"]
| take 10
```

---

## Important Notes ⚠️

1. **Included in Image Build**
   - `.env` file is included in Docker image
   - Must rebuild & redeploy after changing values

2. **Sensitive Key Security**
   - Do not commit `.env` file to Git
   - Verify it's included in `.gitignore`

3. **Sampling Precautions**
   - When sampling is enabled, only some requests are shown in Tracing UI
   - This is intended behavior

4. **Metrics Always Sent**
   - Metrics continue to be collected even when Content Recording is disabled
   - Call count, latency, error rate, etc. are unaffected

---

## Troubleshooting

### Environment Variables Not Applied

```bash
# Check container environment variables
az containerapp show --name agent-service --resource-group <rg> \
  --query properties.template.containers[0].env -o table

# Check if new revision is active
az containerapp revision list --name agent-service --resource-group <rg> \
  -o table
```

### Content Recording Not Visible

1. Verify `AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true`
2. Check Application Insights connection string is correct
3. Verify image rebuild and redeployment
4. Wait 5-10 minutes and check Tracing UI

### Sampling Ratio Different Than Expected

- Verify `OTEL_TRACES_SAMPLER_ARG` value is between 0 and 1
- Parent-based sampling follows the parent span's decision
- Some requests may always be sampled (e.g., when errors occur)

---

## Related Documents

- [OBSERVABILITY.md](./OBSERVABILITY.md) - Advanced observability guide
- [README.md](./README.md) - Project overview
- [PREREQUISITES.md](./PREREQUISITES.md) - Prerequisites

---

**Built with ❤️ using Azure AI Foundry**
