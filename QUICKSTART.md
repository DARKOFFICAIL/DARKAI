# Quick Start

## 🚀 الشروع السريع

### المتطلبات
- Node.js 14+
- Python 3.8+
- npm

### خطوات التثبيت

```bash
# 1. استنساخ المشروع
git clone https://github.com/DARKOFFICAIL/DARKAI.git
cd DARKAI

# 2. التحويل للفرع الصحيح
git checkout setup-ai-bot

# 3. تثبيت المكتبات
npm install
pip install -r requirements.txt

# 4. إعداد API
cp src/config/.env.example .env
# عدّل .env وأضف مفتاح API الخاص بك

# 5. التشغيل
npm run dev
```

## ⚙️ تكوين API

### الخيار 1: عبر متغيرات البيئة

عدّل ملف `.env`:
```env
API_PROVIDER=openai
API_KEY=your-api-key-here
API_MODEL=gpt-4
API_BASE_URL=https://api.openai.com/v1
```

### الخيار 2: عبر الواجهة

1. شغّل التطبيق
2. اذهب إلى Settings ⚙️
3. أدخل مفتاح API
4. اضغط Save

## 📖 الاستخدام

### تحليل يدوي
```
1. اضغط على Analyzer tab
2. الصق الكود
3. اضغط "Analyze Code"
4. اعرض النتائج
```

### مراقبة حية
```
1. فتح ملف في VS Code أو أي محرر
2. عدّل الملف
3. البوت سيحلله تلقائياً
4. اعرض النتائج في Dashboard
```

## 🆘 استكشاف الأخطاء

### المشكلة: "API Key not configured"
**الحل:** أدخل مفتاح API في Settings

### المشكلة: "Failed to analyze code"
**الحل:** 
- تحقق من اتصال الإنترنت
- تأكد من أن الكود ليس فارغاً
- عيد تشغيل التطبيق

### المشكلة: "File monitor not working"
**الحل:**
- فعّل مراقبة الملفات من Settings
- تحقق من صلاحيات المجلد
- جرب ملف بامتداد مدعوم (.py, .js, .java, etc)

## 📚 الموارد

- [README الكامل](README.md)
- [دليل التطوير](DEVELOPMENT.md)
- [المساهمة](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## 💬 الدعم

- 📧 [البريد الإلكتروني](mailto:support@darkai.dev)
- 🐛 [الإبلاغ عن الأخطاء](https://github.com/DARKOFFICAIL/DARKAI/issues)
- 💬 [المناقشات](https://github.com/DARKOFFICAIL/DARKAI/discussions)

---

**Happy Coding! 🚀**
