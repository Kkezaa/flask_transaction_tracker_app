# Import libraries

from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality

app = Flask(__name__)

# Sample data

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation

@app.route("/", methods = ["GET"])
def get_transactions():
    return render_template("transactions.html", transactions = transactions)


# Create operation

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")
    
    if request.method == "POST":

        transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        
        transactions.append(transaction)

        return redirect(url_for("get_transactions"))


# Update operation

@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":

        for transaction in transactions:

            if transaction["id"] == transaction_id:

                return render_template("edit.html", transaction = transaction)

        return {"message" : "Transaction number not found"}, 404 #implemented error handling if the transaction ID is not found.
            
    if request.method == "POST":
        date = request.form["date"]
        amount = float(request.form["amount"])

        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = date
                transaction["amount"] = amount
                break 
        return redirect(url_for("get_transactions"))




# Delete operation

@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):

    for transaction in transactions: # go trough the transactions and check if the ID's match, if yes, delete the transaction form the list.
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("get_transactions")) #redirect the user to the transactions page.
        


# Run the Flask app
    
if __name__ == "__main__":
    app.run(debug=True)