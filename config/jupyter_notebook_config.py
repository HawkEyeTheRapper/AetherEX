# Jupyter Notebook Configuration for AetherEX

c = get_config()

# Allow access from any IP
c.NotebookApp.ip = '0.0.0.0'

# Set the port Jupyter runs on
c.NotebookApp.port = 8888

# Disable automatic browser launch
c.NotebookApp.open_browser = False

# Allow external access (fixes 403 errors)
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_origin = '*'

# Enable trust for headers (important for Nginx proxy)
c.NotebookApp.trust_xheaders = True

# Set the base URL (important if reverse proxy is used)
c.NotebookApp.base_url = '/'

# Enable running Jupyter as root (only if necessary)
c.NotebookApp.allow_root = True

# Set a secure hashed password (Replace with your generated hash)
from notebook.auth import passwd
c.NotebookApp.password = 'sha1:abcdef123456:098f6bcd4621d373cade4e832627b4f6'  # Replace with actual hashed password

# Log level (optional: DEBUG, INFO, WARNING, ERROR)
c.NotebookApp.log_level = 'INFO'
