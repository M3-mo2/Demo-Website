# كبابجي ومشويات الشيخ 🔥

موقع مطعم مشويات مصرية مع إمكانية الطلب عبر واتساب.

## التشغيل المحلي

### باستخدام Python مباشرة:

```bash
# تثبيت المتطلبات
pip install -r requirements.txt

# تشغيل السيرفر
python app.py
```

الموقع سيعمل على: `http://localhost:5000`

### باستخدام Docker:

```bash
# بناء الصورة
docker build -t demo-website .

# تشغيل الحاوية
docker run -p 5000:5000 demo-website
```

## النشر على Railway

### الطريقة الأولى: من خلال GitHub

1. ارفع المشروع على GitHub
2. اذهب إلى [Railway.app](https://railway.app)
3. سجل دخول وانقر على "New Project"
4. اختر "Deploy from GitHub repo"
5. اختر المستودع الخاص بك
6. Railway سيكتشف Dockerfile تلقائياً ويبدأ بالنشر
7. انقر على "Settings" → "Generate Domain" للحصول على رابط الموقع

### الطريقة الثانية: من خلال Railway CLI

```bash
# تثبيت Railway CLI
npm i -g @railway/cli

# تسجيل الدخول
railway login

# رفع المشروع
railway init
railway up
```

## البنية

- `index.html` - الصفحة الرئيسية للموقع
- `app.py` - سيرفر Flask
- `requirements.txt` - متطلبات Python
- `Dockerfile` - ملف Docker للنشر
- `.dockerignore` - الملفات المستبعدة من Docker

## المميزات

- 🚀 سريع وخفيف
- 📱 متجاوب مع جميع الأجهزة
- 🎨 تصميم عصري باللغة العربية
- 💬 طلب مباشر عبر واتساب
- 🔥 قائمة طعام تفاعلية

## الإعدادات

لتغيير رقم الواتساب، قم بتعديل المتغير `WHATSAPP_NUMBER` في ملف `index.html` (السطر 1183).

---

صُنع بـ ❤️ في مصر
