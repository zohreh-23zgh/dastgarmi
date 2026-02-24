def main():
    """تابع اصلی برنامه - نقطه شروع اجرا"""
    
    # چاپ ساده Hello World
    print("Hello, World!")
    
    # چاپ به زبان‌های مختلف
    print("\n🌸 Hello World به زبان‌های مختلف:")
    print("   English:  Hello, World!")
    print("   Persian:   سلام دنیا!")
    print("   French:    Bonjour le monde!")
    print("   Spanish:   ¡Hola mundo!")
    print("   German:    Hallo Welt!")
    print("   Arabic:    مرحبا بالعالم!")
    
    # کار با متغیر ساده
    name = "Python Programmer"
    print(f"\n👋 خوش آمدی {name}!")
    
    # یک پیام تشویق‌آمیز
    print("\n✨ اولین قدمت رو در پایتون برداشتی!")
    print("🚀 ادامه بده، دنیای برنامه‌نویسی منتظرته...")

    # شمارش معکوس ساده
    print("\n⏰ شمارش معکوس برای شروع ماجراجویی:")
    for i in range(5, 0, -1):
        print(f"   {i}...")
    print("   💫 برو که رفتیم!")


if __name__ == "__main__":
    main()