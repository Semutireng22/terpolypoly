# Terpolly Auto Spin

## Fitur

- Mendukung multi-akun
- Menggunkan kode auth sehingga tidak menyebabkan akun telegram di banned

## Prasyarat

- Python 3.x
- Pustaka `requests`
- Pustaka `colorama`

## Instalasi

1. **Clone repository atau unduh file script:**
    ```bash
    git clone https://github.com/Semutireng22/terpolypoly.git
    cd terpolypoly
    ```

2. **Buat file `tokens.txt` dan isi dengan `Kode Auth` untuk setiap akun:**
    ```nano
    nano tokens.txt
    ```
    Lalu isi dengan format berikut (1 baris 1 akun)
    ```
    eyjxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    eyjxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

4. **Instal pustaka yang diperlukan:**
    ```bash
    pip install requests colorama
    ```

5. **Jalankan program:**
    ```bash
    python3 bot.py
    ```

## Cara Mendapatkan `Kode Auth` dari Session Storage

Untuk mendapatkan `Kode auth` dari session storage di browser Anda:

1. Buka bot terpoly dan klik kanan lakukan inspect
2. Buka Developer Tools (biasanya dengan menekan `F12` atau klik kanan dan pilih "Inspect").
3. Pergi ke tab `Application/Aplikasi`.
4. Di sidebar kiri, di bawah `Storage`, pilih `Session Storage`.
5. Temukan URL situs web di bawah `Session Storage`.
6. Cari entri yang berisi `Jwt`.
7. Salin nilai `jwt` tersebut dan tempelkan ke dalam file `tokens.txt`.

## Cara Alternatif Untuk Mendapatkan Kode Auth

Buat yang gak punya pc bisa juga dengan login dari web.telegram.org.
Caranya juga sama seperti [Di Atas](#cara-mendapatkan-kode-auth-dari-session-storage)


## Catatan

- Pastikan file `tokens.txt` berada di direktori yang sama dengan script Python.
- Untuk menjalankan 24jam nonstop gunakanlah screeen
## Lisensi

Program ini dilisensikan di bawah [MIT License](LICENSE).
