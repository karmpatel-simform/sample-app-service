from flask import Flask, render_template_string
 
app = Flask(__name__)
 
# Enhanced HTML template for the web page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Frontdoor LB to webapptry2</title>
    <style>
        /* General styles */
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
 
        /* Card container */
        .container {
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            padding: 30px;
            max-width: 400px;
            text-align: center;
        }
 
        /* Header styles */
        h1 {
            color: #2c3e50;
            font-size: 2rem;
            margin-bottom: 20px;
        }
 
        /* Paragraph styles */
        p {
            color: #7f8c8d;
            font-size: 1rem;
            margin-bottom: 30px;
        }
 
        /* Button styles */
        button {
            padding: 12px 25px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
 
        button:hover {
            background-color: #2980b9;
        }
 
        /* Footer styles */
        footer {
            margin-top: 20px;
            font-size: 0.9rem;
            color: #bdc3c7;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Modern Web Page Ola Amigo Kaise ho theek ho</h1>
        <p>Experience a clean and modern design with Flask.</p>
        <button onclick="alert('Button clicked!')">Click Me</button>
        <footer>&copy; 2025 My Web Page</footer>
    </div>
</body>
</html>
"""
 
@app.route('/')
def home():
    return render_template_string(html_template)
 
if __name__ == '__main__':
    app.run(debug=True, port=8000)
 