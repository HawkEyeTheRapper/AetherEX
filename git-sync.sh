#!/bin/bash

cd ~/AetherEx
git add .
git commit -m "Auto-sync from JupyterLab"
git pull origin main --rebase
git push origin main
