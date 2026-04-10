# Saudi Safety & Health Law Intelligence (SSLI) 🇸🇦
### نظام ذكاء اصطناعي لتحليل وتصور شبكة القوانين والأنظمة السعودية للسلامة والصحة المهنية

## 📌 Project Overview
هذا المشروع يهدف إلى بناء "شبكة ذكاء" تربط الأنظمة التشريعية السعودية ببعضها (مثل نظام العمل، كود البناء السعوديه واشتراطات الدفاع المدني). باستخدام تقنيات معالجة اللغات الطبيعية، نقوم بتحويل النصوص القانونية إلى شبكة مرئية توضح الترابط والتشابه بين المواد القانونية المختلفة لتسهيل 
الامتثال (Compliance) وتقليل المخاطر التشغيلية.

هذا العمل هو جزء من المحرك الأساسي لمشروع آخر للأتمتة والتدقيق في سلامة المواقع.

## 🚀 Key Features
* **Similarity Mapping:** ربط المواد القانونية المتشابهة في أنظمة مختلفة باستخدام نموذج AraBERT.
* **Network Visualization:** رسم شبكة علاقات تفاعلية توضح "عناقيد" (Clusters) المواضيع القانونية.
* **Impact Analysis:** تحليل أثر التغيير في مادة قانونية على المواد المرتبطة بها في الأنظمة الأخرى.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **NLP Model:** AraBERT / CAMeL Tools (for Arabic context understanding)
* **Similarity:** Cosine Similarity / Euclidean Distance
* **Visualization:** NetworkX / Plotly
* **Framework:** Scikit-learn, Pandas

## 📂 Repository Structure
* `/data`: الأنظمة السعودية الخام (Raw Data) والمعالجة (Processed).
* `/scripts`: أكواد التنظيف والتحليل (Preprocessing & Similarity).
* `/notebooks`: تجارب البحث والتحليل الأولي (Jupyter Notebooks).
* `/outputs`: الصور النهائية لشبكة العلاقات القانونية.

## 💡 Acknowledgement

---
**Developed by:** Bader B. Almutairi (Abu Bejad)  
**Affiliation:** MYSELF
