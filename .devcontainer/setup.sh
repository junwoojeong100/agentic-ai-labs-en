#!/bin/bash
set -e

echo "======================================"
echo "🚀 Setting up Python Development Environment"
echo "🌐 Environment: GitHub Codespaces"
echo "======================================"

# Print environment information
echo ""
echo "📍 System Information:"
echo "   OS: $(uname -s)"
echo "   Architecture: $(uname -m)"
echo "   User: $(whoami)"

# Check Python version
echo ""
echo "📍 Python Version:"
python3 --version
which python3

# Create virtual environment
echo ""
echo "📦 Creating Python virtual environment (.venv)..."
if [ -d ".venv" ]; then
    echo "⚠️  Virtual environment already exists, removing..."
    rm -rf .venv
fi

python3 -m venv .venv
echo "✅ Virtual environment created"

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Check and upgrade pip
echo ""
echo "🔍 Checking pip..."
which pip
pip --version

echo ""
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# Install required packages
echo ""
echo "📚 Installing required packages..."
echo "   This may take a few minutes..."

# requirements.txt 사용
if [ -f "requirements.txt" ]; then
    pip install --no-cache-dir -r requirements.txt
    echo "✅ All packages from requirements.txt installed!"
else
    echo "⚠️  requirements.txt not found, installing packages manually..."
    # Packages required for notebook execution
    pip install --no-cache-dir \
        "azure-identity>=1.17.0" \
        "azure-ai-projects>=1.0.0b5" \
        "azure-ai-inference>=1.0.0b6" \
        "azure-search-documents>=11.4.0" \
        "openai>=1.51.0" \
        "python-dotenv>=1.0.0" \
        "requests>=2.31.0" \
        "fastapi>=0.110.0" \
        "uvicorn>=0.30.0" \
        "httpx>=0.27.0" \
        "agent-framework>=1.0.0b251016" \
        "azure-monitor-opentelemetry>=1.6.0" \
        "azure-monitor-opentelemetry-exporter>=1.0.0b27" \
        "opentelemetry-api>=1.20.0" \
        "opentelemetry-sdk>=1.20.0" \
        "opentelemetry-instrumentation-fastapi>=0.45b0" \
        "fastmcp>=0.2.0" \
        "mcp>=1.1.0" \
        "ipykernel>=6.29.0"
    echo "✅ All packages installed!"
fi

# Register Jupyter kernel
echo ""
echo "🎯 Registering Jupyter kernel..."
python -m ipykernel install --user --name=agentic-ai-labs --display-name "Python 3.12 (agentic-ai-labs)"

# Check Azure CLI login status (optional)
echo ""
echo "🔐 Azure CLI Status:"
if az account show &> /dev/null; then
    echo "   ✅ Already logged in to Azure"
    az account show --query "{Name:name, TenantId:tenantId}" -o table
else
    echo "   ℹ️  Not logged in to Azure (run 'az login' when needed)"
fi

echo ""
echo "======================================"
echo "✅ Setup completed successfully!"
echo "======================================"
echo ""
echo "📍 Virtual environment: .venv"
echo "📍 Python interpreter: .venv/bin/python"
echo "📍 Jupyter kernel: Python 3.12 (agentic-ai-labs)"
echo ""
echo "� Next steps:"
echo "   1. Open a notebook (.ipynb file)"
echo "   2. Select kernel: 'Python 3.12 (agentic-ai-labs)'"
echo "   3. Start Lab 1: 01_deploy_azure_resources.ipynb"
echo ""
echo "💡 Tip: Run 'az login' to authenticate with Azure before starting the labs"
echo ""
