# Laporan Proyek Machine Learning - Deaka Ahmad Naufal
## Domain Proyek
Pendidikan merupakan fondasi krusial dalam membentuk sumber daya manusia berkualitas dan daya saing bangsa. Buruknya prestasi siswa dalam organisasi pendidikan merupakan masalah sosial yang signifikan, yang menyebabkan siswa putus sekolah, dan ternyata penting bagi lembaga pendidikan dan akademisi untuk lebih memahami alasan di balik banyaknya kegagalan dalam komunitas siswa. Ini bukan kasus sederhana, karena banyak faktor atau atribut yang harus dinilai yang memengaruhi kinerja siswa[1].

Kasus ketidaklulusan siswa berkorelasi dengan kebiasaan belajar yang tidak terpantau, seperti ketidakhadiran ke sekolah, kurangnya waktu belajar mandiri, dan ketidakteraturan mengerjakan tugas. Sayangnya, sistem pemantauan konvensional masih bersifat _reaktif_, di mana intervensi baru dilakukan setelah hasil ujian keluar. Oleh karena itu, diperlukan Predictive analysis untuk mengidentifikasi pola kebiasaan siswa dan bagaimana hasilnya pada kelulusan agar dapat menjadi langkah prepetif untuk memaksimalkan performa siswa

