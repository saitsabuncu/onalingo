---

# 📘 OnaLingo – Django REST API (MVP Sürümü)

OnaLingo, kullanıcıların seviye bazlı dil öğrenimini destekleyen bir konuşma temelli dil öğrenme platformudur. Bu repo, projenin backend (sunucu tarafı) kodlarını içerir.

---

## 🚀 Kurulum Adımları

### 1. Projeyi Klonla

```bash
git clone https://github.com/saitsabuncu/onalingo.git
cd onalingo
```

### 2. Sanal Ortam Oluştur

```bash
python -m venv onalingo-env
onalingo-env\Scripts\activate  # (Windows için)
```

### 3. Gerekli Paketleri Kur

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Veritabanı İşlemleri

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Süper Kullanıcı Oluştur

```bash
python manage.py createsuperuser
```

### 6. Geliştirme Sunucusunu Başlat

```bash
python manage.py runserver
```

---

## 🔐 JWT Authentication Sistemi

| Endpoint                   | Görev                               |
| -------------------------- | ----------------------------------- |
| `POST /api/token/`         | Kullanıcı adı ve şifre ile token al |
| `POST /api/token/refresh/` | Token yenile                        |

Postman veya frontend tarafında her istekte header'a şunu ekleyin:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📚 API Endpoint’leri

| Endpoint              | Metod      | Açıklama                                           |
| --------------------- | ---------- | -------------------------------------------------- |
| `/api/levels/`        | GET        | Seviye listesi (A1, A2, B1...)                     |
| `/api/lessons/`       | GET, POST  | Dersleri listele / oluştur (POST sadece admin)     |
| `/api/progress/`      | GET, POST  | İlerlemeni gör / yeni kayıt ekle                   |
| `/api/progress/<id>/` | GET, PATCH | Belirli ilerleme verisini gör / güncelle           |
| `/api/speaking/`      | GET, POST  | Konuşma ses kaydı & geri bildirim gönder / listele |

---

## 🗂️ Klasör Yapısı (Özet)

```
onalingo_backend/
├── manage.py
├── onalingo_backend/
│   ├── settings.py
│   ├── urls.py
├── users/
│   ├── models.py
│   ├── serializers.py
├── lessons/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── permissions.py
```

---

## 💡 Geliştirici Notları

* Her kullanıcı sadece **kendi progress** ve **speaking feedback** verilerine erişebilir.
* `admin/` paneli içerik yönetimi için aktiftir.
* MVP sonrası aşamalarda:

  * 🔴 Canlı ders entegrasyonu (Jitsi, Zoom)
  * 🌐 Çoklu dil desteği
  * 💳 Ödeme altyapısı (Stripe, iyzico)
  * 📈 Gelişmiş analiz modülleri
    planlanabilir.

---

## 👨‍💻 Geliştirici

**Mustafa Sait Sabuncu**
GitHub: [@saitsabuncu](https://github.com/saitsabuncu)

---
