#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysubnettree
Version  : 0.32
Release  : 5
URL      : https://files.pythonhosted.org/packages/50/2a/279a44355aa16e21ac56b961958f357efb37641c83ca92db1874af5148d4/pysubnettree-0.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/2a/279a44355aa16e21ac56b961958f357efb37641c83ca92db1874af5148d4/pysubnettree-0.32.tar.gz
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pysubnettree-license = %{version}-%{release}
Requires: pysubnettree-python = %{version}-%{release}
Requires: pysubnettree-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
..
.. Version number is filled in automatically.
.. |version| replace:: 0.32
===============================================
PySubnetTree - A Python Module for CIDR Lookups
===============================================

%package license
Summary: license components for the pysubnettree package.
Group: Default

%description license
license components for the pysubnettree package.


%package python
Summary: python components for the pysubnettree package.
Group: Default
Requires: pysubnettree-python3 = %{version}-%{release}

%description python
python components for the pysubnettree package.


%package python3
Summary: python3 components for the pysubnettree package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pysubnettree package.


%prep
%setup -q -n pysubnettree-0.32
cd %{_builddir}/pysubnettree-0.32

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581283974
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pysubnettree
cp %{_builddir}/pysubnettree-0.32/COPYING %{buildroot}/usr/share/package-licenses/pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
