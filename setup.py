import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

build_exe_options = {
    "includes": ["assets"],
}

setup(
    name="Calcuslugs",
    version="1",
    description="Math based artillery shooter",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name="Calcuslugs.exe")],
)