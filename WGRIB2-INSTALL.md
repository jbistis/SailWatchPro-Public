# SailWatchPro: wgrib2 Static Library Build & Integration Guide

**Maintainer Note:**  
This document describes the step-by-step process to build, update, and integrate the wgrib2 C static libraries (for both iOS device/arm64 and Simulator/x86_64) for use in SailWatchPro.

---

## Prerequisites

- Xcode 16.x (WWDC 2024, iOS 18.5/SDK 26.0)
```
brew install jasper libpng zlib libaec
git clone https://github.com/NOAA-EMC/wgrib2.git
cd wgrib2
mkdir build && cd build
cmake .. -DMAKE_C_API=ON
make -j
sudo make install

```
- Homebrew and CMake:
  ```
  brew install cmake
  ```
  ```
  cd /Users/jamesbistis/dev/SailWatchPro/
  ```
  ```
  git clone https://github.com/NOAA-EMC/NCEPLIBS-wgrib2.git wgrib2
  ```

---

## Step 1: Clean Previous Builds
```
cd /Users/jamesbistis/dev/SailWatchPro/ios-build
```
```
rm -rf build build-simulator install install-simulator universal
```

---

## Step 2: Build for Device (**arm64**)
```
cmake -S ../wgrib2 -B build -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_OSX_SYSROOT=$(xcrun --sdk iphoneos --show-sdk-path) -DCMAKE_INSTALL_PREFIX=install -DCMAKE_BUILD_TYPE=Release -DBUILD_LIB=ON -DBUILD_SHARED_LIB=OFF -DBUILD_WGRIB=OFF -DBUILD_EXTRA=OFF -DBUILD_TESTING=OFF -DENABLE_DOCS=OFF -DUSE_NETCDF=OFF -DUSE_REGEX=ON -DUSE_TIGGE=OFF -DUSE_MYSQL=OFF -DUSE_IPOLATES=OFF -DUSE_UDF=OFF -DUSE_OPENMP=OFF -DUSE_PROJ4=OFF -DUSE_WMO_VALIDATION=OFF -DUSE_G2CLIB_HIGH=OFF -DUSE_G2CLIB_LOW=OFF -DUSE_AEC=OFF -DMAKE_FTN_API=OFF -DDISABLE_TIMEZONE=ON -DDISABLE_ALARM=ON -DDISABLE_STAT=ON
```
```
cmake --build build -- -j$(sysctl -n hw.ncpu || echo 4)
```

---

## Step 3: Build for Simulator (**x86_64**)

Get your actual simulator SDK version first:

ls /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/
# Should show iPhoneSimulator26.0.sdk or similar

Then build with the SDK path for your version:

mkdir -p build-simulator
cmake -S ../wgrib2 -B build-simulator \
  -DCMAKE_SYSTEM_NAME=iOS \
  -DCMAKE_OSX_ARCHITECTURES=x86_64 \
  -DCMAKE_OSX_SYSROOT=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator26.0.sdk \
  -DCMAKE_INSTALL_PREFIX=install-simulator \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_LIB=ON \
  -DBUILD_SHARED_LIB=OFF \
  -DBUILD_WGRIB=OFF \
  -DBUILD_EXTRA=OFF \
  -DBUILD_TESTING=OFF \
  -DENABLE_DOCS=OFF \
  -DUSE_NETCDF=OFF \
  -DUSE_REGEX=ON \
  -DUSE_TIGGE=OFF \
  -DUSE_MYSQL=OFF \
  -DUSE_IPOLATES=OFF \
  -DUSE_UDF=OFF \
  -DUSE_OPENMP=OFF \
  -DUSE_PROJ4=OFF \
  -DUSE_WMO_VALIDATION=OFF \
  -DUSE_G2CLIB_HIGH=OFF \
  -DUSE_G2CLIB_LOW=OFF \
  -DUSE_AEC=OFF \
  -DMAKE_FTN_API=OFF \
  -DDISABLE_TIMEZONE=ON \
  -DDISABLE_ALARM=ON \
  -DDISABLE_STAT=ON
cmake --build build-simulator --target install -- -j$(sysctl -n hw.ncpu || echo 4)

---

## Step 4: Create Universal (Fat) Static Libraries

mkdir -p universal
lipo -create \
  install/lib/libwgrib2.a \
  install-simulator/lib/libwgrib2.a \
  -output universal/libwgrib2.a
lipo -create \
  install/lib/libwgrib2_c_api.a \
  install-simulator/lib/libwgrib2_c_api.a \
  -output universal/libwgrib2_c_api.a

---

## Step 5: Copy to SailWatchPro Xcode Project

cp universal/libwgrib2.a ../SailWatchPro/Libraries/
cp universal/libwgrib2_c_api.a ../SailWatchPro/Libraries/
cp -r install/include ../SailWatchPro/Libraries/

---

## Step 6: Finalize Xcode Integration

- Add both `libwgrib2.a` and `libwgrib2_c_api.a` to your Xcode project’s “Link Binary With Libraries.”
- Header search path:
  $(PROJECT_DIR)/SailWatchPro/Libraries/include
  (non-recursive)
- Bridging header path:
  SailWatchPro/SailWatchPro-Bridging-Header.h
- Clean and build: **There should be zero SDK version warnings** (as of Xcode 16 and iOS 18.5/SDK 26.0).

---

## Notes

- **To update wgrib2:**  
  Pull a new version from GitHub and repeat these steps.
- **To support new iOS/Xcode versions:**  
  Repeat the “simulator build” step with the new SDK path.
- **Troubleshooting:**  
  - If you see architecture or deployment target mismatches, double-check `-DCMAKE_OSX_SYSROOT` and Xcode’s selected SDK.
  - Clean builds (`rm -rf build-* install-* universal`) solve most integration issues.
- **These libraries support both device and simulator, arm64 and x86_64.**

---

_Short link: [this file is WGRIB2-INSTALL.md in your repo root]_

---
