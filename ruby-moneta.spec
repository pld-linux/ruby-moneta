%define gemname moneta
Summary:	A unified interface to key/value stores
Name:		ruby-%{gemname}
Version:	0.6.0
Release:	0.1
License:	MIT
Group:		Development/Languages
URL:		http://github.com/wycats/moneta
Source0:	http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
# Source0-md5:	20b115b6feb9d0161b879ad37bf12110
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moneta provides a standard interface for interacting with various
kinds of key/value stores including Memcache, Redis, CouchDB, Berkeley
DB and many more.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO LICENSE
%{ruby_vendorlibdir}/moneta.rb
%{ruby_vendorlibdir}/moneta


%if 0
%files doc
%defattr(644,root,root,755)
%endif
