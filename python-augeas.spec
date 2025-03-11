#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	augeas
Summary:	Python 2.x bindings to augeas
Summary(pl.UTF-8):	Wiązania Pythona 2.x do augeasa
Name:		python-%{module}
Version:	0.5.0
Release:	14
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://fedorahosted.org/released/python-augeas/%{name}-%{version}.tar.gz
# Source0-md5:	2d5a903467410b8d60abca5fa54bae2d
URL:		http://augeas.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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
Pure Python bindings to augeas, built for Python 2.x.

%description -l pl.UTF-8
Czysto pythonowe wiązania do augeasa, zbudowane dla Pythona 2.x.

%package -n python3-%{module}
Summary:	Python 3.x bindings to augeas
Summary(pl.UTF-8):	Wiązania Pythona 3.x do augeasa
Group:		Libraries/Python

%description -n python3-%{module}
Pure Python bindings to augeas, built for Python 3.x.

%description -n python3-%{module} -l pl.UTF-8
Czysto pythonowe wiązania do augeasa, zbudowane dla Pythona 3.x.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
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
%{py3_sitescriptdir}/__pycache__/augeas.cpython-*.py[co]
%{py3_sitescriptdir}/python_augeas-%{version}-py*.egg-info
%endif
