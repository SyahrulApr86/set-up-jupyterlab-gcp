# jupyter_server_config.py
c.ServerApp.jpserver_extensions = {
    'jupyterlab_code_formatter': True,
    'jupyterlab_lsp': True,
    'jupyter_copilot': True
}

c.JupyterLabCodeFormatter.formatters = {
    'black': {
        'line_length': 88,
        'string_normalization': True
    },
    'isort': {
        'multi_line_output': 3,
        'include_trailing_comma': True,
        'force_grid_wrap': 0,
        'use_parentheses': True,
        'line_length': 88
    }
}

# LSP Configuration
c.LanguageServerManager.language_servers = {
    'pylsp': {
        'serverSettings': {
            'pylsp.plugins.pycodestyle.enabled': True,
            'pylsp.plugins.pyflakes.enabled': True,
            'pylsp.plugins.flake8.enabled': True,
            'pylsp.plugins.pylint.enabled': True,
            'pylsp.plugins.yapf.enabled': False,
            'pylsp.plugins.black.enabled': True,
            'pylsp.plugins.rope_completion.enabled': True,
            'pylsp.plugins.rope_rename.enabled': True
        }
    }
}