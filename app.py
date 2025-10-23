from flask import Flask, render_template, jsonify, request
import json, os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

@app.after_request
def no_cache(resp):
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp

@app.route('/')
def index():
    cfg = load_config()
    return render_template('index.html', config=cfg)

@app.route('/api/config', methods=['GET', 'PUT'])
def api_config():
    if request.method == 'GET':
        return jsonify(load_config())
    else:
        cfg = request.get_json(force=True)
        save_config(cfg)
        return jsonify({"ok": True})

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)