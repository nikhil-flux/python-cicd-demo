from flask import Flask

app = Flask('Chota Flask')

@app.route('/')
def hello():
    return {'message': 'Hello from CI/CD!', 'status': 'success'}

@app.route('/api/health')
def health():
    return {'status': 'healthy', 'version': '1.0'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
