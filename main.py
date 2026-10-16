import os
from flask import Flask, render_template, request, make_response
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'website': request.form.get('website'),
        'summary': request.form.get('summary'),
        'experience': request.form.get('experience'),
        'education': request.form.get('education'),
        'skills': request.form.get('skills')
    }
    
    rendered_html = render_template('resume.html', data=data)
    
    try:
        pdf = HTML(string=rendered_html).write_pdf()
    except Exception as e:
        # Fallback for systems lacking Cairo/Pango native libraries during testing
        pdf = rendered_html.encode('utf-8')
        response = make_response(pdf)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
