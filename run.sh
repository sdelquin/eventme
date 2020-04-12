#!/bin/bash
# Master script.

source ~/.virtualenvs/eventme/bin/activate
cd "$(dirname "$0")"
exec python main.py --when=next-weekend
