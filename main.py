# main.py
#!/usr/bin/env python
import sys, os

def main():
    # ensure src/ is importable in container
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from src.main import main as run_server
        run_server()
    except Exception as e:
        print(f"Error starting MCP server: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()