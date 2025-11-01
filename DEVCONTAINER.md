# Dev Container Setup Guide

This project provides a consistent development environment using Dev Container.

## 🚀 Quick Start

### 1. Open Dev Container

**In VS Code:**
1. Open this repository in VS Code
2. Click the remote icon in the bottom left (><)
3. Select "Reopen in Container"
4. Container build and setup completes automatically (takes 5-10 minutes on first run)

**In GitHub Codespaces:**
1. Click the "Code" button on the GitHub repository page
2. Select the "Codespaces" tab
3. Click "Create codespace on main"

### 2. Verify Setup Completion

When the container starts, the following tasks are automatically performed:

```bash
✅ Install Python 3.12
✅ Create virtual environment (.venv)
✅ Install required packages
✅ Register Jupyter kernel
✅ Install Azure CLI, Azure Developer CLI
```

Verify in terminal:

```bash
# Check Python version
python --version  # Python 3.12.x

# Verify virtual environment activation
which python  # /workspaces/agentic-ai-labs/.venv/bin/python

# Verify package installation
pip list | grep azure
```

### 3. Run Notebook

1. Open `.ipynb` file in VS Code
2. Click "Select Kernel" in the top right
3. Select "Python 3.12 (agentic-ai-labs)"
4. Start running cells!

## 📦 Included Tools

- **Python 3.12**: Latest Python runtime
- **Azure CLI**: Azure resource management
- **Azure Developer CLI (azd)**: Infrastructure deployment
- **Docker**: Container build and execution
- **Git**: Version control

## 📚 Installed Python Packages

All required packages are defined in `requirements.txt`:

- **Azure SDK**: identity, core, ai-projects (1.0.0b5), ai-inference (1.0.0b6), ai-evaluation, search-documents
- **OpenAI SDK**: GPT models and embedding API
- **Agent Framework**: Microsoft Agent Framework (1.0.0b251016)
- **Agent Framework Dev UI**: agent-framework-devui (1.0.0b251007) - Workflow visualization tool
- **MCP**: Model Context Protocol
- **FastAPI & Uvicorn**: API server
- **OpenTelemetry**: Observability and monitoring
- **Jupyter**: Notebook support

## 🔧 Manual Setup (Without Dev Container)

If not using Dev Container:

```bash
# 1. Verify Python 3.12 installation
python --version

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Install packages
pip install --upgrade pip
pip install -r requirements.txt

# 5. Register Jupyter kernel
python -m ipykernel install --user --name=agentic-ai-labs --display-name "Python 3.12 (agentic-ai-labs)"
```

## 🆘 Troubleshooting

### If Packages Are Not Installed

```bash
# Verify virtual environment activation
source .venv/bin/activate

# Manually reinstall packages
pip install -r requirements.txt
```

### If Jupyter Kernel Not Visible

```bash
# Re-register kernel
source .venv/bin/activate
python -m ipykernel install --user --name=agentic-ai-labs --display-name "Python 3.12 (agentic-ai-labs)"
```

### Rebuild Dev Container

1. Open VS Code Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`)
2. Type and select "Dev Containers: Rebuild Container"
3. Container will be rebuilt from scratch

## 📝 Additional Information

- **Virtual Environment Path**: `.venv/`
- **Setup Script**: `.devcontainer/setup.sh`
- **Package List**: `requirements.txt`
- **Dev Container Configuration**: `.devcontainer/devcontainer.json`

## 🎯 Next Steps

Once Dev Container setup is complete:

1. Run `01_deploy_azure_resources.ipynb`
2. Run `02_setup_ai_search_rag.ipynb`
3. Run `03_deploy_foundry_agent.ipynb`
4. Run `04_deploy_foundry_agent_with_maf.ipynb`
5. Run `05_maf_workflow_patterns.ipynb`
6. Run `06_maf_dev_ui.ipynb`
7. Run `07_evaluate_agents.ipynb`

Follow the instructions in each notebook!

---

## Related Documents

- [README.md](./README.md) - Project overview and getting started guide
- [PREREQUISITES.md](./PREREQUISITES.md) - Prerequisites and tool installation
- [CONFIGURATION.md](./CONFIGURATION.md) - Environment variables and configuration guide
- [.github/codespaces.md](./.github/codespaces.md) - GitHub Codespaces setup
