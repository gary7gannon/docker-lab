from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  
@app.route("/euler1")
def euler1():
  Totsum = 0
   for i in range (1000):
     if i%3 == 0 :
       Totsum +=i;
     elif i % 5 == 0:
       Totsum += i;
       print(Totsum)

@app.route("/euler2")
def euler2():
f1 = 1
f2 = 2
temp = 0
total = 0
while temp <=4000000:
  temp = f2
  if temp % 2 == 0:
    total = total + temp
    print (total)
    temp = f1 + f2
    f1 = f2
    f2 = temp

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
