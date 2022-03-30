#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		siphashc
%define		egg_name	siphashc
%define		pypi_name	siphashc
Summary:	Python module for siphash
Name:		python-%{pypi_name}
Version:	0.8
Release:	8
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	f2078b9c12d4650a67ad29ab4c63d8cc
URL:		https://github.com/WeblateOrg/siphashc
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
Obsoletes:	python-siphashc3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for siphash, based on floodberry's version.

%package -n python3-%{pypi_name}
Summary:	Python module for siphash
Group:		Libraries/Python
Requires:	python3-modules
Obsoletes:	python3-siphashc3

%description -n python3-%{pypi_name}
Python module for siphash, based on floodberry's version.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -r %{pypi_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/%{module}.*.so
%{py3_sitedir}/%{egg_name}-%{version}-py*.egg-info
%endif
