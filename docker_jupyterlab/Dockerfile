# Base image
FROM quay.io/jupyter/pytorch-notebook:cuda12-python-3.11.8

# Set user ke root untuk instalasi awal
USER root

# Install system dependencies, Node.js 18.x, coreutils, dan sudo
RUN apt-get update && \
    apt-get install -y \
    zip \
    unzip \
    git \
    curl \
    coreutils \
    sudo \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Tambahkan user 'jovyan' ke grup sudo dan beri akses tanpa password
RUN usermod -aG sudo jovyan && \
    echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jovyan

# Tambahkan alias 'll' untuk semua user
RUN echo "alias ll='ls -l --color=auto'" >> /etc/bash.bashrc

# Verifikasi bahwa coreutils dan ll tersedia
RUN ls --version && node --version && npm --version

# Aktifkan Conda base secara default
RUN echo "source /opt/conda/etc/profile.d/conda.sh && conda activate base" >> /home/jovyan/.bashrc
RUN echo "source /opt/conda/etc/profile.d/conda.sh && conda activate base" >> /home/jovyan/.profile
RUN echo "source /opt/conda/etc/profile.d/conda.sh && conda activate base" >> /etc/bash.bashrc

# Pindah ke user jovyan setelah instalasi sistem selesai
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

# Set working directory
WORKDIR /home/jovyan

# Pastikan Conda base aktif dan jalankan JupyterLab saat container berjalan
ENTRYPOINT ["/bin/bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate base && exec \"$@\"", "--"]

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
