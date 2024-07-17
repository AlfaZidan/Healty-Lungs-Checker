from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/klasifikasi', methods=['GET', 'POST'])
def klasifikasi():
    if request.method == 'POST':
        # Ambil data dari form
        air_pollution = request.form.get('Air Pollution')
        alcohol_use = request.form.get('Alcohol use')
        dust_allergy = request.form.get('Dust Allergy')
        occupational_hazards = request.form.get('OccuPational Hazards')
        genetic_risk = request.form.get('Genetic Risk')
        chronic_lung_disease = request.form.get('chronic Lung Disease')
        balanced_diet = request.form.get('Balanced Diet')
        obesity = request.form.get('Obesity')
        passive_smoker = request.form.get('Passive Smoker')
        chest_pain = request.form.get('Chest Pain')
        coughing_of_blood = request.form.get('Coughing of Blood')
        fatigue = request.form.get('Fatigue')

        # Lakukan prediksi dengan model (misalnya knn_loaded.predict)
        # Misalkan hasil prediksi disimpan dalam variabel `result`
        # result = knn_loaded.predict([[air_pollution, alcohol_use, ...]])
        result = 'Hasil prediksi'  # Placeholder

        # Redirect ke halaman hasil dengan hasil prediksi
        return render_template('result.html', result=result)
    return render_template('klasifikasi.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
