#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔥 پروژه Super Slang Translator Pro
مترجم پیشرفته زبان خودمونی اینترنتی با قابلیت‌های جدید
نوشته شده توسط: [اسم تو]
ورژن: 3.0.0
"""

import json
import random
import os
from datetime import datetime
from typing import Dict, List, Optional

class SuperSlangTranslator:
    """
    کلاس پیشرفته مترجم خودمونی با قابلیت ذخیره و بازیابی دیکشنری
    """
    
    def __init__(self, user_name="کاربر"):
        """
        مقداردهی اولیه مترجم
        
        Args:
            user_name (str): نام کاربر برای شخصی‌سازی
        """
        self.user_name = user_name
        self.data_file = "slang_dictionary.json"
        self.slang_dict = self.load_dictionary()
        self.translation_history = []
        self.emojis = ["😎", "✌️", "🔥", "💯", "👌", "🚀", "💪", "🎯", "⚡", "💫"]
        self.hash_tags = ["#slang", "#cool", "#internet", "#lol", "#funny"]
        
    def load_dictionary(self) -> Dict[str, str]:
        """
        بارگذاری دیکشنری از فایل (اگر وجود داشته باشد)
        """
        default_dict = {
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
            "too long; didn't read": "tl;dr",
            "just kidding": "jk",
            "rolling on floor laughing": "rofl",
            "shaking my head": "smh",
            "facepalm": "fp",
            "as soon as possible": "asap"
        }
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    # ترکیب دیکشنری پیش‌فرض با دیکشنری ذخیره شده
                    default_dict.update(loaded)
                print(f"✅ دیکشنری از فایل {self.data_file} بارگذاری شد!")
            except:
                print("⚠️ خطا در بارگذاری فایل، استفاده از دیکشنری پیش‌فرض")
        else:
            print("📁 فایل دیکشنری یافت نشد، ایجاد فایل جدید...")
            self.save_dictionary(default_dict)
            
        return default_dict
    
    def save_dictionary(self, dictionary=None):
        """ذخیره دیکشنری در فایل"""
        if dictionary is None:
            dictionary = self.slang_dict
            
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(dictionary, f, ensure_ascii=False, indent=4)
            print(f"💾 دیکشنری در فایل {self.data_file} ذخیره شد!")
        except Exception as e:
            print(f"❌ خطا در ذخیره فایل: {e}")
    
    def translate(self, text: str, add_emoji: bool = True, add_hashtag: bool = False) -> str:
        """
        ترجمه متن ورودی به زبان خودمونی
        
        Args:
            text (str): متن اصلی
            add_emoji (bool): اضافه کردن شکلک
            add_hashtag (bool): اضافه کردن هشتگ
        
        Returns:
            str: متن ترجمه شده
        """
        if not text or not text.strip():
            return "⚠️ هیچ متنی وارد نشده!"
        
        original = text
        text_lower = text.lower().strip()
        translated = text_lower
        
        # جایگزینی کلمات (از طولانی به کوتاه)
        sorted_words = sorted(self.slang_dict.keys(), key=len, reverse=True)
        for word in sorted_words:
            translated = translated.replace(word, self.slang_dict[word])
        
        # ذخیره در تاریخچه
        self.translation_history.append({
            "original": original,
            "translated": translated,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        # اضافه کردن شکلک
        if add_emoji:
            translated += f" {random.choice(self.emojis)}"
        
        # اضافه کردن هشتگ
        if add_hashtag:
            translated += f" {random.choice(self.hash_tags)}"
        
        return translated
    
    def batch_translate(self, texts: List[str]) -> List[str]:
        """ترجمه چند متن به صورت همزمان"""
        results = []
        for text in texts:
            results.append(self.translate(text, add_emoji=True))
        return results
    
    def show_stats(self):
        """نمایش آمار مترجم"""
        print(f"\n📊 آمار مترجم {self.user_name}:")
        print(f"   📚 تعداد کلمات دیکشنری: {len(self.slang_dict)}")
        print(f"   📝 تعداد ترجمه‌های انجام شده: {len(self.translation_history)}")
        
        if self.translation_history:
            print(f"   ⏱️ آخرین ترجمه: {self.translation_history[-1]['time']}")
            print(f"   🔤 آخرین متن: {self.translation_history[-1]['original'][:30]}...")
    
    def show_history(self, limit: int = 5):
        """نمایش تاریخچه ترجمه"""
        if not self.translation_history:
            print("📭 تاریخچه ترجمه خالی است!")
            return
        
        print(f"\n📋 آخرین {min(limit, len(self.translation_history))} ترجمه:")
        for i, item in enumerate(self.translation_history[-limit:], 1):
            print(f"   {i}. [{item['time']}]")
            print(f"      ➡️ {item['original']}")
            print(f"      🔄 {item['translated']}")
    
    def add_custom_word(self, word: str, slang: str):
        """اضافه کردن کلمه جدید به دیکشنری"""
        word = word.lower().strip()
        slang = slang.lower().strip()
        
        if word in self.slang_dict:
            print(f"⚠️ کلمه '{word}' قبلاً وجود دارد!")
            overwrite = input("آیا می‌خواهید آن را بازنویسی کنید؟ (y/n): ").lower()
            if overwrite != 'y':
                return
        
        self.slang_dict[word] = slang
        self.save_dictionary()
        print(f"✅ کلمه '{word}' با معادل '{slang}' اضافه شد!")
    
    def remove_word(self, word: str):
        """حذف کلمه از دیکشنری"""
        word = word.lower().strip()
        if word in self.slang_dict:
            del self.slang_dict[word]
            self.save_dictionary()
            print(f"✅ کلمه '{word}' حذف شد!")
        else:
            print(f"❌ کلمه '{word}' یافت نشد!")
    
    def export_history(self, filename: str = "translation_history.txt"):
        """خروجی گرفتن از تاریخچه"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"تاریخچه ترجمه‌های {self.user_name}\n")
                f.write("=" * 50 + "\n")
                for item in self.translation_history:
                    f.write(f"[{item['time']}]\n")
                    f.write(f"اصلی: {item['original']}\n")
                    f.write(f"ترجمه: {item['translated']}\n")
                    f.write("-" * 30 + "\n")
            print(f"✅ تاریخچه در فایل {filename} ذخیره شد!")
        except Exception as e:
            print(f"❌ خطا در ذخیره فایل: {e}")


