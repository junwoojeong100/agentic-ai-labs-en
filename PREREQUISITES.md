# Prerequisites Guide

This document is a detailed guide on the prerequisites for conducting the Azure AI Foundry Agent lab.

## 📋 Table of Contents

1. [Lab Environment Selection](#lab-environment-selection)
2. [GitHub Codespace Environment](#github-codespace-environment)
3. [Local Environment Setup](#local-environment-setup)
4. [Azure Subscription and Permissions](#azure-subscription-and-permissions)
5. [Permission Verification Methods](#permission-verification-methods)

---

## Lab Environment Selection

This lab is designed based on **Dev Container** to provide a consistent development environment.

### Option 1: GitHub Codespace ⭐ (Recommended)

**Cloud-based development environment - Start immediately without installation!**

**Codespace Advantages:**
- ✅ Pre-configured development environment (tools installed automatically)
- ✅ Cloud-based, accessible from anywhere
- ✅ Provides consistent lab environment
- ✅ Saves local machine resources
- ✅ No OS-specific configuration differences

**How to Start Codespace:**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/junwoojeong100/agentic-ai-labs?quickstart=1)

---

### Option 2: Local VS Code + Dev Container

**Use the same environment locally - Just install Docker!**

**Requirements:**
- ✅ Docker Desktop installed
- ✅ Visual Studio Code installed
- ✅ VS Code "Dev Containers" extension installed

**How to Start:**
1. Run Docker Desktop
2. Open this repository in VS Code
3. Click the `><` icon in the bottom left
4. Select "Reopen in Container"
5. All tools and packages install automatically! (takes 5-10 minutes)

> **💡 What is Dev Container?**  
> Based on `.devcontainer/devcontainer.json` configuration, it automatically sets up a development environment inside a Docker container.  
> The **exact same environment** as GitHub Codespaces runs locally!

**Detailed Guide:** See [DEVCONTAINER.md](./DEVCONTAINER.md)

---

### Option 3: Local Environment (Without Dev Container)

**If not using Dev Container - Manual setup required.**

> ⚠️ **Not Recommended**: Problems may occur due to OS-specific configuration differences, firewalls, network policies, etc.  
> **Strongly recommend using Option 1 (Codespace) or Option 2 (Local Dev Container).**

For this option, refer to the [Local Environment Setup](#local-environment-setup) section.

---

## Dev Container Auto-Configuration Environment

> 💡 **When using GitHub Codespaces or local VS Code + Dev Container**  
> All tools and packages below are **automatically installed** according to `.devcontainer/devcontainer.json` configuration.

### Automatically Installed Tools

When Codespace starts, the following are automatically installed:

#### Basic Tools and Runtime

| Tool | Version | Purpose |
|------|------|------|
| **Azure Developer CLI (azd)** | Latest | Infrastructure deployment |
| **Azure CLI (az)** | Latest | Azure resource management |
| **Python** | 3.12 | Agent and server development |
| **Docker** | Latest | Container build |
| **Git** | Latest | Version control |
| **Node.js** | Latest | Tool dependencies |

#### Python Virtual Environment

The `.venv` virtual environment is automatically created and activated:

```bash
# Virtual environment automatically activated
source .venv/bin/activate

# Jupyter kernel also automatically registered
jupyter kernelspec list
```

#### VS Code Extensions (Auto-installed)

| Extension | ID | Purpose |
|------|-----|------|
| **Python** | ms-python.python | Python development |
| **Pylance** | ms-python.vscode-pylance | Python language server |
| **Jupyter** | ms-toolsai.jupyter | Notebook execution |
| **Azure Developer CLI** | ms-azuretools.azure-dev | azd integration |
| **Azure Resources** | ms-azuretools.vscode-azureresourcegroups | Azure resource management |
| **Bicep** | ms-azuretools.vscode-bicep | IaC development |
| **GitHub Copilot** | GitHub.copilot | AI code assistant |
| **GitHub Copilot Chat** | GitHub.copilot-chat | AI chat |

### Python Packages (Auto-installed)

The following packages are automatically installed in `.venv`:

#### Azure AI and Core Services

```txt
azure-identity>=1.17.0
azure-core>=1.30.0
azure-ai-projects>=1.0.0b5
azure-ai-evaluation>=1.0.0
azure-ai-inference>=1.0.0b6
azure-search-documents>=11.4.0
openai>=1.51.0
python-dotenv>=1.0.0
requests>=2.31.0
```

#### API Server

```txt
fastapi>=0.110.0
uvicorn>=0.30.0
httpx>=0.27.0
```

#### Observability

```txt
azure-monitor-opentelemetry>=1.6.0
azure-monitor-opentelemetry-exporter>=1.0.0b27
opentelemetry-api>=1.20.0
opentelemetry-sdk>=1.20.0
opentelemetry-instrumentation-fastapi>=0.45b0
```

#### Agent Framework (Lab 5) & MCP

```txt
agent-framework>=1.0.0b251016
mcp>=1.1.0
```

#### Jupyter Notebook

```txt
jupyter>=1.0.0
ipykernel>=6.29.0
```

### Codespace Resources

**Default Provided Resources (GitHub Codespaces):**
- CPU: 2-4 cores
- RAM: 8-16 GB
- Storage: 32 GB

**Free Tier (Personal Account):**
- 120 core hours per month
- 15 GB storage per month

**Local Dev Container:**
- Uses local machine's Docker Desktop resources
- CPU/memory allocation adjustable in settings

---

## Local Environment Setup (Without Dev Container)

> ⚠️ **This section only applies if you are NOT using Dev Container.**  
> If using **GitHub Codespaces** or **local VS Code + Dev Container**, skip this section.

To proceed with the lab locally without Dev Container, you must manually install the following.

> ⚠️ **Warning**: In a local environment, problems may occur due to OS-specific configuration differences, firewalls, network policies, etc. **Strongly recommend using GitHub Codespace or local Dev Container.**

### Required Tool Installation

#### 1. Azure Developer CLI (azd)

**macOS/Linux:**
```bash
curl -fsSL https://aka.ms/install-azd.sh | bash
```

**Windows (PowerShell):**
```powershell
powershell -ex AllSigned -c "Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression"
```

**Verify Installation:**
```bash
azd version
```

#### 2. Azure CLI

**macOS:**
```bash
brew install azure-cli
```

**Linux (Ubuntu/Debian):**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Windows:**
- Download MSI installer from [download page](https://learn.microsoft.com/cli/azure/install-azure-cli-windows)

**Verify Installation:**
```bash
az version
```

#### 3. Python 3.11+

**macOS:**
```bash
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)

**Verify Installation:**
```bash
python3 --version
```

#### 4. Docker Desktop

- [Download Docker Desktop](https://www.docker.com/products/docker-desktop)

**Verify Installation:**
```bash
docker --version
docker compose version
```

#### 5. Visual Studio Code

- [Download VS Code](https://code.visualstudio.com/)

**Install Required Extensions:**
```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-azuretools.azure-dev
code --install-extension ms-azuretools.vscode-azureresourcegroups
```

### Local Environment Setup

```bash
# Clone repository
git clone https://github.com/junwoojeong100/agentic-ai-labs.git
cd agentic-ai-labs

# Create Python virtual environment
python3 -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Register Jupyter kernel
python -m ipykernel install --user --name=agentic-ai-labs --display-name="Python 3.12 (agentic-ai-labs)"
```

---

## Azure Subscription and Permissions

### Required Azure Resources

This lab creates the following Azure resources:

| Resource | Purpose | Estimated Cost/Month |
|--------|------|-------------|
| Azure AI Foundry (AIServices) | Agent service + OpenAI model integration | $20-50 (usage-based) |
| Azure AI Search | RAG search | $10-30 |
| Azure Container Apps | Container hosting | $10-20 |
| Azure Container Registry | Image storage | $5 |
| Azure Key Vault | Secret management | $1 |
| Azure Storage Account | Data storage | $5 |
| **Total Estimated Cost** | | **$51-131** |

> 💡 **Note**: AI Foundry is a unified resource that integrates Azure OpenAI, Agents, Evaluations, etc.  
> No need to create a separate Azure OpenAI resource; models are automatically deployed within AI Foundry.

> 💡 **Tip**: You can minimize costs by deleting the resource group immediately after completing the lab.

---

### Recommended Setup: Subscription Owner ⭐

> **📚 Lab Recommendations**
>
> This lab is designed to be conducted with **Subscription Owner (`Owner`) role**.
> 
> Manually configuring individual roles is complex and time-consuming.  
> The individual role descriptions in the sections below are for **educational purposes and production environment reference**.

**Lab Procedure:**

1. **Verify Subscription Owner Permission** (Required)
   - Verify you have `Owner` role on existing subscription
   - Or create a separate lab-dedicated subscription ([Subscription Creation Guide](https://learn.microsoft.com/azure/cost-management-billing/manage/create-subscription))

2. **Permission Verification Commands:**
   ```bash
   # Azure login
   az login

   # Verify subscription Owner role
   az role assignment list \
     --assignee $(az ad signed-in-user show --query id -o tsv) \
     --role Owner \
     --scope /subscriptions/$(az account show --query id -o tsv) \
     -o table
   ```

3. **Example Output (If Owner):**
   ```
   Principal                            Role    Scope
   -----------------------------------  ------  --------------------------------------------------
   user@example.com                     Owner   /subscriptions/12345678-1234-1234-1234-123456789012
   ```

**Advantages:**
- ✅ Automatic resource creation and role assignment
- ✅ No lab interruptions due to permission issues
- ✅ Bicep template automatically assigns necessary roles
- ✅ Faster lab progress (no permission setup required)

**⚠️ Precautions:**
- Recommended to use a **separate learning/development subscription** rather than production subscription
- Delete resource group immediately after lab completion to minimize costs
- Estimated cost: $50-130 (with immediate resource deletion)


---

## Permission Verification Methods

### ✅ Step 1: Azure Login and Subscription Verification

```bash
# Azure login
az login

# Verify current subscription
az account show --query "{Name:name, ID:id, TenantID:tenantId}" -o table

# Change subscription if multiple subscriptions exist
az account set --subscription "<subscription-ID>"
```

---

### ✅ Step 2: Verify Subscription Owner Permission (Required)

```bash
# Verify subscription Owner role
az role assignment list \
  --assignee $(az ad signed-in-user show --query id -o tsv) \
  --role Owner \
  --scope /subscriptions/$(az account show --query id -o tsv) \
  -o table
```

**✅ If Owner (lab possible):**
```
Principal                            Role    Scope
-----------------------------------  ------  --------------------------------------------------
user@example.com                     Owner   /subscriptions/12345678-1234-1234-1234-123456789012
```

**❌ If not Owner:**
```
(No output or only other roles displayed)
```

➡️ **Action:** Request Owner role from subscription administrator or create separate lab-dedicated subscription

---

### ✅ Step 3: Verify Resource Provider Registration Status

```bash
# Verify required resource provider registration status
az provider list --query "[?namespace=='Microsoft.CognitiveServices' || namespace=='Microsoft.Search' || namespace=='Microsoft.App' || namespace=='Microsoft.Storage' || namespace=='Microsoft.KeyVault' || namespace=='Microsoft.ContainerRegistry'].{Provider:namespace, Status:registrationState}" -o table
```

**✅ If all registered:**
```
Provider                          Status
--------------------------------  ----------
Microsoft.CognitiveServices       Registered
Microsoft.Search                  Registered
Microsoft.App                     Registered
Microsoft.ContainerRegistry       Registered
Microsoft.Storage                 Registered
Microsoft.KeyVault                Registered
```

**❌ If unregistered providers exist:**
```bash
# Batch register required providers (Owner permission required)
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Search
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.ContainerRegistry
az provider register --namespace Microsoft.Storage
az provider register --namespace Microsoft.KeyVault
az provider register --namespace Microsoft.OperationalInsights

# Wait for registration completion (takes 2-5 minutes)
# Recheck registration status
az provider list --query "[?namespace=='Microsoft.CognitiveServices' || namespace=='Microsoft.Search' || namespace=='Microsoft.App' || namespace=='Microsoft.Storage' || namespace=='Microsoft.KeyVault'].{Provider:namespace, Status:registrationState}" -o table
```


### ✅ Step 4: Verify Azure Quota (Optional)

```bash
# Verify current subscription ID
SUBSCRIPTION_ID=$(az account show --query id -o tsv)
echo "Subscription ID: $SUBSCRIPTION_ID"

# Verify preferred region (e.g., eastus, koreacentral)
LOCATION="eastus"

# Verify AI Foundry/OpenAI quota (SKU list)
az cognitiveservices account list-skus --location $LOCATION -o table
```

> **💡 Tip:** If quota shortage error occurs, try a different region or request quota increase from Azure support team

---

### 📋 Permission Verification Checklist

Verify all of the following before starting the lab:

- [ ] Azure login complete (`az login`)
- [ ] Subscription Owner role verified
- [ ] Required resource providers registered (6)
- [ ] (Optional) Quota verified and region selected

**If all checked, you're ready to start the lab!** 🎉

---

## Roles Required by Notebook

Reference material organizing Azure RBAC roles required for each Notebook.

### Lab 01: Azure Resource Deployment (`01_deploy_azure_resources.ipynb`)

**User Account (👤):**
- `Owner` (subscription level) - Resource creation and role assignment

**Auto-assigned Roles (Bicep):**
- User Account: `Azure AI User`, `Cognitive Services User`, `Storage Blob Data Contributor`
- Managed Identity: `Azure AI User`, `Cognitive Services User`

> **💡 Note - Principle of Least Privilege:**
> - Bicep grants the `Azure AI User` role following the principle of least privilege.
> - `Azure AI User` provides the minimum permissions needed for agent development and building in AI Foundry Project.
> - If more permissions are needed (e.g., Hub management, ML workspace operations), you can change to the `Azure AI Developer` role.

---

### Lab 02: AI Search RAG Configuration (`02_setup_ai_search_rag.ipynb`)

**User Account (👤):**
- `Cognitive Services User` - Call OpenAI embedding API
- `Search Service Contributor` - Create index schema
- `Search Index Data Contributor` - Upload documents
- `Storage Blob Data Contributor` - Read data files

**Managed Identity (🤖):**
- None

---

### Lab 03: Deploy Foundry Agent without MAF (`03_deploy_foundry_agent.ipynb`)

**User Account (👤):**
- `Azure AI User` - Create and manage Agents
- `Cognitive Services User` - Call OpenAI models

**Managed Identity (🤖) - Container Apps:**
- `Azure AI User` - Execute Agent runtime
- `Cognitive Services User` - Model inference
- `Search Index Data Reader` - RAG search

---

### Lab 04: Deploy Foundry Agent with MAF (`04_deploy_foundry_agent_with_maf.ipynb`)

**User Account (👤):**
- `Azure AI User` - Create and manage Agents
- `Cognitive Services User` - Call OpenAI models

**Managed Identity (🤖) - Container Apps:**
- `Azure AI User` - Execute Agent runtime
- `Cognitive Services User` - Model inference
- `Search Index Data Reader` - RAG search

---

### Lab 05: MAF Workflow Patterns (`05_maf_workflow_patterns.ipynb`)

**User Account (👤):**
- `Azure AI User` - Execute workflows, create Agents
- `Cognitive Services User` - Call model inference API

**Managed Identity (🤖):**
- None

---

### Lab 06: MAF Dev UI (`06_maf_dev_ui.ipynb`)

**Requirements:**
- Microsoft Agent Framework installation (same as Lab 5)
- **agent-framework-devui>=1.0.0b251007** - Dev UI package
  - Automatically installed via `requirements.txt`
  - Provides web server for workflow visualization
  - FastAPI-based server (port 8080)
- Web browser (for Dev UI access)
- Port 8080 available (Dev UI server default port)

**Key Features:**
- Workflow graph visualization (nodes and edges)
- Real-time node status monitoring
- Performance metrics and optimization guide
- Execution history storage and retrieval

**Optional:**
- Automatic port forwarding when using GitHub Codespaces (set host='0.0.0.0')

### Lab 07: Agent Evaluation (`07_evaluate_agents.ipynb`)

**User Account (👤):**
- `Azure AI User` - Execute evaluations, save results
- `Cognitive Services User` - Call evaluation models (Judge LLM)

**Managed Identity (🤖):**
- None

---

## Role Summary

**👤 Roles Required for User Account (All Notebooks):**
```
Subscription Level:
- Owner (or Contributor + User Access Administrator)

Resource Level (Auto-assigned by Bicep):
- Azure AI User
- Cognitive Services User
- Search Service Contributor
- Search Index Data Contributor
- Storage Blob Data Contributor
```

**🤖 Roles Required for Managed Identity (Lab 03-04 Container Apps):**
```
Resource Level (Auto-assigned by Bicep):
- Azure AI User
- Cognitive Services User
- Search Index Data Reader
```

> **💡 Note:** When executing `azd up` in Lab 01, Bicep automatically assigns required roles, so manual configuration is not needed.

---

## Next Steps

If you have met all prerequisites, proceed with the following:

1. ✅ [Quick Start Guide](./README.md#-quick-start)
2. ✅ [Lab 1: Azure Resource Deployment](./01_deploy_azure_resources.ipynb)
3. ✅ [Configuration Guide](./CONFIGURATION.md) (if needed)

---

## Related Documents

- [README.md](./README.md) - Project Overview
- [CONFIGURATION.md](./CONFIGURATION.md) - Environment Variable Guide
- [OBSERVABILITY.md](./OBSERVABILITY.md) - Observability Guide

---

**Built with ❤️ using Azure AI Foundry**
