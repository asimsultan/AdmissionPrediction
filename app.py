from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
   result = ''
   if request.method == 'POST':
      gre = request.form['gre_score']
      toefl = request.form['rating']
      rating = request.form['sop']
      sop = request.form['lor']
      lor = request.form['cgpa']
      cgpa = request.form['cgpa']
      research = request.form['research']

      train = [[gre,toefl,rating,sop,lor,cgpa,research]]

      model = pickle.load(open('Admission_Prediction.sav','rb'))
      score = model.predict(train)
      score = score[0]*100

      print('Score:',score)
      result = 'Admission percentage given the above values is {}'.format(round(score,2))

   return render_template('intro.html', result=result)

if __name__ == '__main__':
   app.run()