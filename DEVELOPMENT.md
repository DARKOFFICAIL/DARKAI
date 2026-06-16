# DARKAI Development Guide

## 🏗️ معمارية المشروع

### Main Process (Electron)
يدير نافذة التطبيق ويتواصل مع نظام التشغيل.

### Renderer Process (React)
تصميم الواجهة الأمامية وتجربة المستخدم.

### Backend (Python)
محرك التح��يل والذكاء الاصطناعي.

## 🔄 سير العمل

```
ملف مفتوح
    ↓
File Monitor يكتشف التغيير
    ↓
كود مُرسَل للتحليل
    ↓
Language Detector يحدد اللغة
    ↓
CodeAnalyzer يفحص الأخطاء
    ↓
AIEngine يطلب الاقتراحات
    ↓
النتائج تُظهر للمستخدم
```

## 📦 الإضافات والتحسينات المستقبلية

- [ ] إضافة مزودي API إضافيين (Claude, Local Models)
- [ ] ملحقات VS Code محسّنة
- [ ] دعم لغات إضافية
- [ ] تخزين محلي للنتائج
- [ ] مشاركة النتائج
- [ ] Linting متقدم
- [ ] اختبارات وحدة
- [ ] معاينة الأخطاء مباشرة في المحرر

## 🧪 الاختبار

```bash
# تشغيل الاختبارات
npm test

# اختبارات Python
pytest src/backend/
```

## 📚 البناء والتوزيع

### بناء محلي
```bash
npm run build
```

### التوزيع
```bash
# Windows
npm run package-win

# macOS
npm run package-mac

# Linux
npm run package-linux
```

## 🔐 الأمان

- مفاتيح API مخزنة محلياً فقط
- لا توجد بيانات شخصية مُر��َلة
- اتصالات مشفرة مع API

## 🎓 دليل المساهم

### إضافة لغة برمجية جديدة

1. أضف الامتداد في `src/backend/language_detector.py`
2. أضف دالة الفحص في `src/backend/analyzer.py`
3. اختبر مع ملفات عينة
4. افتح Pull Request

### إضافة مزود API جديد

1. عدّل `src/backend/ai_engine.py`
2. أضف method جديد `_get_{provider}_suggestions`
3. حدّث `src/config/api.config.json.example`
4. أضف الاختبارات

## 📞 الدعم

للمساعدة:
- فتح Issue على GitHub
- تقديم Pull Request
- التواصل عبر البريد الإلكتروني

---

**Happy Coding! 🚀**
