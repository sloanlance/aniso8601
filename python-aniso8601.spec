%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%if (0%{?fedora} > 12 || 0%{?rhel} > 6)
%global with_python3 1
%endif

%global pkgname aniso8601
%global tarball_name aniso8601

Name:           python-aniso8601
Version:        0.82
Release:        1%{?dist}
Summary:        A Python library for parsing ISO 8601 strings

Group:          Development/Languages
License:        GPLv3+
URL:            https://bitbucket.org/nielsenb/aniso8601
Source0:        https://pypi.python.org/packages/source/a/aniso8601/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
%endif

%description
Library, implemented in pure Python, for parsing date strings
in ISO 8601 format into datetime format.

%if 0%{?with_python3}
%package -n python3-aniso8601
Summary: %{summary}

%description -n python3-aniso8601
Library, implemented in pure Python, for parsing date strings
in ISO 8601 format into datetime format.

This is the version for Python 3.x.
%endif

%prep
%setup -qn %{tarball_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

%build
%{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%check
PYTHONPATH=%{buildroot}/%{python_sitelib} %{__python2} -m unittest discover python2/aniso8601/tests/
%if 0%{?with_python3}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m unittest discover python3/aniso8601/tests/
%endif

%files
%doc COPYING README.rst
%{python_sitelib}/aniso8601
%{python_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-aniso8601
%doc COPYING README.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/aniso8601
%endif

%changelog
* Wed Jan 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-1
- initial packaging
