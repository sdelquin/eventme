#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source $HOME/.virtualenvs/eventme/bin/activate
python main.py --when=next-weekend
