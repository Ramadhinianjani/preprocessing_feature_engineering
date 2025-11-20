# preprocessing_feature_engineering

![Step 1](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T1.png)

Penjelasan:
    Perintah !python preprocessing_feature_engineering.py yang terlihat pada gambar merupakan instruksi untuk menjalankan sebuah file Python bernama preprocessing_feature_engineering.py di dalam lingkungan notebook seperti Jupyter Notebook atau Google Colab. Tanda seru (!) digunakan untuk mengeksekusi perintah command line langsung dari sel notebook. Ketika perintah ini dijalankan, seluruh kode yang ada di dalam file tersebut akan dieksekusi, termasuk proses data preprocessing dan feature engineering yang sudah disusun sebelumnya—misalnya pembersihan data, normalisasi, encoding, pembuatan fitur baru, atau transformasi lainnya. Dengan mengeksekusi file ini, user dapat menjalankan seluruh rangkaian tahapan preprocessing secara otomatis tanpa harus menuliskan ulang kode di dalam notebook. Ini memastikan workflow menjadi lebih rapi, terstruktur, dan mudah direproduksi.

![Step 1](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T2.png)

Penjelasan:
Kode pada gambar menunjukkan proses pemuatan dataset hasil preprocessing menggunakan pandas. File preprocessed_dataset.csv dibaca ke dalam DataFrame dengan pd.read_csv(), lalu df.head() menampilkan lima baris pertama untuk memastikan datanya sudah benar. Dari output terlihat bahwa data telah melalui tahap normalisasi pada fitur numerik dan one-hot encoding pada fitur kategorikal, sehingga muncul kolom seperti Gender_Male, Satisfaction_Low, dan Satisfaction_Medium. Tampilan ini memastikan bahwa hasil preprocessing dan feature engineering sudah berhasil diterapkan dan siap digunakan untuk analisis atau pemodelan berikutnya.
