# DARKAI - AI Code Assistant Desktop Bot

## 📋 نظرة عامة

DARKAI هو تطبيق سطح مكتب ذكي يراقب الكود الذي تكتبه ويحللها باستخدام الذكاء الاصطناعي لاكتشاف الأخطاء وتقديم الاقتراحات.

## 🚀 المميزات

✅ **مراقبة حية** - يراقب الملفات التي تفتحها/تعدلها
✅ **دعم جميع اللغات** - Python, JavaScript, Java, C++, وأكثر
✅ **تحليل ذكي** - اكتشاف الأخطاء والتحسينات
✅ **توصيات AI** - اقتراحات بناءً على GPT-4
✅ **منصات متعددة** - Windows, macOS, Linux
✅ **API مرن** - يمكن تغيير API من الإعدادات
✅ **واجهة سهلة** - تصميم حديث وسهل الاستخدام

## 🛠️ المتطلبات

- Node.js 14+ و npm
- Python 3.8+
- مفتاح API من OpenAI أو خدمة أخرى

## 📥 التثبيت

### 1. استنساخ المشروع
```bash
git clone https://github.com/DARKOFFICAIL/DARKAI.git
cd DARKAI
git checkout setup-ai-bot
```

### 2. تثبيت المكتبات
```bash
# تثبيت مكتبات Node.js
npm install

# تثبيت مكتبات Python
pip install -r requirements.txt
```

### 3. تكوين API

عدّل ملف `src/config/api.config.json`:

```json
{
  "apiProvider": "openai",
  "apiKey": "your-api-key-here",
  "model": "gpt-4",
  "baseUrl": "https://api.openai.com/v1"
}
```

## ▶️ التشغيل

### وضع التطوير
```bash
npm run dev
```

### البناء للإنتاج
```bash
npm run build
```

### حزم التطبيق
```bash
npm run package
```

سيتم إنشاء ملفات التثبيت في مجلد `release/`:
- `DARKAI-Setup-x.x.x.exe` (Windows)
- `DARKAI-x.x.x.dmg` (macOS)
- `DARKAI-x.x.x.AppImage` (Linux)

## 📁 هيكل المشروع

```
DARKAI/
├── src/
│   ├── main/              # Electron Main Process
│   │   ├── main.js
│   │   └── preload.js
│   ├── renderer/          # React Frontend
│   │   ├── App.jsx
│   │   ├── components/
│   │   ├── public/
│   │   └── package.json
│   ├── backend/           # Python Analysis Engine
│   │   ├── analyzer.py
│   │   ├── language_detector.py
│   │   ├── ai_engine.py
│   │   └── __init__.py
│   ├── services/          # Services
│   │   ├── file_monitor.js
│   │   └── __init__.py
│   └── config/            # Configuration
│       ├── api.config.json
│       └── .env.example
├── extensions/            # Editor Extensions
│   ├── vscode/
│   ├── sublime/
│   └── jetbrains/
├── package.json
├── electron-builder.json
├── requirements.txt
└── README.md
```

## ⚙️ الإعدادات

### ملف API Config (`src/config/api.config.json`)

```json
{
  "apiProvider": "openai",        // مزود API
  "apiKey": "your-key",          // مفتاح API
  "model": "gpt-4",              // نموذج AI
  "baseUrl": "https://...",      // عنوان API
  "temperature": 0.7,            // درجة الإبداع (0-1)
  "maxTokens": 2000,             // أقصى طول النص
  "language": "ar",              // اللغة (en/ar/fr/etc)
  "debugMode": false,            // وضع الحفظ
  "enableFileMonitoring": true   // تفعيل مراقبة الملفات
}
```

### متغيرات البيئة (`.env`)

```env
API_PROVIDER=openai
API_KEY=your-api-key
APP_LANGUAGE=ar
APP_DEBUG=false
MONITOR_INTERVAL=1000
MONITOR_ENABLED=true
```

## 🎯 الاستخدام

### 1. تشغيل التطبيق
```bash
npm start
```

### 2. تكوين API (المرة الأولى)
- اذهب إلى tab "Settings" ⚙️
- أدخل مفتاح API الخاص بك
- اختر النموذج والإعدادات
- اضغط "Save Settings"

