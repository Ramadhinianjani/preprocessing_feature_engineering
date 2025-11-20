# preprocessing_feature_engineering

![Step 1](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T1.png)

Penjelasan:
    Perintah !python preprocessing_feature_engineering.py yang terlihat pada gambar merupakan instruksi untuk menjalankan sebuah file Python bernama preprocessing_feature_engineering.py di dalam lingkungan notebook seperti Jupyter Notebook atau Google Colab. Tanda seru (!) digunakan untuk mengeksekusi perintah command line langsung dari sel notebook. Ketika perintah ini dijalankan, seluruh kode yang ada di dalam file tersebut akan dieksekusi, termasuk proses data preprocessing dan feature engineering yang sudah disusun sebelumnya—misalnya pembersihan data, normalisasi, encoding, pembuatan fitur baru, atau transformasi lainnya. Dengan mengeksekusi file ini, user dapat menjalankan seluruh rangkaian tahapan preprocessing secara otomatis tanpa harus menuliskan ulang kode di dalam notebook. Ini memastikan workflow menjadi lebih rapi, terstruktur, dan mudah direproduksi.

![Step 2](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T2.png)

Penjelasan:
Kode pada gambar menunjukkan proses pemuatan dataset hasil preprocessing menggunakan pandas. File preprocessed_dataset.csv dibaca ke dalam DataFrame dengan pd.read_csv(), lalu df.head() menampilkan lima baris pertama untuk memastikan datanya sudah benar. Dari output terlihat bahwa data telah melalui tahap normalisasi pada fitur numerik dan one-hot encoding pada fitur kategorikal, sehingga muncul kolom seperti Gender_Male, Satisfaction_Low, dan Satisfaction_Medium. Tampilan ini memastikan bahwa hasil preprocessing dan feature engineering sudah berhasil diterapkan dan siap digunakan untuk analisis atau pemodelan berikutnya.

![Step 3](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T3.png)

Penjelasan:
df.info() menunjukkan ringkasan struktur dataset setelah preprocessing. Dataset terdiri dari 200 baris dan 6 kolom, tanpa nilai yang hilang (semua kolom memiliki 200 nonnull). Tiga kolom numerik—Age, Income, Balance—bertipe float64, menandakan bahwa ketiganya sudah melalui proses normalisasi atau standardisasi. Sementara tiga kolom lainnya— Gender_Male, Satisfaction_Low, Satisfaction_Medium—bertipe bool, hasil dari one-hot encoding pada fitur kategorikal. Informasi ini menegaskan bahwa dataset sudah bersih, terstruktur, dan siap digunakan untuk analisis lanjutan atau pemodelan machine learning.

![Step 4](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T4.png)

Penjelasan:
df.describe() menampilkan ringkasan statistik untuk tiga fitur numerik: Age, Income, dan Balance. Nilai mean yang mendekati nol serta standar deviasi sekitar satu menunjukkan bahwa ketiga fitur tersebut telah melalui proses standardisasi sehingga berada pada skala yang sama. Rentang nilai minimum dan maksimum juga konsisten dengan hasil transformasi z-score, yaitu berada di sekitar -2 hingga 2. Selain itu, nilai kuartil (25%, 50%, 75%) menunjukkan distribusi data yang sudah teratur dan tidak memiliki anomali besar. Secara keseluruhan, statistik ini mengonfirmasi bahwa proses normalisasi atau standardisasi telah diterapkan dengan benar dan dataset siap digunakan untuk tahap pemodelan.

![Step 5](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T5.png)

Penjelasan:
df["Age"].hist() digunakan untuk menampilkan histogram dari kolom Age pada DataFrame. Grafik yang dihasilkan menunjukkan distribusi nilai usia yang telah distandarisasi, terlihat dari rentang nilai yang berada di sekitar -1.5 hingga 1.5. Histogram ini memperlihatkan bagaimana frekuensi nilai usia tersebar pada berbagai interval, di mana sebagian besar data berada di sekitar nilai 0 yang mewakili nilai rata-rata setelah proses standardisasi. Area dengan nilai ekstrem terlihat memiliki frekuensi yang lebih rendah, sehingga grafik ini membantu memberikan gambaran mengenai pola penyebaran data usia dalam bentuk visual yang mudah dipahami. 

![Step 6](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T6.png) 

Penjelasan:
Kode pada gambar menggunakan matplotlib.pyplot untuk menampilkan boxplot dari kolom Income pada DataFrame. Baris plt.boxplot(df["Income"]) menghasilkan grafik boxplot yang menggambarkan penyebaran data Income, sementara plt.title("Boxplot Income") memberi judul pada grafik, dan plt.show() menampilkannya. Output berupa boxplot menunjukkan nilai tengah (median), rentang kuartil (Q1–Q3), serta batas bawah dan atas data. Karena nilai Income tampak berada pada rentang sekitar -2 hingga 2, dapat disimpulkan bahwa data telah distandarisasi. Boxplot ini membantu melihat persebaran data, mendeteksi pencilan, serta mengetahui apakah distribusi Income cenderung simetris atau miring.

![Step 7](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/T7.png)
![Lanjutan Step 7](https://github.com/Ramadhinianjani/preprocessing_feature_engineering/blob/main/Screenshot/OU7.png)

Penjelasan:
Kode tersebut digunakan untuk menampilkan heatmap korelasi pada dataset. Baris plt.figure(figsize=(8,5)) mengatur ukuran gambar, sementara sns.heatmap(df.corr(), annot=True, cmap="coolwarm") menghasilkan heatmap berdasarkan nilai korelasi antar variabel numerik dalam DataFrame. Parameter annot=True membuat setiap sel menampilkan angka korelasinya, dan cmap="coolwarm" memberi warna gradasi dari merah (korelasi tinggi) hingga biru (korelasi negatif). Output grafik menunjukkan hubungan antar variabel, misalnya Age memiliki korelasi negatif kecil dengan Satisfaction_Low, dan variabel Satisfaction_Low serta Satisfaction_Medium memiliki korelasi negatif kuat sekitar -0.46. Heatmap ini memudahkan untuk melihat pola hubungan antar fitur secara visual dan cepat.
