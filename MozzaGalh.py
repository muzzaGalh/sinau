#!/bin/bash
#version 1.0

# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
clear
echo -e  "===================================== $white" |lolcat
echo -e  "=  Tools    : D3FICE||PAND4         = $white" |lolcat
echo -e  "=  Creadby  : MuzzaGalh             = $white" |lolcat
echo -e  "=  Contact  : MuzzaGalh46@gmail.com = $white" |lolcat
echo -e  "===================================== $white" |lolcat






echo -e  "silahkan pilih menu yang diinginkan! $white  "|lolcat
echo -e "Belajar itu penting untuk masa depan :) $white "|lolcat

###################################################                     # CTRL + C
###################################################                     trap ctrl_c INT
ctrl_c() {                                                              clear

                                                                        



echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit
... "
echo -e $cyan"[#]> Thanks"
sleep 1                                                                 echo ""
echo -e $white"[#]> see you Gaess :)..."
sleep 1
exit
}

lagi=1
while [ $lagi -lt 5 ];
do
echo ""
echo -e $m "1.  sumpah pemuda${endc}";
echo -e "============================ $white" |lolcat
echo -e $r "2.  pancasila${endc}";
echo -e "============================ $white" |lolcat
echo -e $g "3.  UUD 1945${endc}";
echo -e "============================ $white" |lolcat
echo -e $c "4   Dasadarma pramuka${endc}";
echo -e "============================ $white" |lolcat

echo -e $r "5. Exit${endc}";
echo ""
echo -e "╭─Silahkan pilih" |lolcat
read -p "╰─#" pil;

case $pil in
# sumpah pemuda

1) echo -e "Pertama:
Kami poetra dan poetri Indonesia, mengakoe bertoempah
darah jang satoe, tanah Indonesia.
Kedoea:
Kami poetra dan poetri Indonesia mengakoe berbangsa jang
satoe, bangsa Indonesia.
Ketiga:
Kami poetra dan poetri Indonesia mendjoendjoeng bahasa
persatoean, bahasa Indonesia..." |lolcat
;;

#pancasila

2) echo -e "PANCASILA

1.   Ketuhanan Yang Maha Esa.
2.   Kemanusiaan Yang Adil Dan Beradab.
3.   Persatuan Indonesia.
4.   Kerakyatan Yang Dipimpin Oleh Hikmat Kebijaksanaan Dalam
     Permusyawaratan/Perwakilan.
5.   Keadilan Sosial Bagi Seluruh Rakyat Indonesia..." |lolcat

;;

#UUD 1945

3) echo -e "UNDANG-UNDANG DASAR NEGARA REPUBLIK INDONESIA
TAHUN 1945
PEMBUKAAN
(Preambule)

 Bahwa sesungguhnya Kemerdekaan itu ialah hak segala
bangsa dan oleh sebab itu, maka penjajahan di
atas dunia harus dihapuskan, karena tidak sesuai dengan
peri-kemanusiaan dan peri-keadilan.
 Dan perjuangan pergerakan kemerdekaan Indonesia telah
sampailah kepada saat yang berbahagia
dengan selamat sentausa mengantarkan rakyat Indonesia ke
depan pintu gerbang kemerdekaan Negara
Indonesia, yang merdeka, bersatu, berdaulat, adil dan
makmur.
 Atas berkat rakhmat Allah Yang Maha Kuasa dan dengan
didorongkan oleh keinginan luhur, supaya
berkehidupan kebangsaan yang bebas, maka rakyat Indonesia
menyatakan dengan ini kemerdekaannya.
 Kemudian daripada itu untuk membentuk suatu Pemerintah
Negara Indonesia yang melindungi segenap
bangsa Indonesia dan seluruh tumpah darah Indonesia dan
untuk memajukan kesejahteraan umum,
mencerdaskan kehidupan bangsa, dan ikut melaksanakan
ketertiban dunia yang berdasarkan kemerdekaan,
perdamaian abadi dan keadilan sosial, maka disusunlah
Kemerdekaan Kebangsaan Indonesia itu dalam
suatu Undang Undang Dasar Negara Indonesia, yang terbentuk dalam suatu susunan Negara Republik
Indonesia yang berkedaulatan rakyat dengan berdasarkan
kepada Ketuhanan Yang Maha Esa,
Kemanusiaan yang adil dan beradab, Persatuan Indonesia
dan Kerakyatan yang dipimpin oleh hikmat
kebijaksanaan dalam Permusyawatan/Perwakilan, serta
dengan mewujudkan suatu Keadilan Sosial bagi
seluruh rakyat Indonesia..." |lolcat

;;

#Dasadarma pramuka

4) echo -e "
1.  Taqwa kepada Tuhan Yang Maha Esa.
2.  Cinta alam dan kasih sayang sesama manusia.
3.  Patriot yang sopan dan kesatria.
4.  Patuh dan suka bermusyawarah.
5.  Rela menolong dan tabah.
6.  Rajin, trampil dan gembira.
7.  Hemat, cermat dan bersahaja.
8.  Disiplin, berani dan setia.
9.  Bertanggung jawab dan dapat dipercaya.
10. Suci dalam pikiran perkataan dan perbuatan..." |lolcat

;;


6) echo "created by : MuzzaGalh" | lolcat
exit
;;

*) echo "sorry, pilihan yang anda cari tidak ada"
esac
done
done