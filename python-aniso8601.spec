%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if (0%{?fedora} > 12)
%global with_python3 1
%endif

%global pkgname aniso8601
%global tarball_name aniso8601

Name:           python-aniso8601
Version:        0.93dev
Release:        1%{?dist}
Summary:        Python 2 library for parsing ISO 8601 strings

Group:          Development/Languages
License:        BSD
URL:            https://bitbucket.org/nielsenb/aniso8601
Source0:        https://pypi.python.org/packages/source/a/aniso8601/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
%endif

%description
This is a Python 2 library for parsing date strings
in ISO 8601 format into datetime format.

%if 0%{?with_python3}
%package -n python3-aniso8601
Summary:        Python 3 library for parsing ISO 8601 strings

%description -n python3-aniso8601
This is a Python 3 library for parsing date strings
in ISO 8601 format into datetime format.
%endif

%prep
%setup -qn %{tarball_name}-%{version}
rm -rf %{tarball_name}.egg-info

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

%if ! 0%{?rhel} || 0%{?rhel} > 6
%check
PYTHONPATH=%{buildroot}/%{python_sitelib} %{__python2} -m unittest discover aniso8601/tests/
%if 0%{?with_python3}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m unittest discover aniso8601/tests/
%endif
%endif

%files
%doc LICENSE README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-aniso8601
%doc LICENSE README.rst
%{python3_sitelib}/*

%endif

%changelog
* Thu Dec 18 2014 Brandon Nielsen <nielsenb@jetfuse.net> - 0.91dev-1
- update for merged python2 / python3 trees

* Tue Nov 18 2014 Jan Sedlak <jsedlak@redhat.com> - 0.85-1
- change license to BSD, new version

* Thu May 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-2
- disabled tests for EL6

* Wed Jan 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-1
- initial packaging
