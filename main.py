from flask import Flask,render_template,request,redirect,jsonify,session,flash
import device_manger as mgr
    
IPAddr = '192.168.0.107'
app = Flask(__name__)
app.secret_key ="digipodium iot workshops"

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/update', methods=['GET','POST'])
def process():
    device = request.args.get('device')
    action = request.args.get('state')
    status = 'on' if action=='1' else 'off'
    
    result = mgr.update_device(device,status)
    if result:
        return jsonify({'msg':f"device {device} successfully set to {status}",'status':True})
    else:
        return jsonify({'msg':f"device {device} failed to  update {status}",'status':False})

if __name__ == '__main__':

	app.run(host=IPAddr,debug=True)
