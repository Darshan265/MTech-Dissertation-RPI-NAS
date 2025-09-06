
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = '26e4c45477343cac8cc28328647035d86bda27a4a75f368a2d281679b370be53'

# Path to mounted Samba/USB folder
app.config['UPLOAD_FOLDER'] = '/mnt/usb128GB/share'

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Single user store for demo
users = {
    'pi': generate_password_hash('1994')
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and check_password_hash(users[username], password):
            login_user(User(username))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash(f'Uploaded {filename}')
        return redirect(url_for('dashboard'))

    # List files
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
    except FileNotFoundError:
        files = []

    # Build table rows dynamically
    rows = ""
    for file in files:
        rows += f"""
        <tr>
            <td>{file}</td>
            <td>
                <a href="{url_for('download_file', filename=file)}" class="btn btn-sm btn-success">Download</a>
                <a href="{url_for('delete_file', filename=file)}" class="btn btn-sm btn-danger" onclick="return confirm('Delete {file}?');">Delete</a>
            </td>
        </tr>
        """

    return render_template('dashboard.html', file_rows=rows)

@app.route('/download/<path:filename>')
@login_required
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/delete/<path:filename>')
@login_required
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash(f'Deleted {filename}')
    else:
        flash(f'File {filename} not found')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