### 3. تحليل الكود

**الطريقة 1: تحليل يدوي**
- اذهب إلى tab "Analyzer"
- الصق الكود
- اضغط "Analyze Code"

**الطريقة 2: مراقبة حية**
- فتح ملف في محررك المفضل
- البوت سيراقبه تلقائياً عند التعديل
- ستظهر النتائج في Dashboard

### 4. عرض النتائج
- في Dashboard ستجد إحصائيات شاملة
- قائمة بآخر التحليل��ت
- الأخطاء والتحذيرات
- اقتراحات AI

## 🎨 الواجهة

### Tabs الرئيسية:

1. **Dashboard** 📊
   - إحصائيات عامة
   - آخر التحليلات
   - عدد المشاكل المكتشفة

2. **Analyzer** 🔍
   - تحليل يدوي للكود
   - عرض الأخطاء والتحذيرات
   - اقتراحات الحل

3. **Settings** ⚙️
   - إعدادات API
   - إعدادات التحليل
   - تفضيلات عامة

## 🐛 الأخطاء الشائعة وحلولها

### "API Key not configured"
- تأكد من إدخال مفتاح API صحيح في الإعدادات
- تحقق من أن المفتاح لم ينتهِ صلاحيته

### "Failed to analyze code"
- تحقق من اتصال الإنترنت
- تأكد من أن الكود ليس فارغاً
- تحقق من أن نوع الملف مدعوم

### "File monitor not working"
- تأكد من تفعيل مراقبة الملفات في الإعدادات
- جرب إعادة تشغيل التطبيق
- تحقق من صلاحيات المجلد

## 🌍 اللغات المدعومة

### البرمجة:
Python, JavaScript, TypeScript, Java, C, C++, C#, PHP, Ruby, Go, Rust, Kotlin, Swift, Objective-C, Scala, Haskell, R, MATLAB, SQL, HTML, CSS

### الواجهة:
English, العربية, Français, Deutsch, Español

## 📝 الملفات المدعومة

```
.py, .pyw, .pyx          # Python
.js, .mjs, .jsx          # JavaScript
.ts, .tsx                # TypeScript
.java                    # Java
.c                       # C
.cpp, .cc, .cxx          # C++
.cs                      # C#
.php                     # PHP
.rb                      # Ruby
.go                      # Go
.rs                      # Rust
.kt, .kts                # Kotlin
.swift                   # Swift
.m                       # Objective-C
.scala                   # Scala
.hs                      # Haskell
.r, .R                   # R
.sql                     # SQL
.html, .htm              # HTML
.css                     # CSS
```

## 🔌 مزودي API المدعومون

- **OpenAI** (GPT-4, GPT-3.5-turbo)
- **Claude** (يمكن الإضافة)
- **Local Models** (يمكن الإضافة)

## 🤝 المساهمة

نرحب بالمساهمات! يرجى:

1. عمل Fork للمشروع
2. إنشاء branch جديد (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add AmazingFeature'`)
4. Push إلى Branch (`git push origin feature/AmazingFeature`)
5. فتح Pull Request

## 🐛 الإبلاغ عن المشاكل

إذا واجهت مشكلة:

1. تحقق من [المشاكل الموجودة](https://github.com/DARKOFFICAIL/DARKAI/issues)
2. افتح [Issue جديد](https://github.com/DARKOFFICAIL/DARKAI/issues/new)
3. صِف المشكلة بوضوح مع لقطات شاشة إن أمكن

## 📜 الرخصة

MIT License - انظر ملف [LICENSE](LICENSE) للتفاصيل

## 👨‍💻 المطور

[DARKOFFICAIL](https://github.com/DARKOFFICAIL)

## 🎓 الموارد المفيدة

- [Electron Documentation](https://www.electronjs.org/docs)
- [React Documentation](https://react.dev)
- [Python AST Module](https://docs.python.org/3/library/ast.html)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## ⭐ شكراً!

إذا أعجبك المشروع، شارك الحب بنجمة ⭐

---

**Made with ❤️ by DARKOFFICAIL**
