import fitz  # PyMuPDF
import os

# المسار الرئيسي للمجلد على جهازك الماك
base_path = "/Users/baderalmutairi/Desktop/الانظمه السعوديه"

# الأقسام الفرعية كما تظهر في صورك
sub_folders = {
    "الدفاع المدني": "data/raw/defense",
    "السلامه والصحه المهنيه": "data/raw/safety",
    "الكود السعودي": "data/raw/sbc"
}

def extract_from_folder(folder_name, output_folder):
    input_path = os.path.join(base_path, folder_name)
    
    # التأكد من وجود مجلد المخرجات (في جهازك مؤقتاً)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    if not os.path.exists(input_path):
        print(f"⚠️ المسار غير موجود: {input_path}")
        return

    for filename in os.listdir(input_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_path, filename)
            try:
                doc = fitz.open(pdf_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                # حفظ النص في ملف .txt
                txt_filename = filename.replace(".pdf", ".txt")
                with open(os.path.join(output_folder, txt_filename), "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"✅ تم استخراج: {filename}")
            except Exception as e:
                print(f"❌ خطأ في ملف {filename}: {e}")

if __name__ == "__main__":
    for folder_name, out_folder in sub_folders.items():
        print(f"--- جاري العمل على مجلد: {folder_name} ---")
        extract_from_folder(folder_name, out_folder)
    print("\n🚀 اكتملت عملية استخراج النصوص بنجاح!")
