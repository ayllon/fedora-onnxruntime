%global onnx_version 1.10.1
%global safeint_version 3.0.26
%global optional_lite_version 3.5.0

Summary:    A cross-platform inferencing and training accelerator
Name:       onnxruntime
Version:    1.9.1
Release:    1%{?dist}
License:    MIT and ASL 2.0
URL:        https://github.com/microsoft/onnxruntime
Source0:    https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    https://github.com/onnx/onnx/archive/v%{onnx_version}/onnx-%{onnx_version}.tar.gz
# Header-only libraries
Source2:    https://github.com/dcleblanc/SafeInt/archive/%{safeint_version}/SafeInt-%{safeint_version}.tar.gz
Source3:    https://github.com/martinmoene/optional-lite/archive/v%{optional_lite_version}/optional-lite-%{optional_lite_version}.tar.gz
# Patch the CMakeLists.txt to use local libraries
Patch0:     CMakeLists.patch
# Use pthreads instead of nsync
Patch1:     drop_nsync.patch

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  bzip2
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  boost-devel >= 1.66
BuildRequires:  date-devel
Buildrequires:  eigen3-devel >= 1.34
BuildRequires:  flatbuffers-devel
BuildRequires:  json-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  re2-devel

%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%prep
%autosetup -p0
tar xf "%{SOURCE1}" -C cmake/external/onnx --strip-components 1
tar xf "%{SOURCE2}" -C cmake/external/SafeInt/safeint --strip-components 1
tar xf "%{SOURCE3}" -C cmake/external/optional-lite --strip-components 1

%build
mkdir -p "%{_vpath_builddir}"
cd "%{_vpath_builddir}"
cmake -Donnxruntime_BUILD_SHARED_LIB=ON \
    -Donnxruntime_EXTENDED_MINIMAL_BUILD=ON \
    -DADD_DEBUG_INFO_TO_MINIMAL_BUILD=ON \
    -Donnxruntime_DEV_MODE=OFF \
    -Donnxruntime_PREFER_SYSTEM_LIB=ON \
    -Donnxruntime_BUILD_UNIT_TESTS=OFF \
    -Donnxruntime_BUILD_BENCHMARKS=OFF \
    -Donnxruntime_USE_PREINSTALLED_EIGEN=ON \
    -Deigen_SOURCE_PATH=/usr/include/eigen3 \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    ../cmake
%make_build

%install
%make_install -C "%{_vpath_builddir}"

%files
%license LICENSE
%doc docs/*
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.*

%files devel
%dir %{_includedir}/onnxruntime/
%{_includedir}/onnxruntime/*
%{_libdir}/libonnxruntime.so
%{_libdir}/pkgconfig/libonnxruntime.pc

%changelog
* Wed Nov 03 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.9.1-1
- Release 1.9.1
