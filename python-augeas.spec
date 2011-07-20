Summary:	Python bindings to augeas
Summary(pl.UTF-8):	Wiązania Pythona do augeasa
Name:		python-augeas
Version:	0.4.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://augeas.net/download/python/%{name}-%{version}.tar.gz
# Source0-md5:	2c0c38686f6085168cf8591ef0251748
URL:		http://augeas.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
# library is dlopened
Requires:	augeas-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure Python bindings to augeas.

%description -l pl.UTF-8
Czysto pythonowe wiązania do augeasa.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.txt
%{py_sitescriptdir}/augeas.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_augeas-%{version}-py*.egg-info
%endif
