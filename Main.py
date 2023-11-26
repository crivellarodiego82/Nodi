from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)

# Dizionario per mappare gli ID dei nodi a script Python
node_scripts = {
    1: "script_per_il_nodo_1.py",
    2: "script_per_il_nodo_2.py",
    3: "script_per_il_nodo_3.py",
    4: "script_per_il_nodo_4.py",
    5: "script_per_il_nodo_5.py",
    6: "script_per_il_nodo_6.py",
    7: "script_per_il_nodo_7.py",
    8: "script_per_il_nodo_8.py",
    9: "script_per_il_nodo_9.py",
    10: "script_per_il_nodo_10.py",
    11: "script_per_il_nodo_11.py",
    12: "script_per_il_nodo_12.py",
    13: "script_per_il_nodo_13.py",
    
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    node_id = int(request.form['node_id'])
    if node_id in node_scripts:
        script_name = node_scripts[node_id]
        try:
            # Esegui lo script associato al nodo utilizzando subprocess
            result = subprocess.check_output(['python', script_name], universal_newlines=True)
            return jsonify({'result': result})
        except subprocess.CalledProcessError as e:
            return jsonify({'error': f'Errore durante l\'esecuzione dello script: {str(e)}'})
    else:
        return jsonify({'error': 'Nodo non trovato'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
