## In order to run the analysis with GSAW, the user have to create a "bin" directory in the main directory of GSAW, and download there the different internal softwares from the package from GitHub.

mkdir bin
cd bin

git clone https://github.com/CRAGENOMICA/mstatspop.git
git clone https://github.com/CRAGENOMICA/fastaconvtr.git
git clone https://github.com/CRAGENOMICA/weight4tfa.git
git clone https://github.com/CRAGENOMICA/gVCF2tFasta.git
git clone https://github.com/CRAGENOMICA/indexingtFasta.git
git clone https://github.com/CRAGENOMICA/concatenate\_tFasta.git
git clone https://github.com/CRAGENOMICA/mergetFasta.git

## Once all applications have been downloaded, each one must be compiled separately.

cd mstatspop
sh compile\_mstatspop.sh

cd ../fastaconvtr
sh compile\_fastaconvtr.sh

cd ../weight4tfa
sh compile\_weight4tfa.sh

cd ../gVCF2tFasta
sh compile\_gVCF2tFasta.sh

cd ../indexingtFasta
sh compile\_indexingtFasta.sh

cd ../mergetFasta
sh compile\_mergetFasta.sh

Finally, when all the softwares are compiled, the user can execute GSAW from the "dist" directory:

./dist/GSAW
