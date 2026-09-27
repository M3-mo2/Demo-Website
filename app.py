from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# تحديد المجلد الذي يحتوي على الملفات الثابتة
STATIC_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """عرض الصفحة الرئيسية"""
    return send_from_directory(STATIC_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """تقديم الملفات الثابتة مثل الصور والـ CSS"""
    try:
        return send_from_directory(STATIC_DIR, filename)
    except FileNotFoundError:
        abort(404)

@app.errorhandler(404)
def not_found(e):
    """صفحة الخطأ 404"""
    return send_from_directory(STATIC_DIR, 'index.html')

if __name__ == '__main__':
    # الحصول على المنفذ من متغير البيئة أو استخدام 5000 كافتراضي
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
