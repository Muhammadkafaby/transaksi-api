# Dokumentasi API Transaksi

Base URL: `https://transaksi-api-d5491b2b258c.herokuapp.com`

## Endpoints

### 1. Tambah Transaksi
- **URL:** `/api/transaksi`
- **Method:** `POST`
- **Headers:** `Content-Type: application/json`
- **Body (JSON):**
```
{
  "nama_transaksi": "string",
  "mata_uang_asal": "USD|IDR",
  "mata_uang_tujuan": "USD|IDR",
  "jumlah_usd": number,
  "jumlah_idr": number,
  "nilai_tukar": number,
  "tanggal": "YYYY-MM-DD",
  "kategori_transaksi": "string",
  "gambar": "string|null",
  "status_pembayaran": "Paid|Pending|Success",
  "catatan": "string|null"
}
```
- **Response:** `201 Created`

### 2. Lihat Semua Transaksi
- **URL:** `/api/transaksi`
- **Method:** `GET`
- **Response:** `200 OK`, list transaksi

### 3. Lihat Transaksi Berdasarkan ID
- **URL:** `/api/transaksi/<id>`
- **Method:** `GET`
- **Response:** `200 OK` (jika ditemukan), `404 Not Found` (jika tidak)

### 4. Update Transaksi
- **URL:** `/api/transaksi/<id>`
- **Method:** `PUT`
- **Headers:** `Content-Type: application/json`
- **Body:** (sama seperti POST)
- **Response:** `200 OK` (jika berhasil), `404 Not Found` (jika tidak)

### 5. Hapus Transaksi
- **URL:** `/api/transaksi/<id>`
- **Method:** `DELETE`
- **Response:** `200 OK` (jika berhasil), `404 Not Found` (jika tidak)

## Contoh Request POST
```
POST /api/transaksi
Content-Type: application/json

{
  "nama_transaksi": "Pembelian Buku",
  "mata_uang_asal": "USD",
  "mata_uang_tujuan": "IDR",
  "jumlah_usd": 10,
  "jumlah_idr": 150000,
  "nilai_tukar": 15000,
  "tanggal": "2025-05-23",
  "kategori_transaksi": "Belanja",
  "gambar": null,
  "status_pembayaran": "Paid",
  "catatan": "Buku Python"
}
```

## Catatan
- Semua field bertanda `null` boleh dikosongkan.
- Gunakan header `Content-Type: application/json` untuk POST dan PUT.
- Response error akan diberikan dalam format JSON.
