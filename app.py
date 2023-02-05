from flask import Flask, render_template, request

import utils

app = Flask(__name__, static_url_path="")


@app.route("/")
def sheet():
    # Print if we say print=true
    use_print_count = request.args.get("print", default=True, type=lambda v: v.lower() == "true")
    # Fixed only if we say fixed=true
    fixed_only = request.args.get("fixed", default=False, type=lambda v: v.lower() == "true")
    return render_template("sheet.html", cards=utils.get_card_data(use_print_count, fixed_only))


@app.route("/goals")
def goals():
    return render_template("goals.html", goals=utils.get_goal_data())


if __name__ == "__main__":
    app.run(debug=True)
