from flask import Flask , request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

dict_input = {
    'town':'',
    'area':''
}

model = pickle.load(open('area_price_model.pkl','rb'))

@app.route("/",methods=['GET', 'POST'])
def home_area_prediction():

    if request.method == 'POST':
        town  = request.form['town'] if request.form['town'] !='' else ''
        area  = request.form['area'] if request.form['area'] !='' else ''
        dict_input['area']= area
        dict_input['town']= town
        for i in request.form.values() :
                if i == '':
                    message= 'Veuiller remplir toute les valeurs'
                    return render_template('home.html',error=message ,inputs =dict_input)
        
        predictionn = model.predict([[area, ]])
    return render_template('home.html',inputs= dict_input)




if __name__ == '__main__':
    app.run(port= 3000, debug=True)