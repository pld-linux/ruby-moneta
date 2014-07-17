%define pkgname moneta
Summary:	A unified interface to key/value stores
Name:		ruby-%{pkgname}
Version:	0.6.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	20b115b6feb9d0161b879ad37bf12110
URL:		http://github.com/wycats/moneta
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

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO LICENSE
%{ruby_vendorlibdir}/moneta.rb
%{ruby_vendorlibdir}/moneta
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
