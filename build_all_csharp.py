import pathlib
from shutil import rmtree
import subprocess
from sys import platform

rmtree(pathlib.Path("./generated/csharp"), ignore_errors=True)
pathlib.Path("./generated/csharp").mkdir(parents=True, exist_ok=True)

protos = [str(path.relative_to("./").as_posix()) for path in pathlib.Path('./').rglob('*.proto')]
proc = subprocess.run(["protoc", "--proto_path=./", "--csharp_out=generated/csharp", "--csharp_opt=file_extension=.g.cs,base_namespace=PLUME", *protos])