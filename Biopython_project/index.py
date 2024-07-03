from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
import os

# Dosya isimleri listesi
fasta_files = ["neandertal1.fasta", "neandertal2.fasta", "neandertal3.fasta","neandertal4.fasta",
               "neandertal5.fasta","human.fasta", "denisovan.fasta", "chimpanzee.fasta",
               "orangutan.fasta","macaque.fasta","goril.fasta","baboon.fasta","bonobo.fasta"]

# Çıktı dosyasının adı
output_file = "combined.fasta"

# Birleştirilmiş sekansları yazmak için boş bir liste oluşturun
combined_sequences = []

# Her bir FASTA dosyasını okuyup sekansları listeye ekleyin
for fasta_file in fasta_files:
    if not os.path.exists(fasta_file):
        print(f"{fasta_file} bulunamadı.")
        continue
    print(f"{fasta_file} bulundu, işleniyor...")
    with open(fasta_file, "r") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
        if not records:
            print(f"{fasta_file} dosyasında işlenecek sekans bulunamadı.")
        for record in records:
            combined_sequences.append(record)
            print(f"{record.id} sekansı {fasta_file} dosyasından eklendi.")

# Birleştirilmiş sekansları tek bir FASTA dosyasına yazın
with open(output_file, "w") as output_handle:
    SeqIO.write(combined_sequences, output_handle, "fasta")

print(f"{output_file} dosyasına {len(combined_sequences)} sekans birleştirildi.")

# ClustalW kullanarak sekansları hizalama
clustalw_exe = "C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe"  # ClustalW'nin tam yolu
in_file = "combined.fasta"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=in_file)
stdout, stderr = clustalw_cline()
print("Sekanslar hizalandı.")

# Filogenetik ağaç oluşturma ve görüntüleme
tree = Phylo.read("combined.dnd", "newick")

# Filogenetik ağacı çizme
Phylo.draw(tree)
import matplotlib.pyplot as plt

# Filogenetik ağacı çizme ve görüntüleme
fig = plt.figure(figsize=(10, 5), dpi=100)  # Görüntü boyutunu ve çözünürlüğünü ayarlayın
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, do_show=False, axes=axes)  # Filogenetik ağacı çizme
plt.show()  # Grafiği gösterme
