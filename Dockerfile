FROM python:3.11-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملفات المتطلبات أولاً للاستفادة من الـ cache
COPY requirements.txt .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي الملفات
COPY . .

# تعريف المنفذ الذي سيعمل عليه التطبيق
EXPOSE 5000

# تشغيل التطبيق باستخدام gunicorn (أفضل للإنتاج من Flask server المدمج)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "60", "app:app"]
