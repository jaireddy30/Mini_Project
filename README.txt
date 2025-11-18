Flask backend for two C programs
===============================

What is included:
- app.py            : Flask backend providing endpoints to compute Even/Odd and Sum (as JSON).
                     Also includes an optional endpoint to compile & run bundled C programs if gcc is available.
- even_odd.c        : C program that reads an integer and prints Even/Odd.
- sum_n.c           : C program that reads an integer n and prints sum of first n natural numbers.
- requirements.txt  : Python dependencies.

Quick start (local)
-------------------
1. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Example requests (using curl):
   # Even/Odd (JSON)
   curl -X POST http://127.0.0.1:5000/api/evenodd -H "Content-Type: application/json" -d '{"number": 7}'

   # Sum of first n (JSON)
   curl -X POST http://127.0.0.1:5000/api/sum -H "Content-Type: application/json" -d '{"n": 10}'

   # Optional: attempt to compile & run the bundled C programs (requires gcc)
   # For even_odd.c (provide input "7\n")
   curl -X POST http://127.0.0.1:5000/api/run_c -H "Content-Type: application/json" -d '{"program":"even","input":"7\n"}'

   # For sum_n.c (provide input "10\n")
   curl -X POST http://127.0.0.1:5000/api/run_c -H "Content-Type: application/json" -d '{"program":"sum","input":"10\n"}'

Notes:
- The /api endpoints return JSON responses.
- The /api/run_c endpoint tries to compile with gcc and run the program. If gcc is not available or compilation fails, you'll get compile errors in the response.
- This project is intentionally simple so you can expand it (add validation, CI, containerization, tests, etc.)

Enjoy!