# axonize-python-sdk


## For windows environment

requirements:
1. python 2.7
2. python package manager - pip


installation:
1. clone the SDK
2. install the dependencies 
  ```sh
  pip install -r requirements.txt
  ```
3. change the config
4. view the example fake event creation in app.py file.




## For Linux environment

Because the Azure IoT SDKs for Python are wrappers on top of the SDKs for C, you will need to compile the C libraries if you want or need to generate the Python libraries from source code. You will notice that the C SDKs are brought in as submodules to the current repository. In order to setup your development environment to build the C binaries make sure all dependencies are installed before building the SDK.

1. Install build packages
```bash
sudo apt-get update
sudo apt-get install -y git cmake build-essential curl libcurl4-openssl-dev libssl-dev uuid-dev
```

2. Verify that CMake is at least version **2.8.12**:
```
cmake --version
```

3. Verify that gcc is at least version **4.4.7**:
```
gcc --version
```

4. Ensure that the desired Python version (2.7.x) is installed and active.
```
python --version
```

5. Clone Microsoft repo
```
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git
```

6. Navigate to the folder **build_all/linux**

7. Run the `./setup.sh` script to install the prerequisite packages and the dependent libraries.

8. Run the `./build.sh` script.

9. After a successful build, the `iothub_client.so` Python extension module is copied to the [**device/samples**] folder. Copy the module to the Axonize SDK folder.

10. Run the test app in the SDK folder.
```bash
python app.py
```



###Known build issues: 

1.) On building the Python client library (`iothub_client.so`) on Linux devices that have less than **1GB** RAM, you may see build getting **stuck** at **98%** while building `iothub_client_python.cpp` as shown below

``[ 98%] Building CXX object python/src/CMakeFiles/iothub_client_python.dir/iothub_client_python.cpp.o``

If you run into this issue, check the **memory consumption** of the device using `free -m command` in another terminal window during that time. If you are running out of memory while compiling iothub_client_python.cpp file, you may have to temporarily increase the **swap space** to get more available memory to successfully build the Python client side device SDK library.