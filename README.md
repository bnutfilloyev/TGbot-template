<p align="center"><h1 align="center">AIOGram template</h1></p>
<p align="center"><h3 align="center">🇺🇿 | Telegram botlar uchun shablon.</h3></p>



## Template arxitekturasi

- AIOGram 2.x (https://docs.aiogram.dev/en/latest/)
- MongoDB (https://www.mongodb.com/)
- Docker (https://www.docker.com/)

Botda local foydalanayotganda siz `mongodb-express` dan ham foydalansangiz bo'ladi.
Botni docker orqali ishga tushirgandan keyin: http://localhost:8081

## Foydalanish bo'yicha yo'riqnoma:

Barcha configlar `config.py` faylida joylashgan. Botni ishga tushirishdan oldin, `.env.dist` faylini `.env` ga
o'zgartiring va configlarni to'g'rilang.

### Botni ishga tushirish:

```bash
 $ pip install -r requirements.txt
 $ python3 app.py
```

### Botni ishga tushirish Docker bilan:

```bash
 $ docker build -t aiogram-bot .
 $ docker run -d --name aiogram-bot aiogram-bot
```

### Botni ishga tushirish Docker bilan va Docker Compose bilan:

```bash
 $ docker-compose up -d --build
```

## Serverga yuklash

Ishga tushirish uchun quyidagi buyruqlardan foydalansangiz bo'ladi.

```bash
 $ docker-compose -f docker-compose.prod.yml up -d --build 
```

Loglarni ko'rish uchun quyidagi buyruqdan foydalansangiz bo'ladi. Docker logs haqida bu yerdan ma'lumot olishingiz
mumkin: https://docs.docker.com/config/containers/logging/configure/

```bash
 $ docker-compose -f docker-compose.prod.yml logs -f 
```

## Qo'shimcha ma'lumotlar

- Botda juda ko'p qo'llaniladigan `boardcaster` funksiyalari mavjuda. Tekshirish uchun [bu](utils/broadcaster.py) yerni
  bosing.
- Bot ishga tushganda barcha adminlarga xabar boradi.
- Botning commandalarini ko'rish va o'zgartirish uchun [bu](utils/set_bot_commands.py) yerni bosing.

## Hissa qo'shish

    Template O'zbek telegram bot hamjamiyati uchun yaratilgan. 
    Agar sizda biror takliflar bo'lsa, PR yuboring.

