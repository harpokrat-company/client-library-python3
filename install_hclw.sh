git clone git@github.com:harpokrat-company/hcl.git
cd hcl
git checkout v0.0.1
cmake .
make
sudo cp libhcl.so /usr/lib/libhcl.so.0
sudo ldconfig
cd ..
rm -rf hcl

git clone git@github.com:harpokrat-company/hclw-python3.git
git checkout v0.0.1
python3 -m pip install hclw-python3/
rm -rf hclw-python3
