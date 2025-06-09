
from playwright.sync_api import sync_playwright

# بيانات الدخول
email = "f66257000@gmail.com"
password = "XmWn6E7/_8+5GL3"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.microworkers.com/login.php")

        # تعبئة بيانات تسجيل الدخول
        page.fill('input[name="email"]', email)
        page.fill('input[name="password"]', password)
        page.click('input[type="submit"]')
        page.wait_for_timeout(5000)

        # التحقق من نجاح الدخول
        if "dashboard" in page.url:
            print("✅ تم تسجيل الدخول بنجاح!")
        else:
            print("❌ فشل تسجيل الدخول أو هناك مشكلة.")

        # الانتقال إلى صفحة المهام
        page.goto("https://www.microworkers.com/jobs_available.php")
        page.wait_for_timeout(3000)
        print("📄 تم الدخول إلى صفحة المهام بنجاح.")

        # البحث عن أول مهمة متاحة والنقر عليها
        try:
            task_link = page.query_selector('a[href*="showjob"]')
            if task_link:
                task_link.click()
                page.wait_for_timeout(3000)
                print("✅ تم فتح أول مهمة بنجاح!")
            else:
                print("⚠️ لم يتم العثور على مهمة.")
        except Exception as e:
            print(f"❌ حدثت مشكلة أثناء محاولة فتح المهمة: {e}")

        browser.close()

run()
