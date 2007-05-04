# $Id$
# Authority: dag
# Upstream: Phillip Vandry <vandry$TZoNE,ORG>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name gettext

Summary: Perl module implementing message handling functions
Name: perl-gettext
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/gettext/

Source: http://www.cpan.org/authors/id/P/PV/PVANDRY/gettext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
gettext module is a Perl module implementing message handling functions.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/gettext.3pm*
%{perl_vendorarch}/gettext.pm
%{perl_vendorarch}/gettext.pod
%{perl_vendorarch}/auto/gettext/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
