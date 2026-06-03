import subprocess

def execute_script(script_name):

    path = f"./scripts/{script_name}"

    result = subprocess.run(
        ["bash", path],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }