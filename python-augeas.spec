#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	augeas
Summary:	Python bindings to augeas
Summary(pl.UTF-8):	Wiązania Pythona do augeasa
Name:		python-%{module}
Version:	0.4.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://fedorahosted.org/released/python-augeas/%{name}-%{version}.tar.gz
# Source0-md5:	cf5742a6e84c1cc894cedd1984aaa915
URL:		http://augeas.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-devel
%endif
%if %{with python3}
BuildRequires:	python3-devel
%endif
# library is dlopened
Requires:	augeas-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure Python bindings to augeas.

%description -l pl.UTF-8
Czysto pythonowe wiązania do augeasa.

%package -n python3-%{module}
Summary:	Python bindings to augeas
Summary(pl.UTF-8):	Wiązania Pythona do augeasa
Group:		Libraries/Python

%description -n python3-%{module}
Pure Python bindings to augeas.

%description -n python3-%{module} -l pl.UTF-8
Czysto pythonowe wiązania do augeasa.

%prep
%setup -q

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS README.txt
%{py_sitescriptdir}/augeas.py[co]
%{py_sitescriptdir}/python_augeas-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS README.txt
%{py3_sitescriptdir}/augeas.py
%{py3_sitescriptdir}/python_augeas-%{version}-py*.egg-info
%endif
