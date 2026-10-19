from pathlib import Path
print(Path(__file__))
print(Path(__file__).parent.parent / "data" / "SouthGermanCredit.asc")