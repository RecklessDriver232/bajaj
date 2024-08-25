from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/bfhl", methods=["POST", "GET"])
def home():

    if request.method == "GET":

        return jsonify({"operation_code": 1}), 200

    elif request.method == "POST":
        data = request.json.get("data")
        letter = []
        number = []
        smallest = []
        success = True
        if data
        try:
            for i in data:
                if i.isalpha():
                    letter.append(i)
                    if i.islower():
                        smallest.append(i)
                elif i.isdigit():
                    number.append(i)

            largest_lowercase = max(smallest) if smallest else None
            a = []
            a.append(largest_lowercase)
        except:
            success = False

        if success == True:
            response = {
                "is_success": True,
                "user_id": "risabh_sinha_07012003",
                "email": "risabh.sinha25@gmail.com",
                "roll_number": "21BCE2430",
                "numbers": number,
                "alphabets": letter,
                "highest_lowercase_alphabet": a,
            }
        else:
            response = {
                "is_success": True,
                "user_id": "risabh_sinha_07012003",
                "email": "risabh.sinha25@gmail.com",
                "roll_number": "21BCE2430",
            }

        return jsonify(response), 200


if __name__ == "__main__":

    app.run(debug=True)
