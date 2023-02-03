from flask import Flask, render_template, request

import utils

app = Flask(__name__, static_url_path="")


@app.route("/")
def sheet():
    use_print_count = request.args.get(
        "print", default=True, type=lambda v: v.lower() != "false"
    )  # Print unless we say print=false
    print(use_print_count)
    return render_template("sheet.html", cards=utils.get_card_data(use_print_count))


if __name__ == "__main__":
    app.run(debug=True)
