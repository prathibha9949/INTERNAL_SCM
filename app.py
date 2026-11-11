from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def register():
    return render_template('register.html')
@app.route('/success', methods=['POST'])
def success():
    username=request.form.get('username')
    return render_template('success.html', username=username)
if __name__=='__main__':
    app.run(debug=True,port=5001)