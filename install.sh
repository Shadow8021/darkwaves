#!/usr/bin/bash
apt update && apt upgrade -y
apt install python-cryptography -y
pip install ascii-magic -y