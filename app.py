from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/about")
def about():
    return render_template('home.html')

@app.route("/form", methods=['get', 'post'])
def form():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        no1 = float(request.form['num1'])
        no2 = float(request.form['num2'])
        result1=request.form['result']
        
        if result1=='+':
         ans=no1+no2
        
        elif result1=='-':
         ans=no1-no2
         
        elif result1=='*':
         ans=no1*no2
        
        elif result1=='/':
         ans=no1/no2
         
        return render_template('index.html', score=ans)
        
        
if __name__ == "__main__":
    app.run(debug=True)