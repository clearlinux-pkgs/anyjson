#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : anyjson
Version  : 0.3.3
Release  : 24
URL      : https://pypi.python.org/packages/source/a/anyjson/anyjson-0.3.3.tar.gz
Source0  : https://pypi.python.org/packages/source/a/anyjson/anyjson-0.3.3.tar.gz
Summary  : Wraps the best available JSON implementation available in a common interface
Group    : Development/Tools
License  : BSD-3-Clause
Requires: anyjson-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
##############################
anyjson - JSON library wrapper
##############################

%package python
Summary: python components for the anyjson package.
Group: Default

%description python
python components for the anyjson package.


%prep
%setup -q -n anyjson-0.3.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484529298
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1484529298
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
