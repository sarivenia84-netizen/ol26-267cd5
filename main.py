"""MakeFun entry: Slept Great, Says the Bank"""
import os

# Judge brief: sleep-app claim of great rest vs bank's rent charge — one of them is lying
LINE = "My sleep app says I slept great. My bank says otherwise. One of them's lying. Charging rent."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE)