from flask import Flask, request, render_template

file_dir = './files_dir/'
app = Flask('__name__')
@app.route("/read")
@app.route("/read/<file_name>")
@app.route("/read/<file_name>/<start>/<end>")
def route(file_name='file1.txt'):
    try:
        start = request.args.get("start")
        end = request.args.get("end")
        if start is None:
            start = 0
        else:
            if start.isdigit():
                start = int(start)
            else:
                return render_template('content.html', text=f'xxxxxxxxxxxxxxxx please provide valid line numbers xxxxxxxxxxxxxxxxx')
        if end is None:
            end = -1
        else:
            if end.isdigit():
                end = int(end)
            else:
                return render_template('content.html', text=f'xxxxxxxxxxxxxxxx please provide valid line numbers xxxxxxxxxxxxxxxxx')

        if start > end and end >= 0:
            return render_template('content.html', text=f'xxxxxxxxxxxxxxxx please provide valid line numbers xxxxxxxxxxxxxxxxx')
        with open(file_dir+file_name, 'r', encoding='utf8', errors='ignore') as f:
            all_lines_variable = f.readlines()
            all_lines_variable = ''.join(all_lines_variable[start:end])
            return render_template('content.html', text=all_lines_variable)
    except FileNotFoundError:
        return render_template('content.html', text=f'{file_name} not found, please provide valid file')
    except TypeError as ex:
        return render_template('content.html', text=f'{ex}')

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('content.html', text=f'{e} please pass valid url with query strings like "read/file4.txt?start=6&end=3"')

app.run()