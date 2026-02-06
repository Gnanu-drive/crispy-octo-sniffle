"""
File Upload Stream Service
A Flask application that allows users to upload files with stream limits
and automatically saves them to the repository.
"""
import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB stream limit
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'zip', 'mp4', 'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload with stream limit.
    Files are streamed from the request and saved to the upload folder.
    """
    try:
        # Check if file is present in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in request'}), 400
        
        file = request.files['file']
        
        # Check if file was selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Validate file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Stream file to disk with size limit enforced by MAX_CONTENT_LENGTH
            file.save(filepath)
            
            file_size = os.path.getsize(filepath)
            logger.info(f"File uploaded successfully: {filename} ({file_size} bytes)")
            
            return jsonify({
                'message': 'File uploaded successfully',
                'filename': filename,
                'size': file_size
            }), 200
        else:
            return jsonify({'error': 'File type not allowed'}), 400
            
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': 'An error occurred during file upload'}), 500


@app.route('/files')
def list_files():
    """List all uploaded files in the repository."""
    try:
        files = []
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            # Skip hidden files and .gitkeep
            if filename.startswith('.'):
                continue
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filepath):
                files.append({
                    'name': filename,
                    'size': os.path.getsize(filepath)
                })
        return jsonify({'files': files}), 200
    except Exception as e:
        logger.error(f"List files error: {str(e)}")
        return jsonify({'error': 'An error occurred while listing files'}), 500


@app.route('/files/<filename>')
def download_file(filename):
    """Download a file from the uploads folder."""
    try:
        # Validate filename to prevent directory traversal
        filename = secure_filename(filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Ensure the resolved path is within the upload folder
        if not os.path.abspath(filepath).startswith(os.path.abspath(app.config['UPLOAD_FOLDER'])):
            return jsonify({'error': 'Invalid filename'}), 400
        
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        return jsonify({'error': 'File not found'}), 404


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit exceeded error."""
    return jsonify({'error': f'File too large. Maximum size is {MAX_CONTENT_LENGTH / (1024 * 1024)}MB'}), 413


if __name__ == '__main__':
    # Use environment variable for debug mode, default to False for security
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
