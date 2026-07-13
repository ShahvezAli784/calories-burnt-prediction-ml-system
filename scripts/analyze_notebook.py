import nbformat
from pathlib import Path

notebook_path = Path(__file__).resolve().parents[1] / "notebooks" / "burnt_calories.ipynb"

nb = nbformat.read(notebook_path, as_version=4)

print("=" * 80)
print(f"Notebook: {notebook_path}")
print(f"Total Cells: {len(nb.cells)}")
print("=" * 80)

for i, cell in enumerate(nb.cells, start=1):
    print(f"\nCELL {i}")
    print(f"Type: {cell.cell_type}")

    if cell.cell_type == "code":
        source = cell.source.strip().split("\n")

        print(f"Lines: {len(source)}")

        print("Preview:")
        for line in source[:10]:
            print("   ", line)

        if len(source) > 10:
            print("   ...")

    elif cell.cell_type == "markdown":
        text = cell.source.strip().replace("\n", " ")
        print(text[:120])

    print("-" * 80)