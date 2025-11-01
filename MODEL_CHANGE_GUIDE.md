# 🔄 Model Change Guide

This project is designed with **environment variable-centric architecture**, making it easy to change models without code modifications.

> **🎯 Key Summary**  
> **Change model in just 1 place!**  
> Simply change the `model_name` and `model_version` variables in Lab 1 notebook, and it will automatically apply to the entire project.

---

## 🎯 Recommended Workflow: Use Lab 1 Notebook

**The easiest way is to change the model settings in the Lab 1 notebook.**

### File: `01_deploy_azure_resources.ipynb`

**Section 4: Model Configuration** - Only modify these variables:

```python
# 👇 Just change these 2 lines!
model_name = "gpt-4o"          # Change model name
model_version = "2024-11-20"   # Change model version (varies by model)
model_capacity = 50            # TPM capacity (optional)

# Run cell to automatically set azd environment variables
```

**Automatically Processed:**
- ✅ Deploy model to Azure OpenAI
- ✅ Auto-generate `.env` files in Labs 3, 4
- ✅ All Agents use the same model

> **💡 Important:** 
> - GPT-4o family (`gpt-4o`, `gpt-4o-mini`) each use different versions
> - When using other models, you must specify the correct version for that model
> - Version check: [Azure OpenAI Models Documentation](https://learn.microsoft.com/azure/ai-services/openai/concepts/models)
> - No need to modify other files (`.env`, `main.bicep`, etc.)!

---

## 🌍 Region Change

Change only when you have quota limitations or specific region requirements.

### Change Location

**File:** `01_deploy_azure_resources.ipynb` - Section 3

```python
# 👇 Change this 1 line only when quota is insufficient!
location = "eastus"  # Change to 'eastus2', 'westus', 'swedencentral', etc.
```

### Recommended Regions

| Region | Recommended Use |
|------|----------|
| `eastus` | Default, supports most services |
| `eastus2` | When eastus quota is insufficient |
| `westus` | Preference for US West region |
| `swedencentral` | When Europe region is needed |
| `northeurope` | Alternative Europe option |

> **⚠️ Warning:** Azure OpenAI or AI Foundry may be restricted in some regions.  
> If deployment fails, check the error message and try a different region.

---

## 📋 Detailed Change Locations (Advanced)

### ✅ Infrastructure Level (Azure Deployment)

#### File: `infra/main.bicep`
```bicep
# Lines 34-40 parameter changes
param openAiModelName string = 'gpt-4o'        # 👈 Model name
param openAiModelVersion string = '2024-11-20'  # 👈 Version
param openAiModelCapacity int = 50              # 👈 Capacity (TPM)
```

**Or specify parameters during deployment:**
```bash
azd up --parameter openAiModelName=gpt-4o-mini --parameter openAiModelVersion=2024-07-18
```

---

### ✅ Application Level (Runtime)

#### File: `src/foundry_agent/.env`
```bash
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o  # 👈 Change only here
```

#### File: `src/agent_framework/.env`
```bash
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o  # 👈 Change only here
```

---

## 🚀 Quick Change Examples

### Change to GPT-4o Mini (Cost Savings)

**Lab 1 Notebook Method (Recommended):**
```python
# 01_deploy_azure_resources.ipynb Section 4
model_name = "gpt-4o-mini"     # 👈 Change to lightweight model
model_version = "2024-07-18"   # GPT-4o-mini version
model_capacity = 50

# Deploy after running cell
```

### Other Model Examples

```python
# GPT-4o (default, recommended)
model_name = "gpt-4o"
model_version = "2024-11-20"

# GPT-4o Mini (lightweight, low cost)
model_name = "gpt-4o-mini"
model_version = "2024-07-18"
```

**Manual Method:**
```bash
# 1. Set azd environment variables
azd env set openAiModelName gpt-4o-mini
azd env set openAiModelVersion 2024-07-18

# 2. Deploy infrastructure
azd provision

# 3. Modify environment variable file (foundry_agent)
sed -i 's/AZURE_AI_MODEL_DEPLOYMENT_NAME=.*/AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini/g' src/foundry_agent/.env

# 4. Modify environment variable file (agent_framework)
sed -i 's/AZURE_AI_MODEL_DEPLOYMENT_NAME=.*/AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini/g' src/agent_framework/.env

# 5. Redeploy containers (re-run Lab 3, Lab 4 notebooks)
```

---

## 🎯 Files That Don't Need Changes

### ✅ Automatically Processed Files (No Code Changes Needed)
- **`src/foundry_agent/main_agent.py`** - Automatically reads environment variables
- **`src/foundry_agent/research_agent.py`** - Automatically reads environment variables
- **`src/foundry_agent/tool_agent.py`** - Automatically reads environment variables
- **`src/foundry_agent/api_server.py`** - Dynamically retrieves model name
- **`src/agent_framework/*.py`** - Uses environment variables first

### 📝 Optional Updates
- **`src/foundry_agent/.env.example`** - Example file (for documentation)
- **`src/agent_framework/.env.example`** - Example file (for documentation)
- **`README.md`** - Project documentation (optional)
- **`MODEL_CHANGE_GUIDE.md`** - This file (optional)

---

## 📊 Supported Model List

## Supported Models

| Model Name | Version | Features |
|--------|------|------|
| `gpt-4o` | `2024-11-20` | Multimodal, fast response, cost-effective (recommended) |
| `gpt-4o-mini` | `2024-07-18` | Lightweight version, low cost |

**GPT-4o Family Key Features:**
- **Context Window**: 128,000 tokens
- **Multimodal**: Supports text and image input
- **Fast Response**: Quick response speed
- **Tool Support**: Function calling and tool integration
- **Cost Effective**: More cost-efficient than previous models
- **Training Data**: Data up to October 2023

> **Note**: Use versions supported by Azure OpenAI Service.  
> [Azure OpenAI Models Documentation](https://learn.microsoft.com/azure/ai-services/openai/concepts/models)

---

## 🔍 Environment Variable Priority

The project selects models in the following priority order:

```
1. Constructor parameter (directly specified in code)
   ↓ (if not specified)
2. Environment variable (AZURE_AI_MODEL_DEPLOYMENT_NAME)
   ↓ (if not specified)
3. Default value (gpt-4o) + warning log
```

**Example:**
```python
# foundry_agent/main_agent.py
self.model = model or os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o")
#           ↑ 1st priority    ↑ 2nd priority environment variable                           ↑ 3rd priority default value
```

---

## ✅ Checklist

When changing models, check the following items:

### When Using Lab Notebooks
- [ ] **Lab 1**: Change model settings in `01_deploy_azure_resources.ipynb` Section 4
- [ ] **Deploy**: Run notebook cell to set azd environment variables
- [ ] **Infrastructure**: Run `azd provision` (or re-run entire Lab 1)
- [ ] **Verify**: Check OpenAI model deployment in Azure Portal
- [ ] **Agent Deployment**: Auto-generate .env files and redeploy containers in Lab 3, Lab 4 notebooks
- [ ] **Test**: Verify Agent operates correctly

### When Changing Manually
- [ ] **Infrastructure**: Set environment variables using `azd env set` command
- [ ] **Foundry Agent**: Change `AZURE_AI_MODEL_DEPLOYMENT_NAME` in `src/foundry_agent/.env` file
- [ ] **Agent Framework**: Change `AZURE_AI_MODEL_DEPLOYMENT_NAME` in `src/agent_framework/.env` file
- [ ] **Deploy**: Run `azd provision` to deploy new model
- [ ] **Containers**: Rebuild Docker images and redeploy Container Apps
- [ ] **Test**: Test Agent API

---

## 💡 Tips

### Notebook vs Manual Changes

**Using Notebooks (Recommended):**
- ✅ Easy configuration changes
- ✅ Automatic validation
- ✅ Step-by-step guide
- ✅ Optimized for hands-on learning

**Manual Changes:**
- 🔧 When building CI/CD pipelines
- 🔧 Production environment automation
- 🔧 Script-based deployment

### Local Development vs Deployment Environment

```bash
# Local development: Only modify .env file
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini

# Update Azure Container Apps environment variables directly
az containerapp update \
  --name agent-service \
  --resource-group <rg-name> \
  --set-env-vars AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini

# Or regenerate .env and redeploy from Lab 3/4 notebooks (recommended)
```

### Using Multiple Models Simultaneously

You can use different models for each Agent:

```python
# Main Agent uses gpt-4o (latest model)
main_agent = MainAgent(client, model="gpt-4o")

# Research Agent uses gpt-4o (same model)
research_agent = ResearchAgent(client, ..., model="gpt-4o")

# Tool Agent uses gpt-4o-mini (cost savings)
tool_agent = ToolAgent(client, model="gpt-4o-mini")

# Simple tasks handled with gpt-4o-mini
simple_agent = SimpleAgent(client, model="gpt-4o-mini")
```

### Verify Model After Deployment

```bash
# Check Azure OpenAI deployment
az cognitiveservices account deployment list \
  --name <openai-account-name> \
  --resource-group <rg-name> \
  --query "[].{Name:name, Model:properties.model.name, Version:properties.model.version}" \
  --output table

# Check Container Apps environment variables
az containerapp show \
  --name agent-service \
  --resource-group <rg-name> \
  --query "properties.template.containers[0].env" \
  --output table
```

---

## 📚 References

- [Azure OpenAI Service Models](https://learn.microsoft.com/azure/ai-services/openai/concepts/models)
- [GPT-4o Documentation](https://platform.openai.com/docs/models/gpt-4o)
- [README.md - Model Change Section](./README.md#changing-models)
- [Lab 1 Notebook](./01_deploy_azure_resources.ipynb)

---

**Built with ❤️ for easy model switching**
