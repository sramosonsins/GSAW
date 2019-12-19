
DIR=/PATH-TO-GSAW/GSAW

mkdir $DIR/bin

cd $DIR/bin

## Download the required packages/softwares

git clone https://github.com/CRAGENOMICA/mstatspop.git
git clone https://github.com/CRAGENOMICA/fastaconvtr.git
git clone https://github.com/CRAGENOMICA/weight4tfa.git
git clone https://github.com/CRAGENOMICA/gVCF2tFasta.git
git clone https://github.com/CRAGENOMICA/indexingtFasta.git
git clone https://github.com/CRAGENOMICA/concatenate_tFasta.git
git clone https://github.com/CRAGENOMICA/mergetFasta.git

## Compile the previous programs

cd mstatspop
sh compile_mstatspop.sh

cd ../fastaconvtr
sh compile_fastaconvtr.sh

cd ../weight4tfa
sh compile_weight4tfa.sh

cd ../gVCF2tFasta
sh compile_gVCF2tFasta.sh

cd ../indexingtFasta
sh compile_indexingtFasta.sh

cd ../mergetFasta
sh compile_mergetFasta.sh

## Execute GSAW

cd $DIR

./dist/GSAW
