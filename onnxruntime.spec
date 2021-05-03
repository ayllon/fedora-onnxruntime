Summary:    A cross-platform inferencing and training accelerator compatible with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras, scikit-learn, and more
Name:       onnxruntime
Version:    1.7.2
Release:    1%{?dist}
License:    MIT
URL:        https://github.com/microsoft/onnxruntime
Source0:    https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz

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


%description
%{name} is a cross-platform inferencing and training accelerator compatible with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras, scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%prep
%autosetup -p1

%build
mkdir -p "%{_vpath_builddir}"
cd "%{_vpath_builddir}"
cmake -Donnxruntime_BUILD_SHARED_LIB=ON -Donnxruntime_DEV_MODE=OFF -Donnxruntime_BUILD_UNIT_TESTS=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
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

%changelog
* Fri Apr 30 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.7.2-1
- Release 1.7.2