def print_menu():
    """نمایش منوی اصلی"""
    menu = f"""
╔{'═' * 50}╗
║{' ' * 12}🔥 SUPER SLANG TRANSLATOR PRO{' ' * 12}║
║{' ' * 15}نسخه ۳.۰ - حرفه‌ای{' ' * 18}║
╠{'═' * 50}╣
║ 1. 🔤 ترجمه متن                                          ║
║ 2. 📚 ترجمه چند متن (دسته‌ای)                            ║
║ 3. ➕ اضافه کردن کلمه جدید                                ║
║ 4. ❌ حذف کلمه                                            ║
║ 5. 📋 نمایش تاریخچه                                       ║
║ 6. 📊 نمایش آمار                                          ║
║ 7. 💾 ذخیره دیکشنری                                       ║
║ 8. 📤 خروجی تاریخچه                                       ║
║ 9. ❌ خروج                                                ║
╚{'═' * 50}╝
    """
    print(menu)


def main():
    """تابع اصلی برنامه"""
    print("\n" * 2)
    print("🚀 در حال راه‌اندازی Super Slang Translator Pro...")
    time.sleep(1)
    
    # دریافت نام کاربر
    name = input("👤 لطفاً نام خود را وارد کنید: ").strip()
    if not name:
        name = "کاربر"
    
    # ایجاد مترجم
    translator = SuperSlangTranslator(name)
    
    # حلقه اصلی برنامه
    while True:
        print_menu()
        choice = input("🔢 گزینه مورد نظر را انتخاب کنید: ").strip()
        
        if choice == "1":
            # ترجمه متن
            text = input("\n📝 متن خود را وارد کنید: ").strip()
            if text:
                result = translator.translate(text, add_emoji=True, add_hashtag=True)
                print(f"\n✅ نتیجه: {result}")
            else:
                print("⚠️ متنی وارد نشد!")
        
        elif choice == "2":
            # ترجمه دسته‌ای
            print("\n📚 چند جمله وارد کنید (هر جمله در یک خط، خط خالی برای پایان):")
            texts = []
            while True:
                line = input()
                if not line:
                    break
                texts.append(line)
            
            if texts:
                results = translator.batch_translate(texts)
                print("\n🎯 نتایج ترجمه:")
                for i, (orig, trans) in enumerate(zip(texts, results), 1):
                    print(f"\n   {i}. 📝 {orig}")
                    print(f"      🔄 {trans}")
            else:
                print("⚠️ متنی وارد نشد!")
        
        elif choice == "3":
            # اضافه کردن کلمه
            word = input("🔤 کلمه اصلی را وارد کنید: ").strip()
            slang = input("💬 معادل خودمونی را وارد کنید: ").strip()
            if word and slang:
                translator.add_custom_word(word, slang)
            else:
                print("⚠️ هر دو فیلد باید پر شوند!")
        
        elif choice == "4":
            # حذف کلمه
            word = input("🔤 کلمه مورد نظر برای حذف را وارد کنید: ").strip()
            if word:
                translator.remove_word(word)
        
        elif choice == "5":
            # نمایش تاریخچه
            limit = input("🔢 تعداد آیتم‌های اخیر (پیش‌فرض ۵): ").strip()
            limit = int(limit) if limit.isdigit() else 5
            translator.show_history(limit)
        
        elif choice == "6":
            # نمایش آمار
            translator.show_stats()
        
        elif choice == "7":
            # ذخیره دیکشنری
            translator.save_dictionary()
        
        elif choice == "8":
            # خروجی تاریخچه
            filename = input("📁 نام فایل خروجی (پیش‌فرض: translation_history.txt): ").strip()
            if not filename:
                filename = "translation_history.txt"
            translator.export_history(filename)
        
        elif choice == "9":
            # خروج
            print("\n👋 خداحافظ! به امید دیدار...")
            print("✨ از همراهی شما متشکریم")
            break
        
        else:
            print("❌ گزینه نامعتبر! لطفاً دوباره تلاش کنید.")
        
        input("\n⏎ برای ادامه Enter را بزنید...")
        print("\n" * 2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 خداحافظ! برنامه با موفقیت بسته شد.")
    except Exception as e:
        print(f"\n❌ خطای سیستمی: {e}")
        print("🛠️ لطفاً مشکل را گزارش دهید.")