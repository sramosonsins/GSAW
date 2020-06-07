
DIR=/PATH-TO-GSAW/GSAW

mkdir $DIR/bin

cd $DIR/bin

if [ "$(uname)" == "Darwin" ]; then
    function _wget() { curl "${1}" -o $(basename "${1}") ; };
    alias wget='_wget'
fi

#zlib 1.2.11 installation (dependency)
mkdir -p ./zlib
wget http://zlib.net/zlib-1.2.11.tar.gz -P ./zlib
tar -zxvf ./zlib/zlib-1.2.11.tar.gz -C ./zlib
rm ./zlib/zlib-1.2.11.tar.gz
cd ./zlib/zlib-1.2.11
./configure
make
sudo make install

#gsl installation (dependency)
mkdir -p /tmp/gsl
curl -o /tmp/gsl-2.2.tar.gz ftp://ftp.gnu.org/gnu/gsl/gsl-2.2.tar.gz -LOk
tar -zxvf /tmp/gsl-2.2.tar.gz -C /tmp/gsl && \
rm /tmp/gsl-2.2.tar.gz && \
cd /tmp/gsl/gsl-2.2 && \
./configure && \
make && \
sudo make install

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
