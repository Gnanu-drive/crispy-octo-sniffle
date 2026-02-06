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

#### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Gnanu-drive/crispy-octo-sniffle.git
cd crispy-octo-sniffle
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

#### Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Gnanu-drive/crispy-octo-sniffle)

1. Click the "Deploy with Vercel" button above, or:

2. Install Vercel CLI:
```bash
npm i -g vercel
```

3. Deploy:
```bash
vercel
```

**Note**: When deployed on Vercel, uploaded files are stored in `/tmp` which is ephemeral. Files will be lost when the serverless function spins down. For persistent storage, consider using a cloud storage service like AWS S3, Cloudflare R2, or Vercel Blob Storage.

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

### Deployment

This application is ready to deploy on Vercel. The `vercel.json` configuration file is included in the repository.

**Important Notes for Vercel Deployment:**
- Uploaded files are stored in `/tmp` directory which is ephemeral
- Files will be deleted when the serverless function restarts
- For production use with persistent storage, integrate a cloud storage service (AWS S3, Cloudflare R2, Vercel Blob, etc.)

### License

See LICENSE file for details.