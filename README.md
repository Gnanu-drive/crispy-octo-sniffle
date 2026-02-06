# crispy-octo-sniffle

## File Upload Stream Service

A Flask-based web application that allows users to upload files with stream limits. Files are automatically saved to the repository and can be managed through a web interface.

### Features

- 📁 **File Upload with Stream Limit**: Upload files up to 16MB
- 🎨 **Modern Web Interface**: Beautiful drag-and-drop UI
- 📊 **File Management**: View, list, and download uploaded files
- 🔒 **Security**: File type validation and secure filename handling
- 📂 **Repository Integration**: Files are saved to the `uploads/` directory

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Gnanu-drive/crispy-octo-sniffle.git
cd crispy-octo-sniffle
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload files using:
   - Drag and drop files into the upload area
   - Click the upload area to browse for files
   - Click "Upload File" to upload

4. View uploaded files in the "Uploaded Files" section

### Configuration

The application can be configured in `app.py`:

- `MAX_CONTENT_LENGTH`: Maximum file size (default: 16MB)
- `ALLOWED_EXTENSIONS`: Allowed file types
- `UPLOAD_FOLDER`: Directory where files are saved (default: `uploads/`)

### API Endpoints

- `GET /` - Main upload interface
- `POST /upload` - Upload a file
- `GET /files` - List all uploaded files (JSON)
- `GET /files/<filename>` - Download a specific file

### Supported File Types

- Documents: txt, pdf, doc, docx
- Images: png, jpg, jpeg, gif
- Media: mp4, mp3
- Archives: zip

### License

See LICENSE file for details.