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

USER jovyan

# Install JupyterLab extensions via pip
RUN pip install --no-cache-dir \
    jupyterlab-filesystem-access \
    jupyter-archive \
    jupyterlab-git \
    jupyterlab-github \
    ipywidgets \
    jlab-enhanced-cell-toolbar \
    jlab-enhanced-launcher \
    jupyterlab-cell-flash \
    jupyterlab-code-toc \
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
    jupyter_copilot

# Install extensions via jupyter labextension
RUN jupyter labextension install \
    @jupyterlab/filebrowser-extension \
    @jupyterlab/directory-listing \
    @jupyter-widgets/jupyterlab-manager

# Konfigurasi untuk mengaktifkan fitur drag-and-drop dan build extensions
RUN jupyter lab build && \
    jupyter lab clean && \
    jupyter cache clean

# Konfigurasi default untuk code formatter, LSP, dan Copilot
COPY jupyter_server_config.py /home/jovyan/.jupyter/

WORKDIR /home/jovyan/work