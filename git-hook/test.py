#!/usr/bin/env python3

import sys
import subprocess

def main():
    print("These files changed:")
    commit_id_byte = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True)
    commit_id_string= commit_id_byte.stdout.decode("utf-8").rstrip()
    subprocess.run(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit_id_string] )  
    sys.exit(1)


if __name__ == "__main__":
    main()

