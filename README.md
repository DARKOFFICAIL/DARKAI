# 🤖 DARKAI - AI Code Assistant Bot

بوت ذكي متعدد اللغات للمراقبة الحية للكود وتصحيح الأخطاء في أي تطبيق برمجة

## ✨ الميزات

- 🔍 **مراقبة حية** للكود أثناء الكتابة
- 🌐 **دعم كل لغات البرمجة**
- 💻 **متعدد المنصات** (Windows, macOS, Linux)
- 🧠 **ذكاء اصطناعي** لاكتشاف الأخطاء
- ⚙️ **قابل للتخصيص** - API خارجي في ملف منفصل
- 🎨 **واجهة سهلة الاستخدام**

## 🏗️ معمارية المشروع

```
DARKAI/
├── backend/              # خادم البوت (Python/Node.js)
├── extensions/           # ملحقات المحررات
│   ├── vscode/          # VS Code Extension
│   ├── sublime/         # Sublime Text Plugin
│   └── jetbrains/       # IntelliJ/PyCharm Plugin
├── core/                # محرك البوت الأساسي
├── config/              # ملفات الإعدادات
│   └── api.config.json  # ملف الـ API (يمكن تعديله)
├── models/              # نماذج الـ AI
└── tests/               # الاختبارات
```

## 🚀 البدء السريع

### المتطلبات
- Python 3.8+ أو Node.js 14+
- pip/npm

### التثبيت

```bash
git clone https://github.com/DARKOFFICAIL/DARKAI.git
cd DARKAI

# اختر أحد الخيارات:

# Python
pip install -r requirements.txt
python start.py

# أو Node.js
npm install
npm start
```

### تكوين الـ API

عدّل ملف `config/api.config.json`:

```json
{
  "apiProvider": "openai",
  "apiKey": "your-api-key-here",
  "model": "gpt-4",
  "baseUrl": "https://api.openai.com/v1"
}
```

## 📦 المكونات الرئيسية

### 1. Backend (خادم البوت)
يحلل الكود ويكتشف الأخطاء

### 2. Language Detectors
يتعرف على لغة البرمجة تلقائياً

### 3. Code Analyzer
يفحص الصيغة والأخطاء المنطقية

### 4. AI Engine
يستخدم نماذج الذكاء الاصطناعي للتحليل العميق

### 5. IDE Extensions
ملحقات لـ VS Code, Sublime, IntelliJ وغيرها

## 🔌 الأنظمة المدعومة

| النظام | الإصدار | الحالة |
|--------|---------|--------|
| Windows | 10+ | ✅ مدعوم |
| macOS | 10.14+ | ✅ مدعوم |
| Linux | Ubuntu 18.04+ | ✅ مدعوم |

## 📝 الترخيص

MIT License

## 👨‍💻 المطور

[DARKOFFICAIL](https://github.com/DARKOFFICAIL)
