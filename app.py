from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
import tempfile

app = Flask(__name__)

@app.get('/')
def home():
    return {
        "message": "Flask backend for two C programs (Even/Odd and Sum of first N). See /api/docs or README in project zip."
    }

@app.post('/api/evenodd')
def even_odd():
    data = request.get_json() or {}
    if 'number' not in data:
        return jsonify({"error": "Please provide 'number' in JSON body."}), 400
    try:
        n = int(data['number'])
    except Exception as e:
        return jsonify({"error": "number must be an integer."}), 400

    result = "Even" if n % 2 == 0 else "Odd"
    return jsonify({"number": n, "result": result})

@app.post('/api/sum')
def sum_n():
    data = request.get_json() or {}
    if 'n' not in data:
        return jsonify({"error": "Please provide 'n' in JSON body."}), 400
    try:
        n = int(data['n'])
    except Exception as e:
        return jsonify({"error": "n must be an integer."}), 400
    if n < 0:
        return jsonify({"error": "n must be non-negative."}), 400

    # sum formula
    s = n * (n + 1) // 2
    return jsonify({"n": n, "sum": s})

# Optional: attempt to compile and run the C programs included in the package (if gcc exists on the host).
def compile_and_run(source_filename, stdin_data=''):
    src_path = os.path.join(os.getcwd(), source_filename)
    if not os.path.exists(src_path):
        return {"error": f"Source file {source_filename} not found."}
    exe_path = os.path.join(tempfile.gettempdir(), "temp_c_exe")
    compile_cmd = ["gcc", src_path, "-o", exe_path]
    try:
        c = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
    except Exception as e:
        return {"error": f"Compilation failed: {e}"}
    if c.returncode != 0:
        return {"compile_stdout": c.stdout, "compile_stderr": c.stderr, "returncode": c.returncode}

    try:
        r = subprocess.run([exe_path], input=stdin_data, capture_output=True, text=True, timeout=5)
        return {"run_stdout": r.stdout, "run_stderr": r.stderr, "returncode": r.returncode}
    except Exception as e:
        return {"error": f"Execution failed: {e}"}

@app.post('/api/run_c')
def run_c():
    # JSON body: { "program": "even" | "sum", "input": "..." }
    # This endpoint will try to compile the matching C file (even_odd.c or sum_n.c) and run it.
    # It requires gcc to be installed on the host running Flask.
    data = request.get_json() or {}
    prog = data.get("program")
    stdin = data.get("input", "")
    if prog not in ("even", "sum"):
        return jsonify({"error": "program must be 'even' or 'sum'"}), 400
    filename = "even_odd.c" if prog == "even" else "sum_n.c"
    result = compile_and_run(filename, stdin)
    return jsonify(result)

if __name__ == '__main__':
    # Run in debug mode on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)