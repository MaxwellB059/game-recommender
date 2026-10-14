import os
from pathlib import Path


# for p in Path().iterdir():
#     print(p)

my_dir = Path("data/raw/backloggd-maxb059-2026-10-13.csv")
# print(my_dir.name)
# print(my_dir.suffix)
# print(my_dir.stem)

with my_dir.open() as f:
    print(f.read())



