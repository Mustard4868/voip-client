from pathlib import Path

path = Path(pathlib.Path(__file__).parent/"utils")
    for f in path.glob("[!_]*.py"):
        import f
