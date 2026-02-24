#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 پروژه Hello World Pro
نسخه پیشرفته‌تر با قابلیت شخصی‌سازی و انیمیشن ساده
نوشته شده توسط: [اسم تو]
ورژن: 2.0.0
"""

import time
import sys
import platform
from datetime import datetime

class HelloWorld:
    """
    کلاس Hello World با قابلیت‌های پیشرفته
    """
    
    def __init__(self, name="دنیا", language="fa"):
        """
        مقداردهی اولیه
        
        Args:
            name (str): نام مخاطب
            language (str): کد زبان (fa, en, fr, es, de)
        """
        self.name = name
        self.language = language
        self.greetings = {
            "en": "Hello",
            "fa": "سلام",
            "fr": "Bonjour",
            "es": "Hola",
            "de": "Hallo",
            "ar": "مرحبا",
            "ru": "Привет",
            "zh": "你好",
            "hi": "नमस्ते",
            "tr": "Merhaba"
        }
        
    def slow_print(self, text, delay=0.03):
        """چاپ کاراکتر به کاراکتر با تاخیر (افکت تایپ)"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def get_greeting(self):
        """دریافت سلام متناسب با زبان انتخاب شده"""
        if self.language in self.greetings:
            return self.greetings[self.language]
        return self.greetings["en"]  # پیش‌فرض انگلیسی
    
    def get_system_info(self):
        """دریافت اطلاعات سیستم"""
        info = {
            "python_version": platform.python_version(),
            "system": platform.system(),
            "machine": platform.machine(),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return info
    
    def print_banner(self):
        """چاپ بنر خوش‌آمدگویی"""
        banner = f"""
╔{'═' * 50}╗
║{' ' * 15}🌸 HELLO WORLD PRO{' ' * 15}║
║{' ' * 12}نسخه ۲.۰ - ویژه برنامه‌نویسان{' ' * 11}║
╚{'═' * 50}╝
        """
        print(banner)
    
    def print_rainbow(self, text):
        """چاپ متن به صورت رنگین‌کمانی"""
        colors = [91, 93, 92, 96, 94, 95]  # کدهای رنگی ANSI
        for i, char in enumerate(text):
            color_code = colors[i % len(colors)]
            sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.02)
        print()
    
    def run(self):
        """اجرای اصلی برنامه"""
        self.print_banner()
        
        # اطلاعات سیستم
        info = self.get_system_info()
        print(f"\n📊 اطلاعات سیستم:")
        print(f"   🐍 Python: {info['python_version']}")
        print(f"   💻 OS: {info['system']}")
        print(f"   🕒 Time: {info['time']}")
        
        # سلام اصلی
        greeting = self.get_greeting()
        message = f"\n{greeting} {self.name}!"
        
        print("\n🤖 ربات سلام‌رسان می‌گوید:")
        self.slow_print(f"   {message}")
        
        # پیام به زبان‌های مختلف
        print("\n🌍 پیام به زبان‌های مختلف:")
        for lang, greet in list(self.greetings.items())[:5]:  # فقط ۵ تا اول
            print(f"   {lang.upper()}: {greet} {self.name}!")
        
        # انیمیشن شمارش معکوس
        print("\n⏰ شمارش معکوس برای شروع ماجراجویی:")
        for i in range(5, 0, -1):
            print(f"   {i}...")
            time.sleep(0.5)
        
        # متن نهایی رنگین‌کمانی
        print("\n🎨 پیام نهایی (به سبک رنگین‌کمان):")
        self.print_rainbow("   🚀 Let's Code with Python!")
        
        # امضا
        print("\n" + "=" * 50)
        print("✨ با عشق از تیم برنامه‌نویسی")
        print("📅 " + datetime.now().strftime("%B %d, %Y"))
        print("=" * 50)


def main():
    """نقطه ورود برنامه"""
    # دریافت ورودی از کاربر
    name = input("👤 لطفاً نام خود را وارد کنید (پیش‌فرض: دنیا): ").strip()
    if not name:
        name = "دنیا"
    
    # انتخاب زبان
    print("\n🌐 زبان مورد نظر را انتخاب کنید:")
    print("   1. فارسی (fa)")
    print("   2. انگلیسی (en)")
    print("   3. فرانسوی (fr)")
    print("   4. اسپانیایی (es)")
    print("   5. آلمانی (de)")
    
    lang_choice = input("🔢 شماره زبان را وارد کنید (پیش‌فرض: ۱): ").strip()
    lang_map = {"1": "fa", "2": "en", "3": "fr", "4": "es", "5": "de"}
    language = lang_map.get(lang_choice, "fa")
    
    # پاکسازی صفحه (اختیاری)
    print("\n" * 2)
    
    # اجرای برنامه
    app = HelloWorld(name, language)
    app.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 خداحافظ! به امید دیدار مجدد...")
    except Exception as e:
        print(f"\n❌ خطایی رخ داد: {e}")