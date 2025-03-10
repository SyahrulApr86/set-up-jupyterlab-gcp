# Base image
FROM quay.io/jupyter/pytorch-notebook:cuda12-python-3.11.8

USER root

# Install system dependencies dan Node.js 18.x
RUN apt-get update && \
    apt-get install -y \
    zip \
    unzip \
    git \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Verifikasi Node.js version
RUN node --version && npm --version

# Grant sudo access ke user jovyan
RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jovyan

# Ubah kepemilikan home directory untuk user jovyan
RUN chown -R jovyan:users /home/jovyan

USER jovyan

# Install JupyterLab extensions via pip
RUN pip install --no-cache-dir \
    jupyterlab \
    notebook \
    jupyterlab-filesystem-access \
    jupyter-archive \
    ipywidgets \
    jupyterlab-cell-flash \
    jupyterlab-favorites \
    jupyterlab-unfold \
    jupyterlab-code-formatter \
    black \
    isort \
    jupyterlab-lsp \
    python-lsp-server[all] \
    pyls-spyder \
    pylsp-mypy \
    python-lsp-black \
    pylsp-rope \
    pyls-memestra \
    jupyter_copilot \
    jupyterlab_widgets \
    nbclassic

# Build JupyterLab
RUN jupyter lab build --minimize=False

# Konfigurasi default untuk code formatter, LSP, dan Copilot
COPY jupyter_server_config.py /home/jovyan/.jupyter/

WORKDIR /home/jovyan
