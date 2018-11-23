@call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
node-pre-gyp build --runtime=electron --target=1.7.5 --target_arch=x64 --target_platform=win32
