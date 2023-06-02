from flask import Flask, render_template, request

# Mapping of grades to numerical values
mapping = {"A+": 10, "A": 9, "B+": 8, "B": 7, "C+": 6, "C": 5, "D": 4, "F": 0}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve input values from the form
        credit_values = [
            int(request.form[f'credit_{i}']) for i in range(len(subjects))
        ]
        grade_values = [
            mapping[request.form[f'grade_{i}']] for i in range(len(subjects))
        ]

        # Calculate weighted total and SGPA
        total = sum(credit_values[i] * grade_values[i] for i in range(len(credit_values)))
        cred_sum = sum(credit_values)
        sgpa = total / cred_sum

        # Additional functionality for SGPA output
        if sgpa >= 9.0:
            additional_text_sgpa = "Damn homie, you smart af. You're still depressed though, I bet."
            # # Play music when SGPA is above 9.0
            # play_music()
        elif 8.0 <= sgpa < 9.0:
            additional_text_sgpa = "Congrats! You live to get depressed another semester!"
        else:
            additional_text_sgpa = "Congrats! You have reached your one-way destination to depression!"

        return render_template('index.html', sgpa=sgpa, additional_text_sgpa=additional_text_sgpa)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

