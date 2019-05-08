from flask import Flask, render_template, request
from seq_predict import search as seq_ai


app = Flask(__name__)
logfile = open("seq-logs.txt", "a")
MAX_SEQ_LEN = 12


def parse_seq(seq_string):
    logfile.write(seq_string + "\n")
    logfile.flush()
    seq_string = seq_string.replace(',', ' ')
    seq_string = ''.join(c for c in seq_string if c in '0123456789-. ')
    seq = list(map(int, seq_string.split()))
    return seq


@app.route('/')
def index():
    example_sequences = ["12, 15, 21, 24, 30", "2, 5, 14, 41", "1, 1, 2, 3, 5",
                         "1, 8, 27", "1, 3, 3, 9, 27"]
    result = ""
    seq_string = ""
    if "seq" in request.args:
        seq_string = request.args['seq']
        try:
            seq = parse_seq(seq_string)
        except Exception:
            return "Invalid Sequence"
        if len(seq) > MAX_SEQ_LEN:
            return "Sequence is too long."
        result = seq_ai.findNext(seq).log_tree.to_string()
    return render_template('index.html', example_sequences=example_sequences,
                           result=result, seq_string=seq_string)


@app.route('/solve')
def solve():
    result = ""
    if "seq" in request.args:
        seq = request.args['seq']
        seq_string = request.args['seq']
        try:
            seq = parse_seq(seq_string)
        except Exception:
            return "Invalid Sequence"
        if len(seq) > MAX_SEQ_LEN:
            return "Sequence is too long."
        result = seq_ai.findNext(seq).log_tree.to_string()
        return result
    return "Invalid input"
