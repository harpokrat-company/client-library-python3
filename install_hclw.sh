git clone git@gitlab.com:harpokrat/hcl/hcl-core.git
cd hcl-core
cmake .
make
sudo cp libhcl.so /usr/lib/libhcl.so.0
sudo ldconfig
cd ..
rm -rf hcl-core

git clone git@gitlab.com:harpokrat/hcl/hclw-python3.git
pip3 install hclw-python3/
rm -rf hclw-python3