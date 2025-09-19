# تمرین فلاسک

برای clone کردن داخل VS Code:

1. آدرس این مخزن را کپی کنید
2. به VS Code بروید
3. منو دستور را با استفاده از <kbd dir="ltr"><kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd></kbd> باز کنید
4. دستور <kbd dir="ltr">Git: Clone</kbd> را انتخاب کنید
5. آدرس را پیست کنید
6. یک فولدر جهت clone انتخاب کنید

برای نصب کردن:

1. ترمینال را باز کنید
2. یک [محیط مجازی](https://docs.python.org/3/library/venv.html) برای این تمرین ایجاد کنید:

   ```sh
   python3 -m venv .venv
   ```
3. آن را فعال کنید:
   - cmd.exe:

     ```batch
     .venv\Scripts\activate.bat
     ```
   - powershell:

     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - bash/zsh:

     ```sh
     source .venv/bin/activate
     ```
4. بسته‌های لازم را نصب کنید:

   ```sh
   pip3 install -r requirements.txt
   ```

برای اجرا کردن:

1. ترمینال را باز کنید
2. محیط مجازی را فعال کنید
3. فلاسک را اجرا کنید

   ```sh
   flask --app exercise run
   ```
