%define debug_package %{nil}

Summary:    A cross-platform inferencing and training accelerator compatible with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras, scikit-learn, and more
Name:       onnxruntime
Version:    1.5.2
Release:    2%{?dist}
License:    MIT
URL:        https://github.com/microsoft/onnxruntime
Source0:    https://github.com/microsoft/onnxruntime/archive/v%{version}/%{name}-%{version}.tar.gz

%description
%{name} is a cross-platform inferencing and training accelerator compatible with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras, scikit-learn, and more.

%package devel
Summary:    The development part of the %{name} package
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package

%prep
%autosetup -n onnxruntime-linux-x64-%{version}

%build
true

%install
mkdir -p "%{buildroot}/%{_includedir}/onnxruntime/"
mkdir -p "%{buildroot}/%{_libdir}/"
install -p -t "%{buildroot}/%{_includedir}/onnxruntime/" ./include/*
install -p -t "%{buildroot}/%{_libdir}/" ./lib/*.so.*
ln -s "libonnxruntime.so.%{version}" "%{buildroot}/%{_libdir}/libonnxruntime.so"

%files
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.*

%files devel
%dir %{_includedir}/onnxruntime/
%{_includedir}/onnxruntime/*
%{_libdir}/libonnxruntime.so

