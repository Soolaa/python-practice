# Guess the Number Game 🔢

یک بازی ساده‌ی حدس عدد که در آن کامپیوتر یک عدد تصادفی بین ۱ تا ۱۰۰ انتخاب می‌کند و کاربر باید آن را حدس بزند.

## قوانین بازی

- در ابتدا سطح دشواری انتخاب می‌شود:
  - **easy**: ۱۰ فرصت حدس زدن
  - **hard**: ۵ فرصت حدس زدن
- بعد از هر حدس، برنامه می‌گوید عدد وارد شده بزرگ‌تر است یا کوچک‌تر (`Too high!` / `Too low!`)
- اگر فرصت‌ها قبل از حدس درست تمام شود، بازی باخته می‌شود.

## اجرای برنامه

```bash
python guess.py
```

## فایل‌ها

- `guess.py` — منطق اصلی بازی
- `art.py` — لوگوی ASCII که ابتدای بازی نمایش داده می‌شود

## چیزهایی که در این تمرین یاد گرفتم / تمرین کردم

- تولید عدد تصادفی با `random.randint`
- کار با `while` loop برای ادامه‌ی بازی تا حدس درست یا اتمام فرصت‌ها
- نوشتن تابع با مقدار بازگشتی (`return`) برای مدیریت تعداد فرصت‌های باقی‌مانده
- import کردن یک فایل دیگر (`art.py`) به‌عنوان ماژول

## نمونه‌ی اجرا

```
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low!
You have 9 attempts remaining to guess the number.
Make a guess: 75
Too high!
...
You guessed the number! Well done!
```