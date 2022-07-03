from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("testing")
    except Exception as e:
        print(e)
    return 'This is adult census income prediction'

if __name__=='__main__':
    app.run(debug=True)
    