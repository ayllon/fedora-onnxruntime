Summary:    A cross-platform inferencing and training accelerator compatible with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras, scikit-learn, and more
Name:       onnxruntime
Version:    1.5.2
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
%cmake -B "%{_vpath_builddir}" -Donnxruntime_DEV_MODE=OFF \
    -Donnxruntime_BUILD_SHARED_LIB=ON -Donnxruntime_BUILD_UNIT_TESTS=OFF \
    cmake
%make_build -C "%{_vpath_builddir}"

%install
%make_install -C "%{_vpath_builddir}"

%files
%license LICENSE
%doc docs/*
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so*
%{_includedir}/onnxruntime/*

