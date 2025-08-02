#!/bin/bash
# Simulates checking and restarting idle services

echo "[INFO] Checking idle services..."
sleep 1

# Simulate an idle nginx service
SERVICE_NAME="nginx"
echo "[INFO] Service '$SERVICE_NAME' found idle. Restarting..."
sleep 1
echo "[OK] Service '$SERVICE_NAME' restarted successfully."

# Simulate another service
SERVICE_NAME="mysql"
echo "[INFO] Service '$SERVICE_NAME' is running normally."
