#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : anyjson
Version  : 0.3.3
Release  : 34
URL      : https://files.pythonhosted.org/packages/c3/4d/d4089e1a3dd25b46bebdb55a992b0797cff657b4477bc32ce28038fdecbc/anyjson-0.3.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/4d/d4089e1a3dd25b46bebdb55a992b0797cff657b4477bc32ce28038fdecbc/anyjson-0.3.3.tar.gz
Summary  : Wraps the best available JSON implementation available in a common interface
Group    : Development/Tools
License  : BSD-3-Clause
Requires: anyjson-license = %{version}-%{release}
Requires: anyjson-python = %{version}-%{release}
Requires: anyjson-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose-python

%description
##############################
anyjson - JSON library wrapper
##############################

%package license
Summary: license components for the anyjson package.
Group: Default

%description license
license components for the anyjson package.


%package python
Summary: python components for the anyjson package.
Group: Default
Requires: anyjson-python3 = %{version}-%{release}

%description python
python components for the anyjson package.


%package python3
Summary: python3 components for the anyjson package.
Group: Default
Requires: python3-core
Provides: pypi(anyjson)

%description python3
python3 components for the anyjson package.


%prep
%setup -q -n anyjson-0.3.3
cd %{_builddir}/anyjson-0.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582845859
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/anyjson
cp %{_builddir}/anyjson-0.3.3/LICENSE %{buildroot}/usr/share/package-licenses/anyjson/45837c933d276477fcf0296f7bd8f2a51906e97e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/anyjson/45837c933d276477fcf0296f7bd8f2a51906e97e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
