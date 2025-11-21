from flask import Flask, render_template, request

app = Flask(__name__)


foods = [
    {
        "id": "hamburger",
        "name": "Hamburger",
        "calories": 500,
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"
    },
    {
        "id": "pizza",
        "name": "Pizza (1 Dilim)",
        "calories": 300,
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"
    },
    {
        "id": "kebap",
        "name": "Adana Kebap",
        "calories": 600,
        "image": "https://images.unsplash.com/photo-1644364935906-792b2245a2c0?w=400"
    },
    {
        "id": "salata",
        "name": "Sezar Salata",
        "calories": 200,
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400"
    },
    {
        "id": "makarna",
        "name": "Makarna",
        "calories": 400,
        "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400"
    },
    {
        "id": "baklava",
        "name": "Baklava (1 Porsiyon)",
        "calories": 500,
        "image": "https://images.unsplash.com/photo-1658413380634-e127bbaeeb7b?w=400"
    },
    {
        "id": "kola",
        "name": "Kola (330ml)",
        "calories": 150,
        "image": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400"
    },
    {
        "id": "ayran",
        "name": "Ayran",
        "calories": 80,
        "image": "https://cf.kizlarsoruyor.com/q12446906/8b35aa9d-b348-4c91-92c6-d800fbcdeb35.jpg"
    },
    {
        "id": "patates",
        "name": "Patates Kızartması",
        "calories": 400,
        "image": "https://www.gurmerehberi.com/wp-content/uploads/2024/06/Patates-Kizartmasi-Yapmanin-puf-noktalari.jpg"
    },
    {
        "id": "dondurma",
        "name": "Dondurma",
        "calories": 250,
        "image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400"
    },
    {
        "id": "lahmacun",
        "name": "Lahmacun",
        "calories": 220,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS82aZAsppgoOWRH0iADyPDbDfQrX4amk-zmw&s"
    },
    {
        "id": "simit",
        "name": "Simit",
        "calories": 300,
        "image": "https://www.safranbolufirini.com/wp-content/uploads/2024/01/simit-gevrek-optimized.webp"
    },
    {
        "id": "manti",
        "name": "Mantı",
        "calories": 400,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm1moNX6UyPVMBgaGMtoJTuLiIy-TJG2e_rA&s"
    },
    {
        "id": "corba",
        "name": "Mercimek Çorbası",
        "calories": 150,
        "image": "https://www.usulu.net/wp-content/uploads/2024/12/Dogu-usulu-mercimek-corbasi-2.webp"
    },
    {
        "id": "cigkofte",
        "name": "Çiğ Köfte (Dürüm)",
        "calories": 350,
        "image": "https://lh5.googleusercontent.com/proxy/4KwBi7fzU1xSoye3VaXwBBPRWse0vFt5UaHTL7x3EfgUuRekrkZboWYinGJqFvaJiJE_YdEuXiPAds1ZjkTmhnT0j09gr2qGLd4BaFs"
    },
    {
        "id": "kunefe",
        "name": "Künefe",
        "calories": 450,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj33W7iWG4xZuprc8UxpDeel2X3ciJKnBJ0A&s"
    }
]

@app.route('/')
def index():
    return render_template('index.html', foods=foods)

@app.route('/result', methods=['POST'])
def result():
    selected_items = request.form.getlist('food_selection')
    
    total_calories = 0
    eaten_foods = []
    
    for item_id in selected_items:
        for food in foods:
            if food['id'] == item_id:
                total_calories += food['calories']
                eaten_foods.append(food)
                break
    
    
    weight_gain_kg = total_calories / 770
    
    
    exercises = []
    if total_calories > 0:
        
        walking_hours = total_calories / 250
        
        running_hours = total_calories / 600
        
        swimming_hours = total_calories / 500
        
        exercises.append({"name": "Yürüyüş", "hours": round(walking_hours, 1), "icon": "🚶"})
        exercises.append({"name": "Koşu", "hours": round(running_hours, 1), "icon": "🏃"})
        exercises.append({"name": "Yüzme", "hours": round(swimming_hours, 1), "icon": "🏊"})
    
    return render_template('result.html', 
                           total_calories=total_calories, 
                           weight_gain=round(weight_gain_kg, 3),
                           eaten_foods=eaten_foods,
                           exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)

