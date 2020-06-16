from flask import Flask, request, render_template, Markup

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        return render_template('index.html', input_text='', res_text='')
    else:
        input_text = request.form.get("input_text")
        res_text = Markup(format_res(reverse_text(input_text)))
        return render_template('index.html', input_text=input_text, res_text=res_text)


def format_res(textList):
    return '<p>' + '</p><p>'.join(textList) + '</p>'


def reverse_text(text):
    res = []
    res.append('原来字符串: %s' % (text))
    res.append('转换字符串: %s' % (''.join(reversed(list(text)))))
    return res


if __name__ == '__main__':
    app.run()
