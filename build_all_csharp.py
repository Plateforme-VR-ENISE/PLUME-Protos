import pathlib
from shutil import rmtree
import subprocess
from sys import platform

protos = [str(path.relative_to("./").as_posix()) for path in pathlib.Path('./').rglob('*.proto')]

rmtree(pathlib.Path("./generated/csharp"), ignore_errors=True)
pathlib.Path("./generated/csharp").mkdir(parents=True, exist_ok=True)

program = "./protogen" if platform in ["linux", "linux2"] else "protogen.exe"
proc = subprocess.run([program, "--proto_path=./", "--csharp_out=generated/csharp", "--package=PLUME", "**/*.proto"])