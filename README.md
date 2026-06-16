# 🤖 DARKAI - AI Code Assistant Desktop Bot

بوت ذكي متعدد اللغات لمراقبة الحية للكود وتصحيح الأخطاء في أي تطبيق برمجة

## ✨ المميزات

- 📱 **تطبيق Desktop** (Windows, macOS, Linux)
- 🔍 **مراقبة حية** للكود أثناء الكتابة
- 🌐 **دعم كل لغات البرمجة**
- 🧠 **ذكاء اصطناعي** لاكتشاف الأخطاء
- ⚙️ **قابل للتخصيص** - API خارجي في ملف منفصل
- 🎨 **واجهة سهلة الاستخدام**

## 🏗️ معمارية المشروع

```
DARKAI/
├── src/
│   ├── main/                    # نقطة البداية (Electron Main)
│   │   └── main.js
│   ├── renderer/                # واجهة المستخدم (React)
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── styles/
│   ├── backend/                 # محرك البوت (Python)
│   │   ├── analyzer.py
│   │   ├── language_detector.py
│   │   ├── ai_engine.py
│   │   └── __init__.py
│   ├── services/                # خدمات متعددة
│   │   ├── file_monitor.py      # مراقبة الملفات
│   │   ├── code_runner.py       # تشغيل الكود
│   │   └── api_manager.py       # إدارة API
│   └── config/
│       ├── api.config.json      # ملف API (منفصل)
│       └── default.config.json
├── extensions/                  # ملحقات المحررات
│   ├── vscode/
│   ├── sublime/
│   └── jetbrains/
├── build/                       # ملفات البناء
├── dist/                        # التوزيعات
├── package.json
├── electron-builder.json
└── requirements.txt
```

## 🖥️ الأنظمة المدعومة

| النظام | الإصدار | الحالة |
|--------|---------|--------|
| Windows | 7+ | ✅ مدعوم |
| macOS | 10.12+ | ✅ مدعوم |
| Linux | Ubuntu 18.04+ | ✅ مدعوم |

## 🚀 البدء السريع

### المتطلبات
- Node.js 14+
- Python 3.8+
- npm / yarn

### التثبيت

```bash
# استنساخ المشروع
git clone https://github.com/DARKOFFICAIL/DARKAI.git
cd DARKAI

# تثبيت المكتبات
npm install
pip install -r requirements.txt
```

### تكوين API

عدّل ملف `src/config/api.config.json`:

```json
{
  "apiProvider": "openai",
  "apiKey": "your-api-key-here",
  "model": "gpt-4",
  "baseUrl": "https://api.openai.com/v1",
  "temperature": 0.7,
  "maxTokens": 2000,
  "language": "ar",
  "debugMode": false
}
```

### التشغيل

```bash
# تطوير
npm run dev

# بناء للإنتاج
npm run build

# تشغيل الإصدار النهائي
npm start

# حزم التطبيق
npm run package
```

## 📦 المكونات الرئيسية

### 1. Desktop Application
تطبيق محلي يعمل على نظامك بدون اتصال بخادم

### 2. File Monitor
مراقبة الملفات المفتوحة في المحررات في الوقت الفعلي

### 3. Code Analyzer
فحص الأخطاء والأخطاء المنطقية والتحسينات

### 4. AI Engine
استخدام نماذج AI (OpenAI, Claude, etc) للتحليل الذكي

### 5. Real-time Notifications
تنبيهات فورية عند اكتشاف خطأ مع اقتراحات الحل

## 🔧 اللغات البرمجية المدعومة

- Python
- JavaScript / TypeScript
- Java
- C / C++
- C#
- PHP
- Ruby
- Go
- Rust
- Kotlin
- Swift
- Objective-C
- Scala
- Haskell
- R
- MATLAB
- SQL
- HTML / CSS

## ⚙️ الإعدادات

### ملف API Config
ملف منفصل يمكن تعديله بسهولة:

```json
{
  "apiProvider": "openai",
  "apiKey": "your-key",
  "model": "gpt-4",
  "baseUrl": "https://api.openai.com/v1",
  "temperature": 0.7,
  "maxTokens": 2000,
  "language": "ar",
  "debugMode": false
}
```

### متغيرات البيئة

إنشاء ملف `.env`:

```env
API_PROVIDER=openai
API_KEY=your-api-key
APP_LANGUAGE=ar
DEBUG=false
MONITOR_INTERVAL=1000
```

## 📖 الاستخدام

### 1. تشغيل التطبيق
```bash
npm start
```

### 2. فتح محرر الأكواد
افتح VS Code أو أي محرر آخر

### 3. البوت يراقب
سيبدأ البوت بمراقبة الملفات التي تفتحها تلقائياً

### 4. تصحيح الأخطاء
عند اكتشاف خطأ سيظهر إشعار مع الحل المقت��ح

## 🔨 التطوير

```bash
# تشغيل في وضع التطوير مع Hot Reload
npm run dev

# الاختبارات
npm test

# بناء التوزيع
npm run build

# حزم التطبيق
npm run package
```

## 📦 التوزيعات المتاحة

- Windows Installer (.exe)
- macOS App (.dmg)
- Linux AppImage (.AppImage)
- Portable versions

## 🐛 الإبلاغ عن الأخطاء

[إنشاء issue جديد](https://github.com/DARKOFFICAIL/DARKAI/issues/new)

## 📝 الترخيص

MIT License

## 👨‍💻 المطور

[DARKOFFICAIL](https://github.com/DARKOFFICAIL)

## 🤝 المساهمة

نرحب بالمساهمات! الرجاء فتح PR

---

**شارك الحب ⭐ إذا أعجبك المشروع!**
