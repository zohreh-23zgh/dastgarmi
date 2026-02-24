class SlangTranslator:
    """
    کلاس مترجم خودمونی - تبدیل کلمات معمولی به slang اینترنتی
    """
    
    def __init__(self):
        """ایجاد دیکشنری کلمات خودمونی"""
        self.slang_dict = {
            "hello": "heyy",
            "hi": "heyy",
            "good": "gud",
            "great": "gr8",
            "thanks": "thx",
            "thank you": "thx",
            "please": "pls",
            "ok": "k",
            "okay": "k",
            "see you": "cya",
            "later": "l8r",
            "tomorrow": "2moro",
            "today": "2day",
            "tonight": "2nite",
            "for": "4",
            "before": "b4",
            "friend": "fren",
            "love": "luv",
            "you": "u",
            "your": "ur",
            "are": "r",
            "why": "y",
            "because": "cuz",
            "cool": "kewl",
            "what": "wat",
            "please": "plz",
            "oh my god": "omg",
            "laugh out loud": "lol",
            "be right back": "brb",
            "by the way": "btw",
            "in my opinion": "imo",
            "too long; didn't read": "tl;dr"
        }
    
    def translate(self, text):
        """
        ترجمه متن ورودی به زبان خودمونی
        
        Args:
            text (str): متن اصلی
        
        Returns:
            str: متن ترجمه شده
        """
        if not text:
            return "⚠️ هیچ متنی وارد نشده!"
        
        # تبدیل متن به حروف کوچک
        text_lower = text.lower()
        translated = text_lower
        
        # جایگزینی کلمات
        for word, slang in self.slang_dict.items():
            translated = translated.replace(word, slang)
        
        # اضافه کردن شکلک رندوم
        import random
        emojis = [" 😎", " ✌️", " 🔥", " 💯", " 👌", " 🚀"]
        
        return translated + random.choice(emojis)
    
    def add_slang(self, word, slang):
        """اضافه کردن کلمه جدید به دیکشنری"""
        self.slang_dict[word.lower()] = slang.lower()
        print(f"✅ کلمه '{word}' با معادل '{slang}' به دیکشنری اضافه شد!")


def main():
    """تابع اصلی برنامه"""
    print("=" * 60)
    print("🔥 مترجم خودمونی اینترنتی (Internet Slang Translator)")
    print("=" * 60)
    
    # ساختن نمونه از مترجم
    translator = SlangTranslator()
    
    # نمایش دیکشنری فعلی
    print("\n📖 دیکشنری فعلی (نمایش ۱۰ تا از کلمات):")
    count = 0
    for word, slang in translator.slang_dict.items():
        if count < 10:
            print(f"   {word} -> {slang}")
            count += 1
    print("   ...")
    
    # چند مثال از ترجمه
    examples = [
        "Hello my friend",
        "See you later",
        "Thanks for your help",
        "Oh my god, this is cool",
        "I will be right back",
        "By the way, I love you"
    ]
    
    print("\n🔤 چند نمونه ترجمه:")
    for i, example in enumerate(examples, 1):
        translated = translator.translate(example)
        print(f"\n   {i}. 📝 {example}")
        print(f"      ➡️ {translated}")
    
    # بخش تعاملی
    print("\n" + "=" * 60)
    print("💬 بخش تعاملی (چند تا جمله خودت امتحان کن!)")
    
    # سه جمله نمونه از کاربر
    test_sentences = [
        input("\nجمله اول: "),
        input("جمله دوم: "),
        input("جمله سوم: ")
    ]
    
    print("\n🎯 نتایج ترجمه:")
    for i, sentence in enumerate(test_sentences, 1):
        if sentence.strip():
            result = translator.translate(sentence)
            print(f"\n   {i}. 📝 {sentence}")
            print(f"      ➡️ {result}")
    
    print("\n" + "=" * 60)
    print("🎉 ممنون از استفاده! بعداً می‌تونی کلمات جدید به دیکشنری اضافه کنی")
    print("=" * 60)


if __name__ == "__main__":
    main()