- Referensi terkait riset sebelumnya
	A. Rahman, “Klasifikasi Performa Akademik Siswa Menggunakan Metode Decision Tree dan Naive Bayes,” _saintekom_, vol. 13, no. 1, hlm. 22–31, Mar 2023, doi: [10.33020/saintekom.v13i1.349](https://doi.org/10.33020/saintekom.v13i1.349).

## Business Understanding

### Problem Statements

Berdasarkan latar belakabg yang telah disampaikan sebelumnya, pernytaan masalah yang akan diselesaikan pada proyek ini adalah:
- Kebiasaan (habbit) apa yang paling berpengaruh terhadap kelulusan siswa?
- Apa model terbaik yang bisa memprediksi kelulusan siswa berdasarkan kebiasaannya?

### Goals

Berdasarkan Problem Statement tersebut tujuan yang harus dicapai adalah:
-  Mengidentifikasi faktor dominan yang memengaruhi kelulusan.
-  Membangun model terbaikuntuk prediksi kelulusan siswa yang memiliki akurasi tertinggi.
### Solution statements
- Melakukan proses EDA untuk menemukan fitur yang paling mempengaruhi kelulusan siswa.
- Membangun 4 model Machine Learning yaitu Logistic Regression, Decission Tree,Random Forest, dan Extreme Gradient Boosting
- Menerapkan Feature selection dan crossvalidation untuk meningkatkan performa model dan menghindari overfitting
- Menggukur performa model menggunakan f1 score, precission, recall, dan confussion matrix, untuk memilih model terbaik berdasarkan akurasi tertinggi.

## Data Understanding
Dataset yang digunakan berasal dari kaggle yang dapat diakses pada [Kaggle](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance/data). Dengan 1.000 catatan siswa sintetis dan 15+ fitur termasuk jam belajar, pola tidur, penggunaan media sosial, kualitas diet, kesehatan mental, dan nilai ujian akhir. Dibuat menggunakan pola realistis untuk praktik pendidikan.

### Variabel-variabel pada Student Habits vs Performance dataset


| Kolom                           | Deskripsi                            |
| ------------------------------- | ------------------------------------ |
| `student_id`                    | ID unik siswa (tidak untuk analisis) |
| `age`                           | Usia siswa (17-24 tahun)             |
| `gender`                        | Male/Female/Other                    |
| `study_hours_per_day`           | Rata-rata jam belajar harian         |
| `social_media_hours`            | Waktu harian di media sosial         |
| `netflix_hours`                 | Waktu menonton Netflix               |
| `part_time_job`                 | Yes/No                               |
| `attendance_percentage`         | Persentase kehadiran kelas (0-100%)  |
| `sleep_hours`                   | Rata-rata jam tidur harian           |
| `diet_quality`                  | Poor/Fair/Good                       |
| `exercise_frequency`            | Frekuensi olahraga per minggu (0-7)  |
| `parental_education_level`      | jejang edukasi orang tua             |
| `internet_quality`              | Poor/Average/Good/Excellent          |
| `mental_health_rating`          | Skala 1-10                           |
| `extracurricular_participation` | Yes/No                               |
| `exam_score`                    | Nilai ujian akhir (0-100)            |


**EDA**:
1. Mengecek informasi pada dataset menggunakan `.info()`
	
 	<img src="https://github.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/blob/9e5bb54d37d0690762fe977c2d986200af71f419/images/Pasted%20image%2020250424195500.png">
	
 	Dari gambar diatas dapat kita lihat ada missing value pada kolom `parental_education_level`
2. Mengecek missing value dan duplicate value
	Dalam dataset ini terdapat missing value pada kolom `parental_education_level` sebanyak 91. Missing value tersebut kita isi dengan nilai modusnya( Nilai yang paling sering muncul). Sedangkan untuk duplicated data tidak ada .
3. Mengecek deskripsi statistik menggunakan`.describe()`
 	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424200512.png">
Saat kita lihat statistik tidak terdapat nilai berupa outlier atau nilai yang salah
4. Boxplot dan distribusi setiap variabel numerik
	- Age
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424200916.png">
 
	- study hours perday
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424200944.png">
 
	- attendance percentage
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201004.png">
 
	- sleephours
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201052.png">
 
	- exercise frequency
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201112.png">
 

	- mental health rating
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201131.png">

	- exam score
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201144.png">

	- screen time(Jumlah social media hours dan netflix hours)
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201200.png">
 

	Seluruh variabel memiliki nilai yang cukup normal walaupun beberapa terdapat outlier akan tetapi nilai tersebut masih berada didalam rentang yang seharusnya
5. Categorical Feature 
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424201503.png">
 
## Data Preparation
- Map Exam Score
  
	Memetakan kolom Exam Score menjadi "Pass" dan "Faill" untuk  dijadikan targer klasifikasi dimana exam_score >= 70 adalah "Pass"
- Encoding Feature Kategorikal
  
	fitur kategori yang bertipe object di rubah menjadi numerik agar model mengenali data kategorikal
- Feature Selection
  
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424231629.png">
 
	Kolom study_hours_per_day,mental_health_rating, screen_time dipilih karena memiliki nilai korelasi yang paling tinggi baik itu positif atau negatif. itu artinya Fitur inilah yang paling berpengaruh pada kelulusan
- Split dataset
  
	Membagi dataset menjadi train dan test dengan rasio 80 : 20 dilakukan guna melakukan tahap training pada model menggunakan data train, lalu melakukan tahap evaluasi menggunakan data test
- Standarisasi
  
	Melakukan Standarisasi menggunakan standar scaller agar algoritma tidak terpengaruh oleh perbedaan skala antar fitur

## Modeling

1. logistic Regression
   
**Kelebihan**:
   
- Efisien untuk dataset kecil (sederhana dan mudah dilatih
-  Interpretasi koefisien mudah untuk analisis pengaruh fitur

**Kekurangan**:

- Hanya menangkap hubungan linear
-  Sensitif terhadap outlier
    




2. **Decision Tree **
	Algoritma berbasis pohon keputusan dengan pembagian rekursif.
	
 Parameter:
 
- max_depth=7,          # Batasi kedalaman maksimum pohon
- min_samples_split=15, # Minimal 15 sampel untuk split node
- random_state=42       # Reproduksibilitas struktur
	
 **Kelebihan**:
 
-  Menangkap hubungan non-linear
-  Tidak membutuhkan feature scaling
-  Visualisasi intuitif
	
 **Kekurangan**:
- Rentan overfitting jika depth tidak diatur
-  Sensitif terhadap perubahan kecil data
	    


 
3. **Random Forest**
Metode ensemble berbasis pohon keputusan yang menggabungkan banyak pohon untuk meningkatkan akurasi dan mengurangi overfitting
	
Parameter:

- n_estimators=200,     # Jumlah pohon besar untuk stabilitas
- max_depth=12,         # Kedalaman fleksibel dengan kontrol
- min_samples_leaf=5,   # Minimal 5 sampel di leaf node
- random_state=42       
	
 **Kelebihan**:
 
- Robust terhadap noise dan outlier
- Fitur importance otomatis    
-  Reduksi varians dibanding single tree
	
 **Kekurangan**:
 
- Waktu training lebih lama
-  Kompleksitas interpretasi manual
	 	
4. **XGBoost**
	Algoritma gradient boosting yang optimalkan model bertahap.
	
 Parameter:
 
- learning_rate=0.05,   # Langkah pembelajaran presisi tinggi
- max_depth=4,          # Kedalaman terkontrol
-  n_estimators=300,     # Kompensasi learning rate kecil
- random_state=42       
	
 **Kelebihan**:
 
-  Akurasi tinggi untuk data kompleks
- Regularisasi bawaan (max_depth)
-  Handle missing value otomatis
	
 **Kekurangan**:
 
-  Waktu training panjang
-  Sensitif terhadap hyperparameter

  
**Pemilihan model terbaik**
Berdasarkan Hasil Evaluasi pada data test Model terbaik adalah Logistic Regression
	
## Evaluation

1. Confussion Matrix
	**_Confusion matrix_** adalah alat untuk mengevaluasi kinerja model klasifikasi dengan menunjukkan jumlah prediksi yang benar dan salah dalam format tabel. Ini memberikan pandangan yang lebih rinci tentang cara model berperforma di berbagai kelas.
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230256.png">
 
2. Akurasi
	**Akurasi** adalah metrik yang paling sederhana dan sering digunakan untuk mengukur kinerja model klasifikasi. Akurasi dihitung sebagai proporsi dari prediksi benar (baik positif maupun negatif) terhadap seluruh prediksi yang dilakukan oleh model.
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230111.png">
 
3. F1 Score
	**F1-Score** adalah metrik yang menggabungkan presisi dan recall menjadi satu nilai tunggal yang mempertimbangkan keduanya. F1-Score adalah rata-rata harmonis dari presisi dan recall, memberikan gambaran yang lebih baik ketika ada _trade-off_ antara keduanya.
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230454.png">
 
4. Precission
	**_Precision_** mengukur seberapa baik model menghindari positif palsu (false positives, FP). Ini adalah rasio prediksi positif yang benar terhadap semua prediksi positif yang dibuat oleh model
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230429.png">
 
5. Recall
	**_Recall_** atau **sensitivitas** adalah metrik yang mengukur seberapa baik model dapat menangkap semua contoh positif. Ini adalah rasio prediksi positif yang benar terhadap semua kasus positif yang sebenarnya ada dalam data.
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230144.png">
 
6. Cross-Validation
	Teknik ini membagi data menjadi beberapa subset yang dikenal sebagai **_fold_**. Model dilatih dalam beberapa subset serta diuji pada subset yang tersisa dan proses ini diulang beberapa kali. Jika performa model sangat bervariasi antara **_fold_**, ini menunjukkan bahwa model mengalami overfitting pada subset data tertentu dan tidak dapat menggeneralisasi dengan baik. _Cross-validation_ membantu memastikan bahwa model dinilai secara lebih konsisten di seluruh data.
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230539.png">
 

### Hasil Evaluasi

<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424231028.png">

- Logistic Regression
  
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230654.png">

- Decission Tree
  
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230818.png">
 
- Random Forest
  
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230835.png">
 
- XGBoost
  
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424230842.png">
 

- Perbandingan Akurasi serta crosvall setiap Model
	
	<img src="https://raw.githubusercontent.com/dk1781/PredictiveAnalysis_StudentHabitsvsPerformance/refs/heads/main/images/Pasted%20image%2020250424231128.png">
- Berdasarkan gambar diatas model Logistic regression dan random forest mendapatkan nilai akurasi yang paling tinggi yaitu 83% akan tetapi untuk Cross validationnya model Logistic Regression mengungguli model Random Forest yaitu 83% dibandingkan 78%. Maka didapat model Logistic Regression model terbaik untuk klasifikasi student habits vs performance ini.

### Kesimpulan
- Kebiasaan siswa yang paling berpengaruh terhadap kelulusan adalah study_hours_per_day (rata rata lama belajar siswa perhari ,mental_health_rating (kesehatan mental siswa), screen_time("rata rata lama siswa membuka social media ataupun menonton netflix perhari)
- Model terbaik yang mampu meprediksi kelulusan siswa berdasarrkan kebiasaanya adalah Model Logistic Regression



## REFERENSI
[1]Ashfaq, U., M, B. P., & Mafas, R. (2020). Managing Student Performance: A Predictive Analytics using Imbalanced Data. _International Journal of Recent Technology and Engineering (IJRTE)_, _8_(6), 2277–2283. https://doi.org/10.35940/ijrte.e7008.038620

[2]A. Rahman, “Klasifikasi Performa Akademik Siswa Menggunakan Metode Decision Tree dan Naive Bayes,” _saintekom_, vol. 13, no. 1, hlm. 22–31, Mar 2023, doi: [10.33020/saintekom.v13i1.349](https://doi.org/10.33020/saintekom.v13i1.349).

[3]Dicoding. Diakses pada 23 April 2025 dari https://www.dicoding.com/academies/184/tutorials/38763
